import pandas as pd
from pandas.errors import ParserError
from src.utils import map_plugins


class OperationError(Exception):
    pass


class Operation:
    df = None

    def map_func(self, func_name):
        """Map a function"""
        try:
            return map_plugins()[func_name]
        except KeyError:
            raise OperationError(f"Function not supported - {func_name}")

    def read_csv(self, filepath):
        """Read a csv file"""
        try:
            self.df = pd.read_csv(filepath)
            return self
        except FileNotFoundError as e:
            raise OperationError(f"File not found - {filepath}") from e
        except ParserError as e:
            raise OperationError(f"Fails to parse file - {e}") from e

    def group_by(self, group_by_col):
        """Group by a data frame"""
        try:
            self.df = self.df.groupby(group_by_col)
            return self
        except KeyError as e:
            raise OperationError(f"Column not found: {group_by_col}") from e

    def select_column(self, apply_col):
        """Select a column from a grouped data frame"""
        try:
            self.df = self.df[apply_col]
            return self
        except KeyError as e:
            raise OperationError(f"Column not found: {apply_col}") from e

    def apply(self, func_name):
        """Apply a function"""
        try:
            func = self.map_func(func_name)
            self.df = self.df.apply(func)
            return self
        except TypeError as e:
            raise OperationError(e) from e
