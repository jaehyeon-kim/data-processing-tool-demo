from typing import List
import pytest
import pandas as pd
from src.ops import Operation, OperationError


def _get_sorted_data_frame(pdf: pd.DataFrame, columns_list: List[str] = None):
    if columns_list is None:
        columns_list = list(pdf.columns.values)
    return pdf.sort_values(columns_list).reset_index(drop=True)


def test_read_csv_success():
    lst = [
        ["piers", "smith", 10],
        ["kristen", "smith", 17],
        ["john", "lee", 3],
        ["sam", "eagle", 15],
        ["john", "eagle", 19],
    ]

    expected_df = pd.DataFrame(lst, columns=["first_name", "last_name", "count"])
    actual_df = Operation().read_csv("./ext/input.csv").df
    pd.testing.assert_frame_equal(
        _get_sorted_data_frame(actual_df, ["first_name", "last_name", "count"]),
        _get_sorted_data_frame(expected_df, ["first_name", "last_name", "count"]),
        check_like=True,
    )


def test_read_csv_invalid_path():
    with pytest.raises(OperationError, match=r"File not found.*"):
        Operation().read_csv("./ext/input.cs")


def test_read_csv_invalid_file():
    with pytest.raises(OperationError):
        Operation().read_csv("./ext/bad_input.csv")


# def test_search():
#     runner = CliRunner()
#     results = runner.invoke(cli.search, ["--path", ".", "--ftype", "md"])
#     assert results.exit_code == 0
#     assert ".md" in results.output
