        weights: Neuron weights (one per feature)
        bias: Neuron bias term
    
    Returns:
        Tuple of (predicted probabilities rounded to 4 decimal places, MSE rounded to 
        4 decimal places)
    """
    results = []
    w_t = torch.tensor(weights,dtype = float)
        f_t = torch.tensor(i, dtype = float)
    for i in features:
        labels: List of true binary labels

        features: List of feature vectors (each a list of floats)
        res = torch.matmul(f_t, w_t.T) + bias
        results.append(torch.sigmoid(res).item())
    loss = torch.nn.functional.mse_loss(torch.tensor(results,dtype = float),


                                        torch.tensor(labels, dtype = float))
    return results,loss.item()