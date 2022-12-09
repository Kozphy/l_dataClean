import csv
import pandas as pd
from common import print_variance as pv
import sys
import numpy as np


def Reading_Writing_Data():
    df = pd.read_csv("examples/ex1.csv")
    pv.print_content("df", df)
    df_t = pd.read_table("examples/ex1.csv", sep=",")
    pv.print_content("df_t", df_t)
    pv.print_content(
        "pd.read_csv header=None", pd.read_csv("examples/ex2.csv", header=None)
    )
    pv.print_content(
        "pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message']",
        pd.read_csv("examples/ex2.csv", names=["a", "b", "c", "d", "message"]),
    )

    parsed = pd.read_csv("examples/csv_mindex.csv", index_col=["key1", "key2"])
    pv.print_content("parsed", parsed)

    pv.print_content("list(open('examples/ex3.txt'))", list(open("examples/ex3.txt")))

    result = pd.read_csv("examples/ex3.txt", sep="\s+")
    pv.print_content("result", result)

    pv.print_content(
        "pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3]",
        pd.read_csv("examples/ex4.csv", skiprows=[0, 2, 3]),
    )

    result = pd.read_csv("examples/ex5.csv")
    pv.print_content("result", result)
    pv.print_content("pd.isnull(result)", pd.isnull(result))

    result = pd.read_csv("examples/ex5.csv", na_values=["NULL"])
    pv.print_content("result na_value=['NULL']", result)

    sentinels = {"message": ["foo", "NA"], "something": ["two"]}
    result = pd.read_csv("examples/ex5.csv", na_values=sentinels)
    pv.print_content("result na_value=sentinels", result)


def Reading_Text_Files_in_Pieces():
    pd.options.display.max_rows = 10

    result = pd.read_csv("examples/ex6.csv")
    pv.print_content("result", result)
    print(result["key"].unique())

    chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)

    tot = pd.Series([], dtype="float64")

    for piece in chunker:
        tot = tot.add(piece["key"].value_counts(), fill_value=0)

    tot = tot.sort_values(ascending=False)
    pv.print_content("tot", tot)
    pv.print_content("tot[:10]", tot[:10])

    # pv.print_content("chunker.get_chunk()", chunker.get_chunk())


def Writing_data_to_text_format():
    data = pd.read_csv("examples/ex5.csv")

    pv.print_content("data", data)
    print("\ndata.to_csv(sys.stdout, sep='|':")
    data.to_csv(sys.stdout, sep="|")
    print("\nsys.stdout, na_rep='NULL':")
    data.to_csv(sys.stdout, na_rep="NULL")

    print("\nsys.stdout, index=False, header=False:")
    data.to_csv(sys.stdout, index=False, header=False)

    print("\nsys.stdout, index=False, columns=['a','b','c']:")
    data.to_csv(sys.stdout, index=False, columns=["a", "b", "c"])

    print("\nsys.stdout")
    dates = pd.date_range("1/1/2000", periods=7)
    ts = pd.Series(np.arange(7), index=dates)
    ts.to_csv(sys.stdout)


class my_dialect(csv.Dialect):
    lineterminator = "\n"
    delimiter = ";"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


def Working_with_other_delimited_formmat():
    # data = pd.read_csv("examples/ex7.csv")
    # print(data)

    # f = open("examples/ex7.csv")
    # reader = csv.reader(f)
    # for line in reader:
    #     print(line)

    with open("examples/ex7.csv") as f:
        lines = list(csv.reader(f))

    header, values = lines[0], lines[1:]

    data_dict = {h: v for h, v in zip(header, zip(*values))}
    # pv.print_content("data_dict", data_dict)

    f = open("examples/ex7.csv")
    reader = csv.reader(f, dialect=my_dialect)
    for row in reader:
        print(row)
    f.close()
