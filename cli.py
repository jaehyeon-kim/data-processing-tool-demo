#!/usr/bin/env python
import click
import glob
import src


@click.version_option(src.__version__)
@click.group()
def cli():
    """Data Processing Tool"""


@click.command("search")
@click.option(
    "--path",
    prompt="Path to search for csv files",
    help="This is the path to search for files: /tmp",
)
@click.option("--ftype", prompt="Pass in the type of file", help="Pass in the file type: e.g csv")
def search(path, ftype):
    """This is a tool that search for files given path and file type"""
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found Matches:", fg="red"))
    for result in results:
        click.echo(click.style(f"{result}", bg="blue", fg="white"))


if __name__ == "__main__":
    cli()
