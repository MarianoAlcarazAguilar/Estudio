# Perceptron

## Linear Regression
Approximate *y* from the input data **x**, using the set of weights **w** = {*w*<sub>i</sub>},

<div align="center"><b>y</b> = <b>Xw</b></div>

We could learn **w** using the normal equation (least squares):

<div align="center">
   <b>w</b> = (<b>X</b><sup>T</sup><b>X</b>)<sup>-1</sup><b>X</b><sup>T</sup><b>y</b>
</div>

## Logistic Regression
Similarly, we could fit a logistic function to perform binary classification: true vs false.

<div align="center">
   <i>s</i> = <b>w</b><sup><i>T</i></sup><b>x</b><br>
   <i>y</i> = &sigma;(<i>s</i>)
</div>

where,

$$
   \sigma(s) = \frac{1}{1 + e^{-s}}
$$
es la función **sigmoide**. Y en realidad da la probabilidad de que $y = 1$.

<img src="./images/Screenshot 2023-02-18 at 18.21.25.png">

## Perceptron Lineal

Es otra forma de forumular el problema de regresiones.


<img src="./images/Screenshot 2023-02-18 at 18.21.31.png">

### Usando la función de activación sigmoide

<img src="./images/Screenshot 2023-02-18 at 18.21.36.png">


# Gradient Descent

## Weights Estimation
To estimate the values for $\{w_i\}$ we use an iterative minimization approach termed *Gradient Descent* (GD).

- Most complex problems have no closed-form solution
- Iterative approaches reach fairly good approximations
- Risk of getting trapped in local minima


We require a <kbd>loss function</kbd> e.g., $E = (y - \hat{y})^2$.  
Remember: relation between derivative, tangent, and direction.

<img src="./images/Screenshot 2023-02-18 at 18.21.51.png">

And we can move in the opposite direction of the derivative,

$$
w_i = w_i - \eta \frac{\partial E}{\partial w_i}
$$

We must always move in the direction of the steepest descent, so first, compute **all the partial derivatives and then update**.

## Procedure

~~~py
random_initialization()
for epoch in epochs:
   for training_point in training_points:
      # Calculamos los pesos
      forward_pass()
      # Calculamos el error
      error_computation()
      # Calculamos el gradiante
      gradient_estimation()
      # Ajustamos los pesos
      backward_pass()
~~~

