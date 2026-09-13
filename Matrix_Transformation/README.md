# Matrix Transformation

**Difficulty**: Medium | **Category**: Linear Algebra

## Description

Write a Python function that transforms a given matrix A using the operation 
𝑇
−
1
𝐴
𝑆
T
−1
AS, where T and S are invertible matrices. The function should first validate if the matrices T and S are invertible, and then perform the transformation. In cases where there is no solution return -1

### Example:

- **Input:** A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]

- **Output:** [[0.5,1.5],[1.5,3.5]]

- **Reasoning:** The matrices T and S are used to transform matrix A by computing 
𝑇
−
1
𝐴
𝑆
T
−1
AS.