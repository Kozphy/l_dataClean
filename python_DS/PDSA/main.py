import click
from chp3 import generator


@click.command()
def cli():
    Exec_chp()


def Exec_chp3():
    generator.P_Generator()


def Exec_chp():
    Exec_chp3()


if __name__ == "__main__":
    cli()
