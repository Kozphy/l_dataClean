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
