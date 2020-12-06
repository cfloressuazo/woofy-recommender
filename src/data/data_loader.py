"""
Data loader module
"""
import json
import pandas as pd


class DataLoader:

    def __init__(self, filename: str, input_filepath: str, output_filepath: str):
        self.filename = filename
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

        raw_data = self._get_data()
        self._transform_data()
        self._load_data()

    def _get_data(self) -> list[dict]:
        """private method to get data from Dropbox"""
        j_content = []
        with open(self.input_filepath) as f:
            for line in f:
                j_content.append(json.loads(line))
        return j_content

    def _transform_data(self) -> pd.DataFrame:
        """private method to structure data from raw location"""
        pass

    def _load_data(self) -> None:
        """private method to load data into local filesystem"""
        pass
