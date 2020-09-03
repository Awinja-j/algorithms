Greedy algorithms

An optimization problem is one in which you want to
find, not just a solution, but the best solution

A “greedy algorithm” sometimes works well for
optimization problems

A greedy algorithm works in phases: At each phase:
    - You take the best you can get right now, without regard for
    future consequences
    - You hope that by choosing a local optimum at each step, you
    will end up at a global optimum

Example: Counting money

Suppose you want to count out a certain amount of
money, using the fewest possible bills and coins

A greedy algorithm would do this would be:
At each step, take the largest possible bill or coin
that does not overshoot

- Example: To make $6.39, you can choose:
    - a $5 bill
    - a $1 bill, to make $6
    - a 25¢ coin, to make $6.25
    - A 10¢ coin, to make $6.35
    - four 1¢ coins, to make $6.39

For US money, the greedy algorithm always gives
the optimum solution


A failure of the greedy algorithm

In some (fictional) monetary system, “krons” come
in 1 kron, 7 kron, and 10 kron coins

Using a greedy algorithm to count out 15 krons,
you would get:

    - A 10 kron piece
    - Five 1 kron pieces, for a total of 15 krons
    - This requires six coins

A better solution would be to use two 7 kron pieces
and one 1 kron piece
    - This only requires three coins

The greedy algorithm results in a solution, but not
in an optimal solution