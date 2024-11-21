import pandas as pd
from transformations import DataFrameTransformer


def apply_transformations(dataframe: pd.DataFrame, transformations: list):
    transformer = DataFrameTransformer(dataframe)
    for transformation in transformations:
        action = transformation["action"]
        params = transformation["parameters"]

        if action == "filter_by_predicate":
            transformer.filter_by_predicate(**params)
        elif action == "select_columns":
            transformer.select_columns(**params)
        elif action == "add_computed_column":
            transformer.add_computed_column(**params)
        else:
            raise ValueError(f"Unsupported action: {action}")

    return transformer.get_dataframe()
