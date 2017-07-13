#!/usr/bin/env python

from collections import defaultdict
from math import log
import datetime
import json
import re
import sys
import traceback

from lxml.cssselect import CSSSelector
from matplotlib import pyplot as plt
from matplotlib import markers
#from IPython.display import HTML
import lxml.html
import matplotlib as mpl
import numpy
import requests

from scales import linear

try:
    import seaborn as sns
except ImportError:
    print "Seaborn style not installed"

date = datetime.date
problems = {}
metrics = {}
measurements = set() # we don't try to guarantee unique names for these, so use a set
all_attributes = set()

class Problem:
    def __init__(self, name, attributes=[], solved=False, url=None):
        self.name = name
        self.attributes = attributes
        for a in attributes:
            global all_attributes
            all_attributes.add(a)
        self.subproblems = []
        self.superproblems = []
        self.metrics = []
        self.solved = solved
        self.url = url
        global problems, metrics
        problems[name] = self
        
    def add_subproblem(self, other_problem):
        # add this other problem as a subproblem of us
        other_problem.superproblems.append(self)
        self.subproblems.append(other_problem)
        
    def metric(self, *args, **kwargs):
        m = Metric(*args, **kwargs)
        m.parent = self
        self.metrics.append(m)
        return m
    
    def check_solved(self):
        if all(m.solved for m in self.metrics + self.subproblems):
            self.solved = True
            for p in self.superproblems:
                p.check_solved()
    
    def __str__(self):
        return "Problem({0})".format(self.name)
    
    def print_structure(self, indent=0):
        print indent * " " + str(self)
        for m in self.metrics:
            print (indent + 4) * " " + str(m)
        for p in self.subproblems:
            p.print_structure(indent + 4)
    
    def tables(self):
        return render_tables(self.metrics)

mpl.rcParams["legend.fontsize"] = u"x-small"
mpl.rcParams["xtick.labelsize"] = u"xx-small"
mpl.rcParams["ytick.labelsize"] = u"x-small"

