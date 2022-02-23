# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.datasets import load_iris

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
iris = load_iris()

iris_dataset_python_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], 
                                      columns= iris['feature_names'] + ['target'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
iris_dataset_python = dataiku.Dataset("iris_dataset_python")
iris_dataset_python.write_with_schema(iris_dataset_python_df)