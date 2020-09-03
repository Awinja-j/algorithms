Dynamic programming algorithms

A dynamic programming algorithm remembers past
results and uses them to find new results

Dynamic programming is generally used for
optimization problems

- Multiple solutions exist, need to find the “best” one

- Requires “optimal substructure” and “overlapping
subproblems”
    - Optimal substructure: Optimal solution contains optimal solutions to
    subproblems
    - Overlapping subproblems: Solutions to subproblems can be stored and
    reused in a bottom-up fashion

This differs from Divide and Conquer, where
subproblems generally need not overlap

### Fibonacci numbers again

To find the nth Fibonacci number:

- If n is zero or one, return one; otherwise,
- Compute, or look up in a table, fibonacci(n-1) and
fibonacci(n-2)
- Find the sum of these two numbers
- Store the result in a table and return it

Since finding the nth Fibonacci number involves finding
all smaller Fibonacci numbers, the second recursive call
has little work to do

The table may be preserved and used again later