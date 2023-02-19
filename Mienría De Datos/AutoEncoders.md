# AutoEncoders

## Beyond Supervision

### Supervised Learning
Pairs 
$$\{x^{(n)}, y^{(n)}\}_{n=1}^N$$ 
of input and output data. The goal is to learn model 
$$\hat y^{(n)} = f(x^{(n)}; \Omega)$$
Such that 
$$ \quad \mathcal{L}(y^{(n)}, \hat y^{(n)}) \approx 0$$
ANN's are, by design, models for supervised learning.

### Unsupervised Learning
No labels $y^{(n)}$ for training. Only
$$\{x^{(n)}\}_{n=1}^N$$
We do not learn a mapping function. Rather, we tray to make sense of,
$$\{x^{(n)}\}$$
Examples:
- Clustering
- Density estimation
- Anomaly detection
- Dimensionality reduction

### Self-supervised Learning

Strictly speaking, unsupervised learning is not possible with ANN's.  
We take a roundabout with self-supervised learning.

- Learn models to approximate a task on the input data
- Input and output are the same data
$$(x^{(n)}, \hat x^{(n)})$$
- Examples:
   - Clean noisy data
   - Dimensionality reduction

<div align="center">
<img src="./images/Screenshot 2023-02-18 at 18.26.40.png" height="300">
</div>

### Discriminative vs Generative

**Discriminative Models** $\Rightarrow$ conditional probability
$$\mathbb{P}(y | x; \Omega)$$
**Generative Models** $\Rightarrow$ join probability distribution
$$\mathbb{P}(x; \Omega) = \mathbb P (x_1, x_2, ..., x_N; \Omega)$$

## Autoencoders

ANN that learns to reproduce its own input, while learning interesting data representations.

<div align="center">
<img src="./images/Screenshot 2023-02-18 at 18.26.50.png" width="300">
</div>

Intermediate output is known as $\text{latent representation}$, and denoted by $z$.

### Structure
- Encoder
- Latent representation
- Decoder
- Regularizers (optional)

<div align="center">
<img src="./images/Screenshot 2023-02-18 at 18.26.58.png" height="300">
</div>

### Representation Learning

Is a subset of machine learning, which is of high relevance in deep learning.  
It deals with the study (analysis, design, interpretability, etc.) of the intermedaite representations of a deep nerual network. 

$$\text{Understand how knowledge is learned and represented}$$

Understanding and designing $\text{latent representations}$ can be done by principles of representation learning.

### Undercomplete AE

- AE with hidden representation that are **shorter** than input
- Produces undercomplete representations
- Output after linear transformation equivalent to **PCA** (si todo el encoding se hace de forma lineal, lo que te queda en las dimensiones reducidas es equivalente a hacer PCA en el sentido que te quedan en el mismo espacio, pero no necesariamente van a ser ortonormales)

### Overcomplete AE
- **Larger** latent representation

### Sparse AE
- **Sparsity** by constrains

### Deep AE
Deeper models enable more non-linear transformations, which might lead to richer latent representations

<div align="center">
<img src="./images/Screenshot 2023-02-18 at 18.27.13.png" height="300">
</div>

### Conv AE
<img src="./images/Screenshot 2023-02-18 at 18.27.22.png">

### Pretraining with AE's

Often ther is a lot of unlabeled data out there.
1. Pretrain your model with an AE
2. Transfer weights to a decision model (classifier)
3. Fine tune the transfered weights for specific tasks.

## Variational Inference

### AE's limitations
Latent space of AE is learned to comply with the task of interest, but with no other particular restriction, specially not on its shape
- No special structure
- Latent space might be discontinue
- Sampling from it produces samples from the unknown space
- Decoding unknown samples might lead to noise

<img src="./images/Screenshot 2023-02-18 at 18.27.52.png">

### Variational AE (VAE)
Approximate an observable probability distribution $\mathbb{P}(z|x)$, with another parametric distribution $\mathcal{Q}(z)$

- $\mathcal{Q}(z)$ is chosen to be Gaussian
- VAE's latent space is, by design, continuous
- Latent representation: means $(\mu)$ and standard deviations $(\sigma)$

<img src="./images/Screenshot 2023-02-18 at 18.28.00.png">

### Variational Inference

The **Goal** is to find a distribution 
$$\mathcal{Q}(z|x)$$
of some latent variable $z$, from which we could sample
$$ z \sim \mathcal{Q}(z|x)$$
and then we can generate new synthetic samples,
$$ \hat x \sim \mathbb{P}(x | z)$$

<img src="./images/Screenshot 2023-02-18 at 18.28.06.png">

But it is very hard to find the marginal $\mathbb{P}(x)$, as we need to integrate ist conditional over the whole latent space.  

Instead, minimize the difference between the observable distribution and the ideal Gaussian.  

Use Kullback-Leibler divergence,
$$\mathcal{L}^T = \mathcal{L}^R(x, \hat x) + \gamma D_{KL}(\mathcal{Q}(z)|\mathbb{P}(z))$$
where,
$$\mathbb{P}(z) \sim \mathcal{N}(\mu, \sigma)$$
and $\gamma$ is a weighting factor.

## Other Unsupervised Methods

### Restricted Boltzman Machines (RBM)
- Two_layers NN: input and hidden representation
- No output layer
- Backprop against feed-backward loss
- Input reconstruction from hidden representation

<img src="./images/Screenshot 2023-02-18 at 18.28.29.png">

### Deep Belief Networks (DBN)

Cascaded array of RBM's

<img src="./images/Screenshot 2023-02-18 at 18.28.36.png">
