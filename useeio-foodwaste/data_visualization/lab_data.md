# Laboratory Results

This folder contains laboratory analysis performed by US EPA on microplastics to use in the useeio-foodwaste tool for combinatorial data analysis (CDA) which is the study of data sets where the order in which objects are arranged is important. CDA can be used either to determine how well a given combinatorial construct reflects the observed data, or to search for a suitable combinatorial construct that does fit the data.

Once all existing laboratory data and .csv files have been imported, develop useeio-foodwaste program to examine and plot data. This data will be used as part of the CDA data sets for comparison plotting with actual EPA/CESER/LRTD lab sampling and analysis data for final product report.

## Python Lang

The basic tool will be set up using a django/python web app with postgres database and the lab results stored in this folder from an existing data search using the food waste data search tool on EPA web server RTP RHEL (VM937).

sklearn.ensemble.RandomForestClassifier @ <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>

sklearn.datasets.make_classification @ <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html>
