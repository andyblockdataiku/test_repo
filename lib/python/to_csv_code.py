import dataiku
import pandas as pd

def save_to_csv(input_dataset: pd.DataFrame, output_path: str):
    input_dataset.to_csv(output_path)