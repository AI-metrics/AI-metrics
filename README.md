# Description

A text document to contain data to explore the progression of AI through the amalgamation and display of datasets relating
to the progress of AI, such as image recognition scores over time, or Hutter Prize compression. Both qualitative and
quantitative information, with a bias towards quantitative. Initial version will consist of a basic text document on GitHub,
which multiple organizations will collaborate on. This will likely eventually yield an OpenAI-specific project as well. 

# Purpose

* Improve the public discourse around AI by equipping journalists, politicians, and the public with a single web page containing easy to comprehend data. 
* Help our fellow researchers by giving them a useful resource to scan when looking for relevant scores/results in their own knowledge domain.
* Create a self-reinforceing system to get researchers to proactively share great new results in a shared, public knowledge base. 

# How to contribute to this notebook

This notebook is an open source, community effort. You can help by adding new metrics, data and problems to it! If you're feeling ambitious you can also improve its semantics or build new analyses into it. Here are some high level tips on how to do that.

### 1. If you're comfortable with git and Jupyter Notebooks, or are happy to learn

If you've already worked a lot with `git` and IPython/Jupyter Notebooks, here's a quick list of things you'll need to do:

1. Install [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
    * On an Ubuntu or Debian system, you can do: <br><pre>sudo apt-get install git
      sudo apt-get install ipython-notebook || sudo apt-get install jupyter-notebook || sudo apt-get install python-notebook</pre>
2. Install this notebook's Python dependencies:<br>
    * On Ubuntu or Debian, do: <br><pre>    sudo apt-get install python-{cssselect,lxml,matplotlib{,-venn},numpy,requests,seaborn}</pre>
    * On other systems, use your native OS packages, or use `pip`: <br><pre>    pip install cssselect lxml matplotlib{,-venn} numpy requests seaborn</pre>
3. Fork our repo on github `<LINK>`
4. Configure your copy of git to use [IPython Notebook merge filters](http://pascalbugnion.net/blog/ipython-notebooks-and-git.html) to prevent conflicts when multiple people edit the Notebook simultaneously. You can do that with these two commands in the cloned repo:
    <pre>git config --file .gitconfig filter.clean_ipynb.clean ipynb_drop_output</pre>
    <pre>git config --file .gitconfig filter.clean_ipynb.smudge cat</pre>
5. Run Jupyter Notebok in the project directory (the command may be `ipython notebook`, `jupyter notebook`, `jupyter-notebook`, or `python notebook` depending on your system), then go to [localhost:8888](http://localhost:8888) and edit the Notebook to your heart's content
6. Save and commit your work (`git commit -a -m "DESCRIPTION OF WHAT YOU CHANGED"`)
7. Push it to your remote repo
8. Send us a pull request!


### 2. If you want something very simple

Microsoft Azure has an IPython / Jupyter service that will let you run and modify notebooks from their servers. You can clone this Notebook and work with it via their service: https://notebooks.azure.com/anon-uotycg/libraries/ai-progress. Unfortunately there are a few issues with running the notebook on Azure:

* arXiv seems to block requests from Azure's IP addresses, so it's impossible to automatically extract information about paper when running the Notebook there
* The Azure Notebooks service seems to transform Unicode characters in strange ways, creating extra work merging changes from that source


## Notes on importing data

* Each `.measure()` call is a data point of a specific algorithm on a specific metric/dataset. Thus one paper will often produce multiple measurements on multiple metrics. It's most important to enter results that were at or near the frontier of best performance on the date they were published, though this isn't a strict requirement and it's nice to have a sense of the performance of the field, or of algorithms that are otherwise notable even if they aren't the frontier for a sepcific problem.
* When multiple revisions of a paper (typically on arXiv) have the same results on some metric, use the date of the first version (the CBTest results in [this paper](https://arxiv.org/abs/1606.02245v4) are an example)
* When subsequent revisions of a paper improve on the original results ([example](https://arxiv.org/abs/1606.01549v3)), use the date and scores of the first results, or if each revision is interesting / on the frontier of best performance, include each paper
  * We didn't check this carefully for our first ~100 measurement data points :(. In order to denote when we've checked which revision of an arXiv preprint first published a result, cite the specific version (https://arxiv.org/abs/1606.01549v3 rather than https://arxiv.org/abs/1606.01549); that way we can see which previous entries should be double-checked for this form of inaccuracy.
* Where possible, use a clear short name or acronym for each algorithm. The full paper name can go in the `papername` field (and is auto-populated for some papers). When matplotlib 2.1 ships we may be able to get nice [rollovers](https://github.com/matplotlib/matplotlib/pull/5754) with metadata like this. Or perhaps we can switch to D3 to get that type of interactivity.



## What to work on

* If you know of ML datasets/metrics that aren't included yet, add them
* If there are papers with interesting results for metrics that aren't included, add them
* If you know of important problems that humans can solve, and machine learning systems may or may not yet be able to, and they're missing from our taxonomy, you can propose them
* Look at our [Github issue list](https://github.com/AI-metrics/master_text) perhaps starting with those tagged as [good volunteer tasks](https://github.com/AI-metrics/master_text/issues?q=is%3Aissue+is%3Aopen+label%3A%22Good+volunteer+task%22).
* You can also add missing conferences / journals to to the venue-to-date mapping table (unhide the source code and search for `conference_dates`):
