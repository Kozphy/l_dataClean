# Dataclasses

Dataclasses are (sort of) a **mutable version** of `NamedTuple`.

```python
from dataclasses import dataclass
import datetime


@dataclass
class StockPrice2:
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """
        It's a class, so we can add methods too
        """
        return self.symbol in ["MSFT", "GOOG", "FB", "AMZN", "AAPL"]


price2 = StockPrice2("MSFT", datetime.date(2018, 12, 14), 106.03)

assert price2.symbol == "MSFT"
assert price2.closing_price == 106.03
assert price2.is_high_tech()

# stock split
price2.closing_price /= 2
assert price2.closing_price == 51.03
```

If we tried to modify a field of the **NamedTuple** version, we’d get an **AttributeError**.

This also leaves us `susceptible` to the kind of errors we were hoping to avoid by not using **dicts**:

```python
# It's a regular class, so add new fields however you like!
price2.cosing_price = 75
```