class Metric:
    def __init__(self, name, url=None, solved=False, notes="", scale=linear, target=None, target_source=None,
                 parent=None, changeable=False, axis_label=None, target_label=None, data_url=None):
        self.name = name
        self.measures = []
        self.solved = solved
        self.url = url
        self.notes = notes
        self.scale = scale
        self.target = target
        self.target_source = target_source # Source for human-level performance number
        self.changeable = changeable # True if a metric changes over time
        self.graphed = False
        global metrics
        metrics[name] = self
        self.parent = parent
        self.target_label = target_label
        self.axis_label = (     axis_label            if axis_label 
                           else self.scale.axis_label if hasattr(self.scale, "axis_label") 
                           else self.name)
        # primarily used by the table() method
        self.data_url = self.find_edit_url() if data_url is None else data_url
        
    def __str__(self):
        solved = "SOLVED" if self.solved else "?" if not self.target else "not solved"
        return "{0:<60}{1}".format("Metric(%s)" % self.name, solved)
        
    def measure(self, *args, **kwargs):
        try:
            m = Measurement(*args, **kwargs)
        except AssertionError:
            print "WARNING, failed to create measurement", args, kwargs
            traceback.print_exc()
            return None
        m.metric = self
        if self.target:
            if self.target_source == m.url and self.target == m.value:
                print "Skipping apparent human performance (target_source) paper", m.url
                return None
            if self.scale.improvement(self.target, m.value) >= 0:
                self.solved = True
                self.parent.check_solved()
        self.measures.append(m)
        return m

    def find_edit_url(self):
        "Some magic hackery to find what file and line number a Metric was defined on and produce an edit link"
        try:
            # Deliberately trigger an exception so that we can inspect the stack
            import nosuchthing
        except:
            # find where this metric was defined. The stack looks like this:
            #   0. Metric.find_edit_url; 
            #   1. Metric.__init__; 
            #   2. Problem.metric; 
            #   3. someproblem.meric() in a data/*.py file
            tb_frame = sys._getframe(3) 
            line = tb_frame.f_lineno
            filename = tb_frame and tb_frame.f_code and tb_frame.f_code.co_filename
            if filename:
                return "https://github.com/AI-metrics/AI-metrics/edit/master/{0}#L{1}".format(filename, line)
            else:
                return "https://github.com/AI-metrics/AI-metrics"

    def table(self):
        if len(self.measures) < 2:
            return u""

        # TODO: split out CSS
        table_html = ['<table style="width: 100%">']
        table_html.append("<caption>{0}</caption>".format(self.name))
        col = 'style="background-color: #f7f7f7"'
        table_html.append("<tr {1}><th>Date</th><th>Algorithm</th><th>{0}</th><th>Paper / Source</th></tr>".format(self.scale.col_label, col))
        widest_alg = max(len(m.name) for m in self.measures)
        alg_bound = 'style="width: 25%"' if widest_alg >= 45 else ""
        for n, m in enumerate(self.measures):
            bgcol = 'style="background-color: #f7f7f7"' if n % 2 == 1 else ''
            table_html.append("<tr {0}>".format(bgcol))
            table_html.append('<td align="center" style="width: 10%">{0}</td>'.format(m.date))
            table_html.append('<td align="center" {1}>{0}</td>'.format(m.name, alg_bound))
            table_html.append('<td align="center">{0}</td>'.format(m.value))
            source = ' (<a href="{0}">source code</a>)'.format(m.replicated_url) if m.replicated_url else ""
            table_html.append('<td align="center"><a href=\"{0}\">{1}</a>{2}</td>'.format(m.url, m.papername if m.papername else m.url, source))
            table_html.append("</tr>")
        table_html.append("</table>")
        github_link = ['<div style="text-align: right; font-style: italic"><a href="{0}">Edit/add data on GitHub</a></div>'.format(self.data_url)]
        html = "".join(table_html + github_link)
        return html

    def graph(self, size=(7,5), scale=1.0):
        if len(self.measures) < 2:
            return
        fig = plt.figure(dpi=300)
        fig.set_size_inches((7*scale, 5*scale))
        #fig.add_subplot(111).set_ylabel(self.name)
        subplot = fig.add_subplot(111)
        subplot.set_ylabel(self.axis_label)
        subplot.set_title(self.name)
        #fig.add_subplot(111).set_ylabel(self.name)
        
        self.measures.sort(key=lambda m: (m.date, m.metric.scale.pseudolinear(m.value)))
        
        # scatter plot of results in the literature
        available_markers = markers.MarkerStyle().markers
        for n, m in enumerate(self.measures):
            kwargs = {"c": "r"}
            if self.target and self.scale.improvement(self.target, m.value) >= 0:
                kwargs["c"] = "b"
            if m.not_directly_comparable or self.changeable:
                kwargs["c"] = "#000000"
                if "*" in available_markers:
                    kwargs["marker"] = "*"
            if m.withdrawn:
                if "X" in available_markers:
                    kwargs["marker"] = "X"
                kwargs["c"] = "#aaaaaa"
            plt.plot_date([m.date], [m.value], **kwargs)
                
            plt.annotate('%s' % m.label, xy=(m.date, m.value), xytext=m.metric.scale.offset, fontsize=scale * 6, textcoords='offset points')
            # cases where either results or dates of publication are uncertain
            kwargs = {"c": "#80cf80", "linewidth": scale*1.0, "capsize": scale*1.5, "capthick": scale*0.5, "dash_capstyle": 'projecting'}
                
            if m.min_date or m.max_date:
                before = (m.date - m.min_date) if m.min_date else datetime.timedelta(0)
                after = (m.max_date - m.date) if m.max_date else datetime.timedelta(0)
                kwargs["xerr"] = numpy.array([[before], [after]])
            if self.measures[n].value != self.measures[n].minval:
                kwargs["yerr"] = numpy.array([[m.value - self.measures[n].minval], [self.measures[n].maxval - m.value]])
            if "xerr" in kwargs or "yerr" in kwargs:
                subplot.errorbar(m.date, m.value, **kwargs)
        
        # line graph of the frontier of best results
        if not self.changeable:
            best = self.measures[0].value
            frontier_x, frontier_y = [], []
            for m in self.measures:
                if self.scale.improvement(best, m.value) >= 0 and not m.withdrawn and not m.not_directly_comparable:
                    frontier_x.append(m.date)
                    frontier_y.append(m.value)
                    xy = (m.date, m.value)       
                    best = m.value
            plt.plot_date(frontier_x, frontier_y, "g-")
        
        # dashed line for "solved" / strong human performance
        if self.target:
            target_label = (       self.target_label  if self.target_label
                             else "Human performance" if self.parent and "agi" in self.parent.attributes
                             else "Target")
            start = min([self.measures[0].date]  + [m.min_date for m in self.measures if m.min_date])
            end =   max([self.measures[-1].date] + [m.max_date for m in self.measures if m.max_date])

            plt.plot_date([start, end], 2 * [self.target], "r--", label=target_label)
            
        plt.legend()
        plt.show()
        self.graphed = True

def render_tables(metrics):
    "Jupyter Notebook only lets you call HTML() once per cell; this function emulates doing it several times"
    table_html = u""
    for m in metrics:
        html = m.table()
        if html is not None:
            table_html += html
    #HTML(table_html)
    return table_html

def canonicalise(url):
    if not url:
        return ""
    if url.startswith("http://arxiv.org"):
        url = url.replace("http", "https")
    if url.startswith("https://arxiv.org/pdf/"):
        url = url.replace("pdf", "abs", 1)
        url = url.replace(".pdf", "", 1)
    return url
