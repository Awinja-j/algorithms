# Divide and Conquer

A divide and conquer algorithm consists of two parts:
- Divide the problem into smaller subproblems of the same
type, and solve these subproblems recursively
- Combine the solutions to the subproblems into a solution to the original problem

Traditionally, an algorithm is only called “divide and
conquer” if it contains at least two recursive calls

### Examples

Quicksort:
- Partition the array into two parts (smaller numbers in one
part, larger numbers in the other part)
- Quicksort each of the parts
- No additional work is required to combine the two sorted
parts

Mergesort:
- Cut the array in half, and mergesort each half
- Combine the two sorted arrays into a single sorted array by
merging them

Binary tree lookup

Here’s how to look up something in a sorted binary tree:
- Compare the key to the value in the root

    - If the two values are equal, report success
    - If the key is less, search the left subtree
    - If the key is greater, search the right subtree
    
This is not a divide and conquer algorithm because,
although there are two recursive calls, only one is used
at each level of the recursion

Fibonacci numbers

To find the nth Fibonacci number:

    - If n is zero or one, return one; otherwise,
    - Compute fibonacci(n-1) and fibonacci(n-2)
    - Return the sum of these two numbers

This is an expensive algorithm

    - It requires O(fibonacci(n)) time
    - This is equivalent to exponential time, that is, O(2n)