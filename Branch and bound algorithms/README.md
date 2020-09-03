# Branch and bound algorithms

Branch and bound algorithms are generally used for
optimization problems
- As the algorithm progresses, a tree of subproblems is formed
- The original problem is considered the “root problem”
- A method is used to construct an upper and lower bound for a
given problem
- At each node, apply the bounding methods
    - If the bounds match, it is deemed a feasible solution to that particular
subproblem
    - If bounds do not match, partition the problem represented by that node, and make the two subproblems into children nodes
- Continue, using the best known feasible solution to trim
sections of the tree, until all nodes have been solved or
trimmed

Example branch and bound algorithm

Traveling salesman problem: A salesman has to visit
each of n cities (at least) once each, and wants to
minimize total distance traveled
- Consider the root problem to be the problem of finding the
shortest route through a set of cities visiting each city once
- Split the node into two child problems:
    - Shortest route visiting city A first
    - Shortest route not visiting city A first
- Continue subdividing similarly as the tree grows