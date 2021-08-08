#!/usr/bin/env python
import click
import glob

from src import __version__, ops, utils


@click.version_option(__version__)
@click.group()
def cli():
    """Data Processing Tool"""


@cli.command("process")
@click.option("--filepath", prompt="Path to a csv file", help="Path to a csv file")
@click.option("--group_by_col", prompt="Column name to group", help="Column name to group")
@click.option(
    "--apply_col", prompt="Column name to apply a function", help="Column name to apply a function"
)
@click.option("--func_name", prompt="Function name", help="Function name")
def process(filepath, group_by_col, apply_col, func_name):
    click.echo(
        f"Processing csv file: {filepath}, group by {group_by_col}, apply on {apply_col}, function {func_name}"
    )
    try:
        oper = (
            ops.Operation()
            .read_csv(filepath)
            .group_by(group_by_col)
            .select_column(apply_col)
            .apply(func_name)
        )
        click.echo(oper.df)
    except ops.OperationError as e:
        click.echo(click.style(e, fg="red"))


@cli.command("list")
def listfuncs():
    funcs = utils.get_func_names()
    names = ", ".join(funcs)
    click.echo(f"Available functions: {names}")


if __name__ == "__main__":
    cli()
