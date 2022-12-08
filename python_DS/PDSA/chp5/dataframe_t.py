import pandas as pd
import numpy as np
import pandas_datareader as pdr


data = {
    "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
    "year": [2000, 2001, 2002, 2001, 2002, 2003],
    "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
}


def create_dframe2():
    frame2 = pd.DataFrame(
        data,
        columns=["year", "state", "pop", "debt"],
        index=["one", "two", "three", "four", "five", "six"],
    )
    print(frame2)
    print(frame2.loc["three"])
    frame2["debt"] = 16.5
    print(frame2)
    frame2["debt"] = np.arange(6)
    print(frame2)
    val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])
    frame2["debt"] = val
    print(frame2)


frame3_g = None


def nest_dict_create_dataframe():
    pop = {
        "Nevada": {2001: 2.4, 2002: 2.9},
        "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
    }
    frame3 = pd.DataFrame(pop)
    global frame3_g
    frame3_g = frame3
    print("create with nest dict")
    print(frame3)
    print(frame3.T)


# def dict_series_dataframe():
# deprecated
# pdata = {
#     "Ohio": frame3_g["Ohio"][:-1],
#     "Nevada": frame3_g["Nevada"][:2],
# }
# print("create with dict series")
# pda = pd.DataFrame(pdata)
# print(pda)
# print(pda.T)


def dataframe_index_column():
    print("The name about index and column")
    frame3_g.index.name = "year"
    frame3_g.columns.name = "state"
    print(frame3_g)


def dataframe_index_object():
    print()
    print("dataframe index object")
    obj = pd.Series(range(3), index=["a", "b", "c"])
    index = obj.index
    print(index)
    print(index[1:])

    labels = pd.Index(np.arange(3))
    obj2 = pd.Series([1.5, -2.5, 0], index=labels)
    # print(obj2.index is labels)
    print("Ohio" in frame3_g.columns)
    print(2003 in frame3_g.index)


def dataframe_reindex():
    print("default data")
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
    print(obj)

    print("\nreindex a, b, c, d, e to obj")
    obj2 = obj.reindex(["a", "b", "c", "d", "e"])
    print(obj2)

    print("\nredinex 0, 2, 4 to obj2")
    obj3 = pd.Series(["blue", "purple", "yello"], index=[0, 2, 4])
    print(obj3)
    print("\nreindex ffill")
    obj4 = obj3.reindex(range(6), method="ffill")
    print(obj4)

    frame = pd.DataFrame(
        np.arange(9).reshape((3, 3)),
        index=["a", "c", "d"],
        columns=["Ohio", "Texas", "California"],
    )
    print(f"\nframe: \n{frame}")


def dataframe_indexing_selection_filtering():
    print("indexing, selection, and filtering")
    # obj = pd.Series(np.arange(4.0), index=["a", "b", "c", "d"])
    # print(f"Series default data:\n {obj}\n")
    # print(f"obj['b']:\n {obj['b']}\n")
    # print(f"obj[1]:\n {obj[1]}\n")
    # print(f"obj[2:4]:\n {obj[2:4]}\n")
    # print(f"obj[['b', 'a', 'd']]:\n {obj[['b', 'a', 'd']]}\n")
    # print(f"obj[[1,3]]:\n {obj[[1,3]]}\n")
    # print(f"obj[obj < 2]:\n {obj[obj < 2]}\n")
    # print(f"obj['b':'c']:\n {obj['b':'c']}")
    data = pd.DataFrame(
        np.arange(16).reshape((4, 4)),
        index=["Ohio", "Colorado", "Utah", "New York"],
        columns=["one", "two", "three", "four"],
    )
    print(f"\ndata:\n {data}")
    # print(f"\ndata['two']:\n {data['two']}")
    # print(f"\ndata[['three', 'one']]:\n {data[['three', 'one']]}")
    print(
        f"\ndata.loc['Colorado', ['two', 'three']:\n {data.loc['Colorado', ['two', 'three']]}"
    )
    print(f"\ndata.iloc[2, [3, 0, 1]]:\n{data.iloc[2, [3, 0, 1]]}")
    print(f"\ndata.loc[:'Utah', 'two']:\n {data.loc[:'Utah', 'two']}")
    print(f"\ndata.iloc[:, :3][data.three > 5]:\n {data.iloc[:,:3][data.three > 5]}")


