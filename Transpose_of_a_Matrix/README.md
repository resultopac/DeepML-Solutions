# Transpose of a Matrix

**Difficulty**: Easy | **Category**: Math

## Description

Transpose of a Matrix
Easy
Linear Algebra
Breakdown

Write a Python function that computes the transpose of a given 2D matrix. The transpose of a matrix is formed by turning its rows into columns and columns into rows. For an m×n matrix, the transpose will be an n×m matrix.

Example:
Input:
a = [[1, 2, 3], [4, 5, 6]]
Output:
[[1, 4], [2, 5], [3, 6]]
Reasoning:

The input is a 2×3 matrix. The transpose swaps rows and columns: the first row [1, 2, 3] becomes the first column, and the second row [4, 5, 6] becomes the second column, resulting in a 3×2 matrix.

Learn About topic
Transpose, Index Swap

Nothing is recomputed; entry (i, j) simply moves to (j, i) and the shape flips.

1
2
3
4
5
6
7
8
9
10
11
12
Transpose
shape 3x4
tap any entry to see its index pair
row 0 of A: 1, 2, 3, 4
entries on i = j never move
Contributors:

Moe Chabot

Contribute
Request Edit