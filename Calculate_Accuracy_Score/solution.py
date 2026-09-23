import torch
from typing import Union

def accuracy_score(y_true: Union[torch.Tensor, list, "np.ndarray"],
                   y_pred: Union[torch.Tensor, list, "np.ndarray"]) -> float:
    """
    Compute the accuracy: fraction of matching elements in y_true and y_pred.
    Both inputs may be torch.Tensor, list, or numpy.ndarray.
    """
    tot = 0
    acc = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_true[i]:
            acc+=1
        tot += 1
    return acc/tot
