# Calculate 2x2 Matrix Inverse

**Difficulty**: Easy | **Category**: Linear Algebra

## Description

Write a Python function that calculates the inverse of a 2x2 matrix. The inverse of a matrix A is another matrix A_inv such that A * A_inv = I (the identity matrix).

For a 2x2 matrix [[a, b], [c, d]], the inverse exists only if the determinant (ad - bc) is non-zero.

Return None if the matrix is not invertible (i.e., when the determinant equals zero).

### Example:

- **Input:** matrix = [[4, 7], [2, 6]]

- **Output:** [[0.6, -0.7], [-0.2, 0.4]]

- **Reasoning:** For matrix [[a, b], [c, d]] = [[4, 7], [2, 6]]:

Calculate determinant: det = ad - bc = 4×6 - 7×2 = 24 - 14 = 10
Since det ≠ 0, the matrix is invertible
Apply formula: A⁻¹ = (1/det) × [[d, -b], [-c, a]] = (1/10) × [[6, -7], [-2, 4]] = [[0.6, -0.7], [-0.2, 0.4]]