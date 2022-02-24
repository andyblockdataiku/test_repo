# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
iris_dataset_prepared = dataiku.Dataset("iris_dataset_prepared")
iris_dataset_prepared_df = iris_dataset_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
iris_dataset_prepared_df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
X, y = train_test_split(iris_dataset_prepared_df, test_size=0.2)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
y.drop('target', axis=1, inplace=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
X.reset_index(inplace=True, drop=True)
y.reset_index(inplace=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
X.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
y.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
iris_dataset_train = dataiku.Dataset("iris_dataset_train")
iris_dataset_train.write_with_schema(X)

iris_dataset_test = dataiku.Dataset("iris_dataset_test")
iris_dataset_test.write_with_schema(y)