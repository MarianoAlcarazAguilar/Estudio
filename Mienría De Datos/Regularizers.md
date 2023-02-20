# Regularizers

Recordemos lo siguiente,

- El **entrenamiento** es aprender los parámetros del modelo
- La **validación** es evaluar el modelo en datos no vistos

Se espera tener un desempeño similar en ambos conjuntos (se supone que ambos provienen de la misma distribución de probabilidad)

En caso de que exista un **gap** entre el desempeño de uno y el otro, es bueno usar **hyper-parameters**.

<img src="./images/Screenshot 2023-02-18 at 18.25.28.png">

## Overfitting

Model fits training data extremely good, but fails to generalize for unseen data.  
**Solution**: give up some performance level on the training set in favor of improvement in the validation set.

<img src="./images/Screenshot 2023-02-18 at 18.25.34.png">

### Bias and Variance

- **Bias**: Inability of a model to learn the true mapping relationship between $x$ and $y$, which implies *underfitting*
- **Variance** Difference in fits between training and validation sets, which might imply *overfitting*. E.g. high-order polynomial

### Bias-Variance trade-off
**Ideal Model**: 
- Low bias $\Rightarrow$ accurate mapping function 
- Low variance $\Rightarrow$ performance is consistent between training and validation sets.

<img src="./images/Screenshot 2023-02-18 at 18.25.40.png">

### Common practices

| Underfitting | Overfitting |
| --- | --- |
| Add capacity | Early stopping |
| Add epochs | Gather more data |
| Add data | Decrease features |
| Add features | Add Regularizers |
| Data augmentation | Data augmentation |


## Regularizers

Limit the model capacity, by adding a penalty to the parameters

$$
\mathcal{L}_T(x,y;\Omega) = \mathcal{L}(x,y;\Omega) + \alpha \mathcal{P}(\Omega),
$$

where,
- $\mathcal L(x,y;\Omega)$ corresponds to the target loss already known,
- $\mathcal{P}(\Omega)$ is the penalty function on the parameters,
- $\alpha$ weights the penalty of the parameters, and
- $\mathcal{L}_T(x,y;\Omega)$ indicates the total loss

### Weight Decay $L2$
Also known as Ridge Regression or Tikhonov regularization.

$$
\mathcal{P}(\Omega) = \frac{1}{2}||\Omega||_2^2
$$
Derivative:
$$\Omega$$

### Lasso $L1$
Besides keeping small values for $\omega_i$ it also induces sparsity.

$$\mathcal{P}(\Omega) = ||\Omega||_1 = \sum_i|\omega_i|$$
Derivative:
$$sign(\Omega)$$

### Elastic $L2L1$

Ridge $+$ Lasso

$$\mathcal{P}(\Omega) = \alpha_R||\Omega||_2^2 + \alpha_L||\Omega||_1$$
Derivative:
$$\Omega + sign(\Omega)$$

### Regularized Space
Keep parameter values at the intersection between the Loss space and the Penalty space

<img src="./images/Screenshot 2023-02-18 at 18.25.55.png">

### Dropout
- Add stochasticity
- During training, limit the capacity of the model at random
- Deactivate neurons (dropout) or weights (dropconnect)
- Forces the network to become reduntant
- Also helps make the model robust against variations

<img src="./images/Screenshot 2023-02-18 at 18.26.02.png">


### Batch Normalization

- Normalization is often applied to input layer (accelerates learning)
- We can do the same with hidden layers
- Adds noise and learns to be robust against it
- Induces independence beween layers

Comput the batch mean and variance:

$$\mu_B = \frac{1}{M}\sum_{m=1}^Mx^{(m)}, \quad \sigma_B^2 = \frac{1}{M}\sum_{m=1}^M(x^{(m)}-\mu_B)^2$$
Normalize and feed to next layer:
$$\hat x^{(m)} = \gamma \cdot \frac{x^{(m)-\mu_B}}{\sqrt{\sigma_B^2 + \epsilon}} + \beta$$

## Inicializadores
Es una forma de empezar el valor de los parámetros a estimar (de algún lugar se tiene que empezar).

### Xavier Glorot
Este es la forma tradicional de hacerlo.


$$
w = \mathcal{U}\left(-\frac{1}{\sqrt n},\frac{1}{\sqrt n}\right)
$$

where,
- $n$ es el número de variables

Bueno para,
- Lineal
- Sigmoid
- Tanh

### Normalized Xavier
Este es un poco más estable

$$
w = \mathcal{U}\left(-\frac{\sqrt b}{\sqrt{n+m}}, \frac{\sqrt b}{\sqrt{n+m}}\right)
$$

where,
- $n$ es el número de variables que entran a la capa
- $m$ es el número de variables que salen de la capa

Bueno para,
- Lineal
- Sigmoid
- Tanh

### Kaiming He
Sin notas específicas

$$
w = \mathcal N\left(0, \sqrt{\frac{2}{n}} \right)
$$

where,
- $n$ es el número de variables

Bueno para,
- ReLU