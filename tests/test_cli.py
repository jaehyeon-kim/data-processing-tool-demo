from cli import search
from click.testing import CliRunner
import cli


def test_search():
    runner = CliRunner()
    results = runner.invoke(cli.search, ["--path", ".", "--ftype", "md"])
    print(results.output)
    assert results.exit_code == 0
    assert ".md" in results.output
