# Using NamedTuples

One common way of representing data is using **dicts**:

```python
import datetime
stock_price = {'closing_price': 102.06,
 'date': datetime.date(2014, 8, 29),
 'symbol': 'AAPL'}
```

There are several reasons why this is less than ideal, however. This is a slightly inefficient representation (a dict involves some overhead), so that if you have a lot of stock prices they’ll **take up more memory** than they have to. For the most part, this is a minor consideration.

A larger issue is that **accessing things by dict key is error-prone**. The following code will **run without error and just do the wrong thing**:

```python
# oops, typo
stock_price['cosing_price'] = 103.06
```

Finally, while we can type-annotate uniform dictionaries:

```python
prices: Dict[datetime.date, float]= {}
```

You’ll notice that we still haven’t solved the type annotation issue. We do that by using the typed variant, **NamedTuple**:

```python
import datetime
from typing import Dict
from collections import namedtuple

class StockPrice(NamedTuple):
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """
        It's a class, so we can add methods too
        """
        return self.symbol in ["MSFT", "GOOG", "FB", "AMZN", "AAPL"]


price = StockPrice("MSFT", datetime.date(2018, 12, 14), 106.03)
```