# dates of conferences help us date papers from the "Are We There Yet" dataset
conference_dates = {"ICML 2016": date(2016, 6, 19),
                    "NIPS 2015": date(2015, 12, 7),
                    "ICLR 2014": date(2014, 4, 14),
                    "ICML 2012": date(2012, 6, 26),
                    "ICML 2013": date(2013, 6, 16),
                    "ICML 2014": date(2014, 6, 21),
                   "IJCNN 2015": date(2015, 7, 12),
                    "CVPR 2012": date(2012, 6, 16),
                    "NIPS 2012": date(2012, 12, 3),
                    "CVPR 2015": date(2015, 6, 8),
                    "NIPS 2011": date(2011, 12, 17),
                    "NIPS 2014": date(2014, 12, 8),
               "TUM-I1222 2013": date(2013, 10, 29),
                     "WMT 2014": date(2014, 2, 24),
                    "ECCV 2012": date(2012, 10, 7)}
conferences_wanted = defaultdict(lambda: 0)

offline = False
try:
    r = requests.get('http://arxiv.org/abs/1501.02876')
    if str(r.status_code).startswith("4"):
        offline = True
        print "Arxiv blocked!"
except requests.ConnectionError:
    print "In Offline mode!"
    offline = True

class Measurement:
    def __init__(self, d, value, name, url, algorithms=[], uncertainty=0, minval=None, maxval=None, opensource=False, replicated="",
                 papername=None, venue=None, min_date=None, max_date=None, algorithm_src_url=None, withdrawn=False, 
                 not_directly_comparable=False, long_label=False, notes=""):
        self.date = d
        self.value = value
        assert isinstance(value, float) or isinstance(value, int), "Measurements on metrics need to be numbers"
        self.name = name
        
        # For papers on arxiv, always use the abstract link rather than the PDF link
        self.url = canonicalise(url)
        assert self.url or papername, "Measurements must have a URL or a paper name"
        self.min_date = min_date
        self.max_date = max_date
        self.aglorithm_src_url = algorithm_src_url
        if algorithm_src_url and not min_date:
            _, prev_dates, _ = ade.get_paper_data(algorithm_src_url)
            if prev_dates:
                self.min_date = min(prev_dates.values())
                    
        self.minval = minval if minval else value - uncertainty
        self.maxval = maxval if maxval else value + uncertainty
        self.opensource = opensource
        self.not_directly_comparable = not_directly_comparable
        self.replicated_url = replicated
        self.long_label = long_label
        self.algorithms = algorithms
        self.notes = notes
        arxiv_papername, arxiv_dates, arxiv_withdrawn = ade.get_paper_data(self.url)
        self.withdrawn = withdrawn or arxiv_withdrawn 
        if "arxiv.org" in self.url and not offline:
            assert arxiv_dates, "Failed to extract arxiv dates for "+ self.url
        self.papername = papername if papername else arxiv_papername
        self.determine_paper_dates(d, arxiv_dates, venue)
        self.set_label()
            
        global measurements
        measurements.add(self)

    def set_label(self):
        self.label = self.name
        if self.withdrawn and not "withdrawn" in self.label.lower():
            self.label = "WITHDRAWN " + self.label
        if len(self.label) >= 28 and not self.long_label:
            self.label = self.label[:25] + "..."

    year_re=re.compile(r"([0-9][0-9][0-9][0-9])")
    def determine_paper_dates(self, d, arxiv_dates, venue):
        """
        Try to figure out when a result was obtained, and our uncertainty on that.
        
        :param datetime.date d: date supplied at paper entry time. We may not be able to trust this if the paper had multiple versions
                                   and the person doing the entry didn't specify which version they got their result numbers from :/
        :param dict arxiv_dates:   either None or a dict like {"1": date(2017,1,13), "2": date(2017, 3, 4)...}
        :param venue:              for Rodriguo Benenson's data, a publication venue like "ICML 2016" or "arXiv 2014"
        """
        # begin by trusting whoever entered the data
        self.date = d

        # but warn if it doesn't match arXiv dates
        adates = sorted(arxiv_dates.values()) if arxiv_dates else []

        if arxiv_dates and d:
            if d < min(adates) and d > max(adates):
                print "WARNING, date", self.date, "for", self.url, 
                print "does not match any of the arXiv versions (%s)" % " ".join(str(s) for s in arxiv_dates.values())
        if arxiv_dates:
            if len(arxiv_dates) == 1:
                if not self.date:
                    self.date = adates[0]
            else:
                # multiple arxiv dates means the url wasn't versioned, and we might not have gotten the date exactly right
                self.min_date = self.min_date if self.min_date else min(adates)
                self.max_date = self.max_date if self.max_date else max(adates)
                if not self.date:
                    midrange = datetime.timedelta(days=0.5 * (self.max_date - self.min_date).days)
                    self.date = self.min_date + midrange
        elif venue and not self.date:
            # if all we have is a conference / journal, we might be able to still figure something out..
            if venue.upper() in conference_dates:
                self.date = conference_dates[venue]
            else:
                conferences_wanted[venue] += 1
                year = int(self.year_re.search(venue).groups(0)[0])
                self.date = date(year, 7, 1)
                self.min_date = date(year, 1, 1)
                self.max_date = date(year, 12, 31)
        if not self.date:
            print d, arxiv_dates, venue
        assert self.date, "Need a date for paper {0} {1}".format(self.url, self.papername)

