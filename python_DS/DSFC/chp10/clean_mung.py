from dateutil.parser import parse
from .using_namedTuples import StockPrice
from typing import List, Optional
import re
import csv


def parse_row(row: List[str]) -> StockPrice:
    symbol, date, closing_price = row
    return StockPrice(
        symbol=symbol, date=parse(date).date(), closing_price=float(closing_price)
    )


# Now test our function
stock = parse_row(["MSFT", "2018-12-14", "106.03"])

print("parse_row:", stock)


def try_parse_row(row: List[str]) -> Optional[StockPrice]:
    symbol, date_, closing_price_ = row

    # Stock symbol should be all captial letters
    if not re.match(r"^[A-Z]+$", symbol):
        return None
    try:
        date = parse(date_).date()
    except ValueError:
        return None

    try:
        closing_price = float(closing_price_)
    except ValueError:
        return None

    return StockPrice(symbol, date, closing_price)


# Should return None for errors
print("try_parse_row", try_parse_row(["MSFT0", "2018-12-14", "106.03"]))
print("try_parse_row2", try_parse_row(["MSFT", "2018-12--15", "106.03"]))
print("try_parse_row3", try_parse_row(["MSFT", "2018-12-14", "x"]))

# But should return same as before if data is good
print("try_parse_row4", try_parse_row(["MSFT", "2018-12-14", "106.03"]))

data: List[StockPrice] = []

with open("comma_delimited_stock_prices.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        maybe_stock = try_parse_row(row)
        if maybe_stock is None:
            print(f"skipping invalid row: {row}")
        else:
            data.append(maybe_stock)
