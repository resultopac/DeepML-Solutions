import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending 
    order (highest to lowest).
    """
    eigenvals, eigenvecs = torch.linalg.eig(matrix)
    return torch.sort(eigenvals.real, descending = True).values
