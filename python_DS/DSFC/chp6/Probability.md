# Probability

## intro

You should think of probability as a way of **quantifying the uncertainty associated with events chosen from some universe of events**.

Thinking of rolling die. The **universe consists of all possible outcomes**. And any **subset of these outcomes** is an **event**; for ex, "the die rolls a 1" or "the die rolls an even number".

Notationally, we write **P(E)** to mean **“the probability of the event E.”**

## Dependence and Independence

### Dependence

Roughly speaking, we say that **two events E and F are dependent if knowing something about whether E happens gives us information about whether F happens** (and vice versa).

for ex, Knowing whether the first flip is heads certainly gives us information about whether both flips are tails.

### Independence

For instance, if we flip a fair coin twice, knowing whether the **first flip is heads gives us no information about whether the second flip is heads**. These events are **independent**.

`Mathematically`, we say that **two events E and F are independent** if the probability that they both happen is the **product of the probabilities that each one happens**:

$$
P(E,F) = P(E)P(F)
$$

which can say the probability of “first flip heads” is 1/2, and the probability of “both flips tails” is 1/4, but the probability of “first flip heads and both flips tails” is 0.

## Conditional Probability

When two events **E and F are independent**, then by definition we have:
$$
P(E,F) = P(E)P(F)
$$

If they are **not necessarily independent** (and if the probability of F is not zero), then we define the probability of E “conditional on F” as:
$$
P(E|F) = P(E,F)/P(F)
$$

According to above, You should think of this as the probability that **E happens, given that we know that F happens**.

$$
P(E,F) = P(E|F)P(F)
$$

We can rewrite as:

$$
P(E,F) = P(E|F)P(F)
$$

When **E and F are independent**, you can check that this gives:

$$
P(E|F) = P(E)
$$
