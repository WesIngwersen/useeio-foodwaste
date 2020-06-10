# DataFrames_existing.py (ExistingDataLabResults)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Basic program to view lab results from .csv file.

DataFrames = data in a frame/table or tabular data.
"""

first_run = false
# NOTE: These lines need to be run on the first time only:
if first_run
    using Pkg
    Pkg.add("DataFrames")
    Pkg.add("CSV")
end

using DataFrames
using CSV

# The big csv takes a while to load/print, so I created one with ~10 lines
input = ".\\TestFolderJulia\\sampledata.csv"
input_smaller = ".\\TestFolderJulia\\sampledata_smaller.csv"

df = DataFrame(CSV.File(input_smaller))

# describe(df)
print(df)

# For all users
# New variable: JULIA_HOME C:\Users\Daniel L. Young PhD\AppData\Local\Programs\Julia\Julia-1.4.1\bin
# Edit existing path: Add new path entry: %JULIA_HOME%
