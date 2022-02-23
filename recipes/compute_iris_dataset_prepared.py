# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
iris_dataset_python = dataiku.Dataset("iris_dataset_python")
iris_dataset_python_df = iris_dataset_python.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

iris_dataset_prepared_df = iris_dataset_python_df # For this sample code, simply copy input to output


# Write recipe outputs
iris_dataset_prepared = dataiku.Dataset("iris_dataset_prepared")
iris_dataset_prepared.write_with_schema(iris_dataset_prepared_df)
