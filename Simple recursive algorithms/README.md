# Simple recursive algorithms

A simple recursive algorithm:
- Solves the base cases directly
- Recurs with a simpler subproblem
- Does some extra work to convert the solution to the simpler subproblem into a solution to the given problem
- I call these “simple” because several of the other
algorithm types are inherently recursive

# Example recursive algorithms

To count the number of elements in a list:
- If the list is empty, return zero; otherwise,
- Step past the first element, and count the remaining elements
in the list
- Add one to the result
- To test if a value occurs in a list:
- If the list is empty, return false; otherwise,
- If the first thing in the list is the given value, return true;
otherwise
- Step past the first element, and test whether the value occurs in the remainder of the list