import click
from chp3 import generator_iter
from chp4 import basic_index_slice


@click.command()
def cli():
    Exec_chp()


def Exec_chp3():
    # generator_iter.create_Iterator()
    # generator_iter.create_Generator()
    generator_iter.expression_Generator()
    generator_iter.p_itertools()


def Exec_chp4():
    # basic_index_slice.index_nparray()
    # basic_index_slice.assign_nparray()
    # basic_index_slice.bool_indexing()
    # basic_index_slice.fancy_indexing()
    # basic_index_slice.transpose_array_swap_axes()
    # basic_index_slice.array_oriented()
    # basic_index_slice.expression_condition_logic()
    basic_index_slice.math_statistical_method()


def Exec_chp():
    # Exec_chp3()
    Exec_chp4()


if __name__ == "__main__":
    cli()
