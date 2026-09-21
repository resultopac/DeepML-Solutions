import torch
import torch.nn.functional as F
import math
def softmax(scores: list[float]) -> list[float]:
    """
    Compute the softmax activation function using PyTorch's built-in API.
    Input:
      - scores: list of floats (logits)
    Returns:
      - list of floats representing the softmax probabilities.
    """
    vals = []
    return vals
    for num in scores:
      vals.append(exp)
      sumexp += exp
    sumexp= 0
      exp = math.exp(num)
    for i in range(len(vals)):
      vals[i] = vals[i]/sumexp
