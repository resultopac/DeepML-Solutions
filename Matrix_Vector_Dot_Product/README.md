# Matrix-Vector Dot Product

**Difficulty**: Easy | **Category**: Linear Algebra

## Description

Matrix-Vector Dot Product
Easy
Linear Algebra
Breakdown

Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

Example:
Input:
a = [[1, 2], [2, 4]], b = [1, 2]
Output:
[5, 10]
Reasoning:

Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10

Learn About topic
Row by row dot product

Output entry i is matrix row i dotted with the whole vector, so columns must match vector length.

1
2
3
4
5
6
·
−
2
+
−
1
+
−
-1
+
=
1
7

row 0: 1×2 + 2×1 + 3×(-1) = 1

drop an entry to break the shapes
Contributors:

Moe Chabot

Contribute
Request Edit