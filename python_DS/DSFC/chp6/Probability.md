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
$$
P(HT) = \frac{1}{2} \\
P(TT) = \frac{1}{4} \\
P(H) \ and \ P(TT) = 0
$$

## Conditional Probability

[intro Conditional Probability](https://www.youtube.com/watch?v=ibINrxJLvlM&ab_channel=Dr.TreforBazett)
[two conditional probability example](https://www.youtube.com/watch?v=OYT0AcuLXu8&ab_channel=Dr.TreforBazett)

### independent

When two events **E and F are independent**, then by definition we have:
$$
P(E,F) = P(E)P(F)
$$

which you can check that this gives:

$$
P(E|F) = P(E)
$$

which is the mathematical way of expressing that **knowing F occurred gives us no additional information about whether E occurred**.

### not independent

If they are **not necessarily independent** (and if the probability of F is not zero), then we define the probability of E “conditional on F” as:
$$
P(E|F) = P(E,F)/P(F)
$$

According to above, You should think of this as the probability that **E happens, given that we know that F happens**.

$$
P(E,F) = P(E|F)/P(F)
$$

We can rewrite as:

$$
P(E, F)= P(E|F)P(F)
$$

### Example

Family have two (unknown) children. we assume

- Each child have **same chance** to be boy or girl.
- The gender of the **second child is independent of the gender of the first child**.

Then the event **“no girls” has probability 1/4, the event “one girl, one boy” has probability 1/2, and the event “two girls” has probability 1/4**.

$$
P(BB) = \frac{1}{4} \\
\\
P(GB) + P(BG) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}  \\
\\
P(GG) = \frac{1}{4} \\
$$

Now we can ask what is the probability of the event **“both children are girls” (B) conditional on the event “the older child is a girl” (G)**?

$$
P(B|G) = P(B,G)/P(G) = P(B)/P(G) = \frac{1}{2} \\
P(GG) / (P(BG) + P(GG)) = \frac{0.25}{0.5} = \frac{1}{2}
$$

We could also ask about the probability of the event **“both children are girls” (B) on the event** `and` **“at least one of the children is a girl” (L)**.

$$
P(B|L) = P(B,L)/P(L) = P(B)/P(L) = \frac{1}{3}\\
P(GG) / (1-P(BB)) = \frac{0.25}{0.75} = \frac{1}{3}
$$