#print canonicalise('http://arxiv.org/pdf/1412.6806.pdf')
#cifar10.measure(None, 96.53, 'Fractional Max-Pooling', 'http://arxiv.org/abs/1412.6071', 
# papername='Fractional Max-Pooling', venue='arXiv 2015')
#cifar10.measure(None, 95.59, 'Striving for Simplicity: The All Convolutional Net', 
# 'http://arxiv.org/pdf/1412.6806.pdf', papername='Striving for Simplicity: The All Convolutional Net', venue='ICLR 2015')

# simple hooks for letting us save & restore datetime.date objects in a JSON cache
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return str(obj)
        return super(MyEncoder, self).default(obj)

def parse_date(json_dict):
    if "dates" in json_dict:
        for v, date_str in json_dict["dates"].items():
            json_dict["dates"][v] = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return json_dict


class ArxivDataExtractor:
    def __init__(self):
        try:
            with open(".paper_cache.json") as f:
                self.cache = json.load(f, object_hook=parse_date)
        except:
            print "Failed to load local paper cache, trying a network copy..."
            try:
                req = requests.get('https://raw.githubusercontent.com/AI-metrics/master_text/master/.paper_cache.json')
                self.cache = json.loads(req.content, object_hook=parse_date)
            except:
                traceback.print_exc()
                print "(Continuing with an empty cache)"
                self.cache = {}
        self.arxiv_re = re.compile(r"\[[0-9v.]+\] (.*)")
        
    def save_cache(self):
        try:
            with open(".paper_cache.json", "w") as f:
                json.dump(self.cache, f, indent=4, sort_keys=True, cls=DateEncoder)
        except:
            traceback.print_exc()
            print "Not able to save cache"
    
    ends_with_version = re.compile(r".*v([0-9])+$")
    def arxiv_link_version(self, url):
        m = self.ends_with_version.match(url)
        if m:
            return m.group(1)
        else:
            return None
        
    multiwhitespace = re.compile(r"\s+")  # gets rid of newlines
    def get_paper_data(self, url):
        "Ask arxiv for a (papername, {version:date}) if we don't know it"
        if not url:
            return (None, None, None)    
        if url in self.cache:
            c = self.cache[url]
            return (c["name"], c.get("dates"), c.get("withdrawn", False))
        
        try:
            req = requests.get(url)
        except requests.ConnectionError:
            print "Failed to fetch", url
            #traceback.print_exc()
            return (None, None, None)
        record = {}
        tree = lxml.html.fromstring(req.content)
        withdrawn = self.detect_withdrawn(tree, url)
        if withdrawn:
            record["withdrawn"] = True
        #papername = CSSSelector("title")(tree)[0].text_content()
        papername = tree.findtext('.//title')
        dates = None
        if papername:
            papername = self.multiwhitespace.sub(" ", papername)
            match = self.arxiv_re.match(papername)
            if match:
                papername = match.groups(0)[0]
                v = self.arxiv_link_version(url)
                dates = self.get_submission_dates(tree, v)
                record["dates"] = dates
        record["name"] = papername
        self.cache[url] = record
        print "Caching paper name:", papername
        self.save_cache()
        return papername, dates, withdrawn
    
    def detect_withdrawn(self, tree, url):
        comment = CSSSelector(".tablecell.comments")(tree)
        if comment:
            comment = comment[0].text_content()
            if "withdrawn" in comment.lower():
                print "Paper", url, "appears to be withdrawn!"
                return True
        return False

    version_re = re.compile(r"\[v([0-9]+)\] (.*[0-9][0-9][0-9][0-9]) ")

    def get_submission_dates(self, arxiv_tree, queried_version):
        links = CSSSelector("div.submission-history")(arxiv_tree)[0]
        versions = {}
        #print "Parsing", links.text_content()
        for line in links.text_content().split("\n"):
            match = self.version_re.match(line)
            if match:
                version, d = match.group(1), match.group(2)
                d = datetime.datetime.strptime(d,'%a, %d %b %Y').date()
                versions[version] = d
                if queried_version == version:
                    return {version: d}
                #print version, date

        return versions

ade = ArxivDataExtractor()

#ade.get_paper_data("https://arxiv.org/abs/1501.02876")


