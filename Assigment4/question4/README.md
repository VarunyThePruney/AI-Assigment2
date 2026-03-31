# Cryptarithmetic CSP Solver

## Overview

This project implements the **Cryptarithmetic puzzle (TWO + TWO = FOUR)** using **Constraint Satisfaction Problem (CSP)** in Python.
Each letter represents a unique digit and the goal is to find digits that satisfy the equation.

## Problem

```
  TWO
+ TWO
------
 FOUR
```

Constraints:

* Each letter has a unique digit
* No leading zeros
* TWO + TWO = FOUR must be correct

## Algorithm

* Generate digit permutations
* Assign digits to letters
* Check constraints
* Print solution when equation is satisfied

## How to Run

```bash
python crypt.py
```

## Output

```
734 + 734 = 1468
```

