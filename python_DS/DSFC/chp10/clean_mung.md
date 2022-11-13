# Cleaning and Munging

Real-world data is *dirty*.

We have to convert **strings** to **floats** or **ints** before we can use them.

We have to **check for**

- `missing values`
- `outliers`
- `bad data`.

If there’s **one bad row out of millions**, it’s probably okay to ignore it. But if **half your rows have bad data**, that’s something you need to fix.

A good next step is to check for outliers, using techniques from “Exploring Your Data” on page 123 or by ad hoc investigating.
