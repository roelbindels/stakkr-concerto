import click
import os

from clint.textui import colored, puts


@click.command(help='concerto', name='concerto')
@click.pass_context
def concerto(ctx):
    print("here")