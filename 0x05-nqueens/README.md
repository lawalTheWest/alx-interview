# N Queens

---

The N Queens puzzle is a classic problem in `computer science and mathematics` that involves `placing N non-attacking queens on an N×N chessboard.`

This project aims to implement a solution to the N Queens problem using a backtracking algorithm in Python.


## Concepts

---

To successfully solve the N Queens problem, we'll need to understand the following key concepts:

- **Backtracking Algorithms**: A technique used to explore all potential solutions to a problem and backtrack when a solution path is not viable.
- **Recursion**: Recursive functions will be used to implement the backtracking algorithm.
- **List Manipulations in Python**: You will need to create and manipulate lists to store the positions of queens on the board.
- **Python Command Line Arguments**: Handling command-line arguments using the `sys` module

# The improved code

---

The code was improved by The Use of the following:

- **Use Sets for Faster Lookups:** Instead of iterating through the list of placed queens to check for conflicts, we can use sets to track the columns and diagonals that are already attacked by queens. This reduces the time complexity for checking conflicts from O(N) to O(1).

- **Use Recursive Backtracking:** Using recursion for the backtracking algorithm can make the code cleaner and more efficient by reducing the need to manage state manually.

- **Early Termination:** By placing queens row by row and using recursive backtracking, we can immediately backtrack when we find a conflict without checking the rest of the row..
