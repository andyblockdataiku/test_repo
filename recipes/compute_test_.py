# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
iris_dataset = dataiku.Dataset("iris_dataset")
iris_dataset_df = iris_dataset.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test__df = iris_dataset_df # For this sample code, simply copy input to output


# Write recipe outputs
test_ = dataiku.Dataset("test_")
test_.write_with_schema(test__df)
