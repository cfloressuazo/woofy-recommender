"""
Data loader module
"""
import pandas as pd


class DataLoader:

    def __init__(self, filename: str, input_filepath: str, output_filepath: str):
        self.filename = filename
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

        self._get_data()
        self._transform_data()
        self._load_data()

    def _get_data(self) -> None:
        """private method to get data from Dropbox"""
        pass

    def _transform_data(self) -> pd.DataFrame:
        """private method to structure data from raw location"""
        pass

    def _load_data(self) -> None:
        """private method to load data into local filesystem"""
        pass
