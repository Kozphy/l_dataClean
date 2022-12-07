import pandas as pd
import numpy as np


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