def indexing_integer():
    print("indexing integer")
    ser = pd.Series(np.arange(3.0))
    print(f"\nser:\n {ser}")

    print(f"\nser[:1]:\n {ser[:1]}")
    print(f"\nser.loc[:1]:\n {ser.loc[:1]}")
    print(f"\nser.iloc[:1]:\n {ser.iloc[:1]}")


def add_arth_together():
    print("Arthmetic and Data Alignment")
    s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])

    print(f"\ns1:\n {s1}")
    print(f"\ns2:\n {s2}")
    print(f"\ns1 + s2:\n {s1 + s2}")


def arthmetic_with_fill_values():
    print("arthmetic_with_fill_values")
    df1 = pd.DataFrame(np.arange(12.0).reshape((3, 4)), columns=list("abcd"))
    print(f"\ndf1:\n {df1}")
    df2 = pd.DataFrame(np.arange(20.0).reshape(4, 5), columns=list("abcde"))
    print(f"\ndf2:\n {df2}")
    print(f"\ndf1 + df2:\n{df1 + df2}")
    print(f"\nfill_value:\n {df1.add(df2, fill_value=0)}")

    print(
        f"\ndf1.reindex(columns=df2.columns, fill_value=0):\n {df1.reindex(columns=df2.columns, fill_value=0)}"
    )


def operation_between_df_se():
    arr = np.arange(12.0).reshape((3, 4))
    # print(f"arr: {arr}")
    # print(f"arr[0]: {arr[0]}")
    # print(f"arr - arr[0]: {arr - arr[0]}")

    frame = pd.DataFrame(
        np.arange(12.0).reshape((4, 3)),
        columns=list("bde"),
        index=["Utah", "Ohio", "Texas", "Oregon"],
    )
    print(f"\nframe:\n {frame}")
    series = frame.iloc[0]
    print(f"\nseries:\n {series}")

    print(f"\nframe - series:\n {frame - series}")

    series2 = pd.Series(range(3), index=["b", "e", "f"])
    print(f"\nframe + series2:\n {frame + series2}")

    series3 = frame["d"]
    print(f"\nseries3:\n {series3}")
    print(f"\nframe.sub(series3, axis='index'):\n {frame.sub(series3, axis='index')}")


def fa(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])


def func_app_mapping():
    frame = pd.DataFrame(
        np.random.randn(4, 3),
        columns=list("bde"),
        index=["Utah", " Ohio", "Texas", "Oregon"],
    )
    print(f"\nframe:\n {frame}")
    print(f"\nnp.abs(frame):\n {np.abs(frame)}")

    f = lambda x: x.max() - x.min()
    print(f"\nframe.apply(f):\n {frame.apply(f)}")

    print(f"\nframe.apply(f, axis='columns'):\n {frame.apply(f, axis='columns')}")

    print(f"\nframe.apply(fa):\n {frame.apply(fa)}")

    format = lambda x: "%.2f" % x
    print(f"\nframe.applymap(format):\n {frame.applymap(format)}")

    print(f"\nframe['e'].map(format):\n {frame['e'].map(format)}")


