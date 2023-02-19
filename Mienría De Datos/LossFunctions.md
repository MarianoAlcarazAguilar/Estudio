# Loss Functions

Estas son las funciones que se busca minimizar.

## Common Practices

| Problem | Solution |
| --- | --- |
| Regression | $mse$ and $mae$ |
| Binary Classification | $\text{binary  cross entropy}$|
| Multi-class Classification | $\text{categorical cross entropy}$

## Mean Square Error (mse)
- También se le conoce como $L2$ loss.
- Es buena para tareas de **regresión**
- Trivial derivative for gradient descent
$$
\mathcal{l}_{mse} = \frac{1}{M}\sum_{m=i}^M(y^{(i)} - \hat y^{(i)})^2
$$

Where,
- $M$ indicates the number of training samples in a batch.

<img src="./images/Screenshot 2023-02-18 at 18.24.58.png">


## Mean Absolut Error (mae)

- $L1$ loss
- More robust to outliers than $mse$
- Good for **regression** tasks
- Discontinuity in its derivative

$$
l_{mae} = \frac{1}{M}\sum_{m=i}^M|y^{(i)} - \hat y^{(i)}|
$$

Where,
- $M$ indicates the number of training samples in a batch

<img src="./images/Screenshot 2023-02-18 at 18.25.05.png">

## Pseudo-Huber Loss

- Quadratic for small errors, and linear for large errors.
- Less sensitive to outliers than $mse$
- Good for **regresssion** tasks

$$
l_{PH} = 
\begin{cases}
\frac{1}{2}(y-\hat y)^2, \quad |y - \hat y| < \delta \\
\delta | y - \hat y| - \frac{1}{2}\delta^2, \quad \text{otherwise}
\end{cases}
$$

<img src="./images/Screenshot 2023-02-18 at 18.25.11.png">


## Information Theory

### Information
For a random variable, taking $N$ possible values with equal probability, we need $log_2(N)$ bits to transmit its information

For a random variable, taking N possible values with varying probabilities $p_i$, we obtain $-\sum_ip_ilog_2(p_i)$ bits of information, on average.  
<br>

### Entropy
"how uncertain events are".

$$
H(p) = -\sum_ip_ilog_2(p_i)
$$

- Average amount of information obtained from one sample drawn from a given probability distribuition **$p$**.
- How unpredictable that probability distribution is

The more variation, the higher the intropy.  
<br>

### Cross Entropy

Cross entropy $H(p,q)$ is a function of two probability distributions $p$ and $q$,

$$
H(p,q) = -\sum_ip_ilog_2(q_i)
$$

Provides the average message length when we encode $p$ into $q$.  
If prediction is correct, then $H(p) = H(p,q)$

## Categorical Cross Entropy
- Good for **multi-class classification** problems
- Consider $y$ to be a one-hot encoding vector, e.g. $[0,1,0,0]$ represents the label of the $2th$ class
- Prediction $\hat y$ might look like $[0.01, 0.01, 0.03, 0.93, 0.02]$  
<br>

$$
l_{CCE} = -\sum_i y_i log_2(\hat y_i)
$$

- Notice subindices represent elements of a vector
- Values between $0$ and $1$
<br>

## Binary Cross Entropy
It's a special case of cross entropy for only two classes.

- Good for **binary classification** problems

$$
l_{BCE} = -(ylog_2(\hat y) + (1-y)log_2(1 - \hat y))
$$

- Values between $0$ and $1$
<br>

## Kullback-Leibler Divergence ($D_{KL}$)

- Equivalent to categorical cross entropy up to a scale factor
- Gives notion of the "difference between the expected and predicted length of a message"
- Good for **classification** prolems  
<br>

$$
l_{D_{KL}} = \sum_iy_ilog_2\frac{y_i}{\hat y_i}
$$

$\quad \quad D_{KL}(p|q) = H(p,q) - H(p)$


