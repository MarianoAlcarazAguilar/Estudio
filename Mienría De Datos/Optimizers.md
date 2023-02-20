# Optimizers
Veamos una comparación general

<img src="./images/Screenshot 2023-02-18 at 18.24.19.png">

## Activation Functions

### Linear

$$ a = \sum_{n=0}^{N}x_nw_n $$
$$ \frac{\partial a}{\partial w_i} = x_i $$

### Sigmoid

$$ a = \sigma (s) = \frac{1}{1 + e^{-s}} $$
$$ \sigma \prime (s) = \sigma (s)(1 - \sigma(s)) $$

### Tanh

$$ a \frac{e^s - e^{-s}}{e^s + e^{-s}} $$
$$ a\prime = 1 - a^2 $$

### ReLU
Logistic functions suffer of the so-called *vanishing gradient* issue (la derivada en los extremos es 0, entonces la propagación se pierde).<br>  
Rectified Linear Unites (ReLU) are an alternative:

$$
f(x)=
\begin{cases}
0, & \quad \text{$s < 0$}\\ 
s, & \quad s \geq 0
\end{cases}
$$

$$
a\prime =
\begin{cases}
0, \quad s < 0,\\
1, \quad s \geq 0
\end{cases}
$$

Since the derivative is so simple, this is also more efficient computationally speaking.

### Softmax
All previous functions are element-wise operations. **Softmax** is a vector normalizer.

$$a_i = \frac{e^{s_i}}{\sum_{j}e^{s_j}}$$
$$a_i\prime = a_i(1 - a_i) $$

It is used to exaggerate the most probable of the elements of the vector. Useful in output layers for multi-class classification problems.

## Common Use Scenarios

| Activation | Use |
| --- | --- |
| ReLU (variants) | All hidden layers in all scenarios |
| Sigmoid (tanh) | Output layer for binary classifications |
| Sigmoid | Output layer for regression with $0 \leq y \leq 1$ |
| Tanh | Output layer for regression with $-1 \leq y \leq 1$ |
| Linear | Output layer for unbounded regression |
| Softmax | Output layer for multi-class classification |

## Optimization Functions

### Momentum
Dampens oscillation. Includes a fraction of the historic direction.  
Es como un promedio ponderado temporal que se va desvaneciendo conforme se hacen más antiguos.

$$
w_t = w_{t-1} - v_t
$$
$$
v_t = \gamma v_{t-1} + \eta \nabla_w\mathcal{L}(y, \hat y)
$$
with,
$$ v_0 = 0, \gamma = 0.9, \eta \approx 0.0001 $$

- Accelerates SGD in the relevant directions
- Dampens oscillations
- Includes a fraction of the historic direction
- Momentum accelerates for gradients pointing in the same direction, and reduces for those in changing direction

### Nesterov Accelerated Gradient (NAG)
Calcula el peso y corrige si se equivocó.

$$ w_t = w_{t-1} - v_t $$
$$ v_t = \gamma v_{t-1} + \eta \nabla_{(x-\gamma v_{t-1})}\mathcal{L}(y, \hat y) $$

- $\nabla_{(w-\gamma v_{t-1})}$ approximates the next postion of $w$
- Looks ahead by calculating the gradient w.r.t. future positions
- Anticipates changes in the direction of the gradient

### Adaptive Gradient (AdaGrad)
Cada vez vamos avanzando menos y menos. Pondera la tasa de aprendizaje.

$$w_t = w_{t-1} - \eta \frac{1}{\sqrt{G_t + \epsilon}}g_t, \quad \quad g_t=\nabla_w\mathcal{L}(y, \hat y),$$
$$G_t = \sum_{k=0}^{t}g_t^2, \quad \quad \epsilon \approx 1e^{-8}$$

- $G_t$: sum of gradients $^2$ up to time $t$ (hevy memory loads)
- Adapts $\eta$ at each time step (always decreasing)
- Works well on sparse data and large models

### Adadelta
Parecido al de arriba.

$$w_t = w_{t-1} - \eta \frac{1}{\sqrt{\mathbb{E}[g^2]_t}}g_t, \quad \quad g_t = \nabla_w\mathcal{L}(y, \hat y), $$
$$\mathbb{E}[g^2]_t = \gamma\mathbb{E}[g^2]_{t-1} + (1 - \gamma)g_t^2, \quad \quad \gamma = 0.9$$

- Addresses the issue of monotonically decreasing $\eta$
- Restricts the past to a moving window
- Recursively computes the sum of past gradients using exponential smoothing

### Adaptive Momentum (Adam)
Adadelta + Momentum. Esta tiende a converger más rápido.

We have the first moment estimate (mean), 
$$m_t = \beta_1m_{t-1} + (1 - \beta_1)g_t, \quad \quad$$
And the second moment estimate (stddv),
$$v_t = \beta_2 v_{t-1} + (1 - \beta_2)g_t^2$$

And correcting for bias towards zero:
$$\hat{m_t} = \frac{m_t}{1 - \beta_1^t}; \quad \hat{v_t} = \frac{v_t}{1 - \beta_2^t}$$
$$w_t = w_{t-1} - \eta \frac{1}{\sqrt{\hat{v_t}} + \epsilon}\hat{m_t}$$

Es bueno usar esta función de optimzación para bajar rápido, aunque puede tener mucha variablidad, por lo que es buena idea combinar esta con **adadelta**, la cual baja de forma más lenta pero con menos variabilidad.