def sort_and_rank():
    obj = pd.Series(range(4), index=["d", "a", "b", "c"])
    # print(f"\nobj:\n {obj}")
    # print(f"\nobj.sort_index():\n {obj.sort_index()}")

    frame = pd.DataFrame(
        np.arange(8).reshape((2, 4)),
        index=["three", "one"],
        columns=["d", "a", "b", "c"],
    )

    # print(f"\nframe:\n {frame}")
    # print(f"\nframe.sort_index():\n {frame.sort_index()}")
    # print(f"\nframe.sort_index(axis=1):\n {frame.sort_index(axis=1)}")

    # print(
    #     f"\nframe.sort_index(axis=1, ascending=False):\n {frame.sort_index(axis=1, ascending=False)}"
    # )

    # obj2 = pd.Series([4, 7, -3, 2])
    # print(f"\nobj2.sort_values():\n {obj2.sort_values()}")
    # obj3 = pd.Series([4, np.nan, 7, np.nan, -3, 2])
    # print(f"\nobj3.sort_values():\n {obj3.sort_values()}")

    frame = pd.DataFrame(
        {
            "b": [4, 7, -3, 2],
            "a": [0, 1, 0, 1],
        }
    )
    # print(f"\nframe:\n {frame}")
    # print(f"\nframe.sort_values(by='b'):\n {frame.sort_values(by='b')}")
    # print(f"\nframe.sort_values(by=['a','b']):\n {frame.sort_values(by=['a','b'])}")

    obj2 = pd.DataFrame([1, 2, 3, 4, 5, 3, 6, 7, 7, 9], columns=["Sample"]).sort_values(
        by="Sample"
    )
    obj2["avg_rank"] = obj2["Sample"].rank()
    obj2["first_rank"] = obj2["Sample"].rank(method="first")
    print(f"\nobj2:\n {obj2}")
    # print(f"\nobj2.rank():\n {obj2.rank()}")
    # print(f"\nobj2.rank(method='first'):\n {obj2.rank(method='first')}")


def axis_indexs_with_duplicate_labels():
    print("axis_indexs_with_duplicate_labels")
    obj = pd.Series(range(5), index=["a", "a", "b", "b", "c"])
    print(f"\nobj:\n {obj}")
    print(obj.index.is_unique)
    print(f"\nobj['a']:\n {obj['a']}")
    print(f"\nobj['c']:\n {obj['c']}")

    df = pd.DataFrame(np.random.randn(4, 3), index=["a", "a", "b", "b"])
    print(f"\ndf:\n {df}")
    print(f"\ndf.loc['b']:\n {df.loc['b']}")


def summerize_compute_sta():
    df = pd.DataFrame(
        [[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
        index=["a", "b", "c", "d"],
        columns=["one", "two"],
    )
    print(f"\ndf:\n {df}")
    print(f"\ndf.sum:\n {df.sum()}")
    print(f"\ndf.sum(axis='columns'):\n {df.sum(axis='columns')}")
    print(
        f"\ndf.mean(axis='columns', skipna=False):\n {df.mean(axis='columns', skipna=False)}"
    )

    print(f"\ndf.idxmax():\n {df.idxmax()}")
    print(f"\ndf.idxmin():\n {df.idxmin()}")
    print(f"\ndf.describe():\n {df.describe()}")

    obj = pd.Series(["a", "a", "b", "c"] * 4)
    print(f"\nobj.describe():\n {obj.describe()}")


def correlation_corvariance():
    print("correlation_corvariance")
    all_data = {
        ticker: pdr.data.get_data_yahoo(ticker)
        for ticker in ["AAPL", "IBM", "MSFT", "GOOG"]
    }
    # print(f"\nall_data:\n {all_data}")

    price = pd.DataFrame(
        {ticker: data["Adj Close"] for ticker, data in all_data.items()}
    )

    # print(f"\nprice:\n {price}")

    volume = pd.DataFrame({ticker: data["Volume"] for ticker, data in all_data.items()})
    # print(f"\nvolume:\n {volume}")

    returns = price.pct_change()
    print_content("returns", returns)
    # print(returns.tail())

    print_content(
        "returns['MSFT'].corr(returns['IBM'])", returns["MSFT"].corr(returns["IBM"])
    )

    # print()
    print_content(
        "returns['MSFT'].cov(returns['IBM'])", returns["MSFT"].cov(returns["IBM"])
    )

    print_content("returns.corr()", returns.corr())

    print_content("return.cov()", returns.cov())

    print_content("returns.corrwith(returns.IBM)", returns.corrwith(returns.IBM))


def print_content(name: str, content):
    print(f"\n{name}:\n {content}")
