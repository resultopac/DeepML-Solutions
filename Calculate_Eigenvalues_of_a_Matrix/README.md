# Calculate Eigenvalues of a Matrix

**Difficulty**: Easy | **Category**: Linear Algebra

## Description

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

### Example:

- **Input:** matrix = [[2, 1], [1, 2]]

- **Output:** [3.0, 1.0]

- **Reasoning:** The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is 
𝜆
2
−
𝑡
𝑟
𝑎
𝑐
𝑒
(
𝐴
)
𝜆
+
𝑑
𝑒
𝑡
(
𝐴
)
=
0
λ
2
−trace(A)λ+det(A)=0, where 
𝜆
λ are the eigenvalues.