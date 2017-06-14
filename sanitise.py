#!/usr/bin/env python

with open("AI-progress-metrics.html") as html_file:
    html = html_file.read()

html = html.replace("https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js",
                    "js/require-2.1.10.min.js")

html = html.replace("https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js",
                    "js/require-2.0.3.min.js")

html = html.replace("https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML",
                    "js/MathJax.js")

assert 'script src="http' not in html, "HTMLified Notebook appears to contain unhandled 3rd party JS, please fix sanitise.py"
assert 'src="http' not in html, "HTMLified Notebook appears to contain unhandled 3rd party embed, please fix sanitise.py"

with open("AI-progress-metrics.html", "w") as html_file:
    html_file.write(html)

print "Sanitised AI-progress-metrics.html, apprently successfully"
