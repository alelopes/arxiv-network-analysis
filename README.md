# Arxiv Collaborators Network Analysis

## Introduction

We constructed a network scrapping Arxiv authors from the beginning of Arxiv until October 2020.

We performed some analysis on the network, such as clustering coefficient, average degree, and evaluated the fit of our model to a power-law degree distribution.

We are making available right now just the [main_page.py](https://github.com/alelopes/arxiv-network-analysis/blob/main/main_page.py) code, that runs a flask server of the project and the network data itself separated into several different files (by date).

The main_page contains a page that you can see what is the shortest path between two researchers that published in Arxiv in all areas until October 2020. It is also possible to filter the information.

You can check a page example at [arxivcolab.info/](http://arxivcolab.info/)

## Motivation

The main motivation was to update the Arxiv network and made it available for the network science community. We also wanted to analyze a common problem in Google Scholar, that is the usage by some researchers of other people's work with the same name as theirs. So, they can boost their metrics, such as h-index, and citation numbers. 

We analyzed some of the nodes with the largest degree, as we hypothesized that a high degree happens if a name was shared by many people because it is not common for a researcher to collaborate with large quantities of authors (for instance, +1000 collaborators). In our analysis, we found that most of the high degree author names were common combinations of first and last names, and most of the first five authors found in Google Scholar for each high degree author name contained intersection in the author's papers list and they were also publishing papers in different fields, such as social science, physics, and electronics. This indicates that these people were benefiting from other people's work to boost their metrics.

## Fraud Analysis

It would be Frivolous for us to claim that these suspects were frauds, therefore we are not making available any example with the author's name. The code for this kind of analysis was excluded from the Jupyter Notebook, to preserve the authors. For instance, although it is unlikely for a person to publish in different fields, such as social science, physics, and electronics, it is possible.

## Codes

We are making available two items:

* Flask Web Server to calculate Shortest Path and Closest Name in Arxiv
* Notebook with some network's metrics

## Citing

If you want to use this work for publication purposes (use network or metrics for comparison), let us know by creating an issue in this repo. If there are interested people, we can create a report in Arxiv so you can cite it.
