#!/usr/bin/env ipython

import re
import os

import lxml
from lxml.cssselect import CSSSelector
import requests

from taxonomy import offline
from data.vision import *

# So we can pipe the output of this code somewhere
os.environ["PYTHONIOENCODING"] = "utf-8"

# Rodriguo Benenson's "Are We There Yet?" data!
reimport_awty = True
if reimport_awty and not offline:
    # Fetch the summary page
    awty_url = "https://rodrigob.github.io/are_we_there_yet/build/"
    req = requests.get(awty_url)
    page = req.content.replace("</html>", "", 1) # There is a crazy weird </html> near the top of the page that breaks everything
    tree = lxml.html.fromstring(page)

from urlparse import urlparse
awty_datasets = {}

if reimport_awty and not offline:
    for e in CSSSelector('div.span7')(tree):
        #print dir(e)
        node = e.getchildren()[0].getchildren()[0]
        link = node.attrib["href"]
        metric_name = node.text_content()
        print "%40s" % metric_name, link
        awty_datasets[metric_name] = urlparse(link)

try:
    got = json.load(open(".awty_cache.json"))
except:
    got = {}
    

# For lots of AWTY data, there's no date but there is a conference, so we can look up the dates that way.
conf_dates = {}


def parse_awty_dataset(name, link, verbose=False):
    if offline or not reimport_awty: return []
    print "# Handling", repr(name), link.geturl()
    if link.path not in got:
        page = requests.get(awty_url + link.path).content
        tree = lxml.html.fromstring(page.replace("</html>", "", 1))
        got[link.path] = tree
    else:
        tree = got[link.path]
    #print dir(tree)
    #print "fragment:", link.fragment
    #print page
    results_section = CSSSelector("div#" + link.fragment)(tree)[0]
    
    rows = CSSSelector("tr")(results_section)
    results = []
    for r in rows[1:]:
        result, paperlink, journal, details = CSSSelector("td")(r)
        result, papername, journal = [e.text_content() for e in (result, paperlink, journal)]
        notes = CSSSelector("div")(details)
        notes = notes[0].text_content().strip() if notes else ""
        notes = re.sub("\s+", " ", notes, flags=re.UNICODE)
        assert isinstance(notes, str) or isinstance(notes, unicode), "Expecting stringy notes %s " % type(notes)
        if "%" not in result:
            print "# Skipping", result, papername, journal
            continue
        if verbose: 
            print "%6s" % result, "%90s" % papername, "%10s" %journal, notes
        e = CSSSelector("a")(paperlink)
        paper_url = e[0].attrib["href"] if e else None
        results.append((result, papername, paper_url, journal, notes))
    return results

percent_re = re.compile(r'([0-9.]+) *% *(\(?±([0-9\.]+))?')
done = {}
def ingest_awty_dataset(name, metric, label, regex=percent_re):
    if offline or not reimport_awty:
        #print "Offline, not ingesting", name
        return None
    done[name] = True
    for n, (result, papername, paper_url, journal, notes) in enumerate(parse_awty_dataset(name, awty_datasets[name])):
        try:
            match = regex.match(result)
            value = float(match.group(1))
        except AttributeError:
            print "result", result, "does not parse"
            continue

        try:
            uncertainty = float(match.group(3)) if match.group(3) else 0.0
        except IndexError:
            uncertainty = 0.0

        #if "Graph Cut based inference" in papername or "Spatial and Global Constraints Really" in papername or (paper_url and'http://research.microsoft.com/en-us/um/people/pkohli/papers/lrkt_eccv2010.pdf' in paper_url):

        print "%s.measure(%s, %r, %r, url=%r, papername=%r, uncertainty=%r, venue=%r, notes=%r)" % (
               label, None, value, papername, paper_url,  papername, uncertainty, journal, notes)
        try:
            metric.measure(None, value, papername, url=paper_url, papername=papername, 
                           uncertainty=uncertainty, venue=journal, notes=notes)
        except requests.ConnectionError, e:
            print "Network error on {0} ({1}), skipping:".format(paper_url, papername)
            print e

