import pandas as pd


class DataFrameTransformer:
    def __init__(self, dataframe: pd.DataFrame):
        self.__dataframe = dataframe

    def filter_by_predicate(self, column: str, predicate: str, value: float):
        if predicate == "gt":
            self.__dataframe = self.__dataframe[self.__dataframe[column] > value]
        elif predicate == "lt":
            self.__dataframe = self.__dataframe[self.__dataframe[column] < value]
        elif predicate == "eq":
            self.__dataframe = self.__dataframe[self.__dataframe[column] == value]
        else:
            raise ValueError(f"Unsupported predicate: {predicate}")
        return self

    def select_columns(self, columns: list):
        self.__dataframe = self.__dataframe[columns]
        return self

    def add_computed_column(self, new_column: str, base_column: str, func: str):
        if func == "square":
            self.__dataframe[new_column] = self.__dataframe[base_column] ** 2
        elif func == "double":
            self.__dataframe[new_column] = self.__dataframe[base_column] * 2
        else:
            raise ValueError(f"Unsupported function: {func}")
        return self

    def get_dataframe(self):
        return self.__dataframe
