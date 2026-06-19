# Mathdle Solver

A Python solver for [Mathdle](https://mathdle.app/) puzzles. Given a target number and a set of base numbers, it finds a sequence of `+`, `-`, `*`, `/` operations using all base numbers exactly once to reach the target.

## Usage

```
python mathdle_solver.py
Enter target number: 168
Enter base numbers (comma separated): 100,75,50,25,10,2
100 + 75 = 175
50 / 25 = 2
10 / 2 = 5
175 - 2 = 173
173 - 5 = 168
```

Commas with or without spaces are both fine.

## How it works

Uses recursive backtracking — at each step it picks a pair of remaining numbers, applies a valid operation, and replaces the pair with the result. Continues until one number remains and checks whether it matches the target.

Division is only allowed when the result is an integer (no fractions). Subtraction always produces a non-negative result.
