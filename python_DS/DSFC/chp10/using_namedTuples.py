import datetime
from collections import namedtuple
from typing import NamedTuple


def Exec_UsingNameTuple():
    stock_price = {
        "closing_price": 102.06,
        "date": datetime.date(2014, 8, 29),
        "symbol": "AAPL",
    }

    StockPrice = namedtuple("StockPrice", ["symbol", "date", "closing_price"])
    price = StockPrice("MSFT", datetime.date(2018, 12, 14), 106.03)

    print("StockPrice, price: ", StockPrice, price)


class StockPrice(NamedTuple):
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """
        It's a class, so we can add methods too
        """
        return self.symbol in ["MSFT", "GOOG", "FB", "AMZN", "AAPL"]
