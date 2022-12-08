import click
from chp3 import generator_iter
from chp4 import basic_index_slice
from chp5 import dataframe_t


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
    # basic_index_slice.math_statistical_method()
    basic_index_slice.random_walk()
    basic_index_slice.simulating_random_work()


def Exec_chp5():
    # dataframe_t.create_dframe2()
    # dataframe_t.nest_dict_create_dataframe()
    # dataframe_t.dict_series_dataframe()
    # dataframe_t.dataframe_index_column()
    # dataframe_t.dataframe_index_object()
    # dataframe_t.dataframe_reindex()
    # dataframe_t.dataframe_indexing_selection_filtering()
    # dataframe_t.indexing_integer()
    # dataframe_t.add_arth_together()
    # dataframe_t.arthmetic_with_fill_values()
    # dataframe_t.operation_between_df_se()
    # dataframe_t.func_app_mapping()
    # dataframe_t.sort_and_rank()
    # dataframe_t.axis_indexs_with_duplicate_labels()
    # dataframe_t.summerize_compute_sta()
    dataframe_t.correlation_corvariance()


def Exec_chp():
    # Exec_chp3()
    # Exec_chp4()
    Exec_chp5()


if __name__ == "__main__":
    cli()
