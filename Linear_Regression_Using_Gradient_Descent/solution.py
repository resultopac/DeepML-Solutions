        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D tensor of shape (n,)
    """
    X_t = torch.as_tensor(X, dtype=torch.float32)
    y_t = torch.as_tensor(y, dtype=torch.float32).reshape(-1, 1)
    m, n = X_t.shape
    theta = torch.zeros((n, 1), requires_grad=True) 
    def forward(x):
        return x @ theta
    optimizer = torch.optim.SGD(params=[theta],lr=alpha)
    optimizer.zero_grad()
    for epoch in range(iterations):
        y_pred = forward(X_t)
        loss = ((y_pred - y_t) ** 2).sum() / (2 * m)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return theta.detach().squeeze()