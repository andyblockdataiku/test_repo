# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

iris_dataset_python_df = ... # Compute a Pandas dataframe to write into iris_dataset_python


# Write recipe outputs
iris_dataset_python = dataiku.Dataset("iris_dataset_python")
iris_dataset_python.write_with_schema(iris_dataset_python_df)
