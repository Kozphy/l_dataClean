import click
from chp1 import intro

from chp9 import clean_gov
from chp10 import (
    using_namedTuples,
    dataclasses,
    clean_mung,
    Exploring_one_dimensional_data,
)


@click.command()
def cli():
    Exec_chp()


def Exec_chp9():
    # using_namedTuples.Exec_UsingNameTuple()
    return


def Exec_chp10():
    clean_mung.clean_and_mung()
    Exploring_one_dimensional_data.plot_histogram()


def Exec_chp():
    # intro.Exec_find_key_connect()
    # intro.Exec_DataScientists_You_May_Know()
    # intro.Exec_data_scientists_who_like()
    # clean_gov.clean_national_library()
    # intro.Exec_salary_by_tenure()
    Exec_chp10()


if __name__ == "__main__":
    cli()