msrc21_pc = image_classification.metric("MSRC-21 image semantic labelling (per-class)", "http://jamie.shotton.org/work/data.html", scale=correct_percent)
msrc21_pp = image_classification.metric("MSRC-21 image semantic labelling (per-pixel)", "http://jamie.shotton.org/work/data.html", scale=correct_percent)


cifar100 = image_classification.metric("CIFAR-100 Image Recognition", "http://https://www.cs.toronto.edu/~kriz/cifar.html", scale=correct_percent)

cifar10 = image_classification.metric("CIFAR-10 Image Recognition", "http://https://www.cs.toronto.edu/~kriz/cifar.html", scale=correct_percent, target=94, target_source="http://karpathy.github.io/2011/04/27/manually-classifying-cifar10/")

svhn = image_classification.metric("Street View House Numbers (SVHN)", "http://ufldl.stanford.edu/housenumbers/", scale=error_percent, target=2.0, target_source="http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf")

# We declare MNIST solved because the gap between best performance and human performance appears to be less than the uncertainty in human performance
mnist = image_classification.metric("MNIST handwritten digit recognition", "http://yann.lecun.com/exdb/mnist/", scale=error_percent, target=0.2, target_source="http://people.idsia.ch/~juergen/superhumanpatternrecognition.html", solved=True)

# This awty URL broken
mnist.measure(date(2013,2,28), 0.52, 'COSFIRE', 'http://www.rug.nl/research/portal/files/2390194/2013IEEETPAMIAzzopardi.pdf', papername='Trainable COSFIRE Filters for Keypoint Detection and Pattern Recognition')
# awty transcribes what's in this paper, but it seems to somehow have confused, wildly different units from everything else:
for i, m in enumerate(mnist.measures):
    if m.url == "http://personal.ie.cuhk.edu.hk/~ccloy/files/aaai_2015_target_coding.pdf":
        del mnist.measures[i]

stl10 = image_classification.metric("STL-10 Image Recognition", "https://cs.stanford.edu/~acoates/stl10/", scale=correct_percent)
if not offline: ingest_awty_dataset('STL-10', stl10, 'stl10')

leeds_sport_poses = image_classification.metric("Leeds Sport Poses")

if reimport_awty and not offline:
    ingest_awty_dataset('SVHN', svhn, 'svhn')
    ingest_awty_dataset('CIFAR-100', cifar100, 'cifar100')
    ingest_awty_dataset('CIFAR-10', cifar10, 'cifar10')
    ingest_awty_dataset('MNIST', mnist, 'mnist')
    ingest_awty_dataset('MSRC-21', msrc21_pc, 'msrc21_pc')
    ingest_awty_dataset('MSRC-21', msrc21_pp, 'msrc21_pp', regex=re.compile("[0-9.]+ *% */ * ([0-9.]+) *%"))

    for name, link in awty_datasets.items():
        if not link.scheme and name not in done:
            parse_awty_dataset(name, link, verbose=True)

if reimport_awty and not offline:
    ingest_awty_dataset('SVHN', svhn, 'svhn')
    ingest_awty_dataset('CIFAR-100', cifar100, 'cifar100')
    ingest_awty_dataset('CIFAR-10', cifar10, 'cifar10')
    ingest_awty_dataset('MNIST', mnist, 'mnist')
    ingest_awty_dataset('MSRC-21', msrc21_pc, 'msrc21_pc')
    ingest_awty_dataset('MSRC-21', msrc21_pp, 'msrc21_pp', regex=re.compile("[0-9.]+ *% */ * ([0-9.]+) *%"))

    for name, link in awty_datasets.items():
        if not link.scheme and name not in done:
            parse_awty_dataset(name, link, verbose=True)
