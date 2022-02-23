# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from to_csv_code import save_to_csv

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
iris_dataset_python = dataiku.Dataset("iris_dataset_python")
iris_dataset_python_df = iris_dataset_python.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
iris_dataset_prepared_df = iris_dataset_python_df[iris_dataset_python_df['sepal width (cm)'] >= 3.0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
iris_dataset_prepared = dataiku.Dataset("iris_dataset_prepared")
iris_dataset_prepared.write_with_schema(iris_dataset_prepared_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
to_csv(iris_dataset_prepared_df, '~/Downloads')