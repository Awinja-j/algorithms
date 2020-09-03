# Backtracking algorithms

Backtracking algorithms are based on a depth-first
recursive search
- A backtracking algorithm:
    - Tests to see if a solution has been found, and if so, returns it; otherwise
    - For each choice that can be made at this point,
        - Make that choice
        - Recur
        - If the recursion returns a solution, return it
    - If no choices remain, return failure


## Example backtracking algorithm


To color a map with no more than four colors:
- color(Country n):
    - If all countries have been colored (n > number of countries) return success; otherwise,
    - For each color c of four colors,
        - If country n is not adjacent to a country that has been colored c
            - Color country n with color c
            - recursively color country n+1
            - If successful, return success
    - If loop exits, return failure