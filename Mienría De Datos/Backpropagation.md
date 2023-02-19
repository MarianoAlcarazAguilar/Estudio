# Backpropagation

Recordando el algoritmo de descenso en gradiente, tenemos que,

~~~py
# Inicializamos los pesos aleatoriamente
weights = random_initialization()
# Iteramos sobre cada época
for epoch in epochs:
   # Iteramos sobre cada elemento
   for sample in samples:
      # Calculamos los valores predecidos
      y_hat = f(x; weights)
      # Calculamos el error
      E_i = loss(y, y_hat)
      # Ajustamos los pesos
      weights = weights - eta*derivative(E_i)
~~~

<kbd>PRECAUCIÓN</kbd><br>
La desventaja de este approach es que el modelo estará sesgado hacia los últimos datos vistos.

### Stochastic Gradient Descent
Intenta compensar un poco el error del algoritmo anterior: **en cada época, reordena de forma aleatoria los datos** para que de esta forma la red neuronal no se aprenda los valores "*de memoria*".

El algorimto es de la siguiente forma:

~~~py
# Inicalizamos los pesos aleatoriamente
weights = random_initialization()
# Iteramos sobre cada época
for epoch in epochs:
   # Reorganizamos los datos de forma aleatoria
   {X, y} = shuffle({X, y})
   # Iteramos sobre cada mezcla de datos (dato por dato)
   for sample in samples:
      # Calculamos los valores predecidos
      y_hat = f(x; weights)
      # Encontramos el error
      E_i = loss(y, y_hat)
      # Ajustamos los pesos
      weights = weights - eta*derivative(E_i)
~~~

#### Limitations
$$w_i = w_i - \nabla _{w_i} \mathcal{L}(y, \hat{y}) $$ 

- Slows down around ravines
- Oscillates across the slopes of the ravine
- Limited progress towards the local minimum
- Might never escape from saddle points

### Batch Gradient Descent
Es otra forma de hacerlo, pero esta vez no se hace el cambio dato por datos, sino que se toman por **batches** y el ajuste se hace sobre la media de las pérdidas en ese subconjunto, lo que lo hace aún más generalizable.

El algoritmo queda de la siguiente forma:

~~~py
# Inicializamos los pesos de forma aleatoria
weights = random_initialization()
# Definimos el número de batches que se quiere usar
# O en su defecto, el tamaño del batch con el que se desea trabajar
n_batches = define_number_of_batches()
# Iteramos sobre cada época
for epoch in epochs:
   # Reorganizamos los datos de forma aleatoria
   {X, y} = shuffle({X, y})
   # Para cada una de las batches iteramos
   for batch in batches:
      # Tomamos los datos correspondientes al batch
      {X_b, y_b} = next_N_training_pairs()
      # Encontramos los valores predecidos para todos los datos correspondietes
      y_hat_b = f(X_b, weights)
      # Calculamos el error promedio en el batch
      E_b = mean(loss(y_b_n, y_hat_b_n))
      # Ajustamos los pesos con el promedio encontrado
      weights = weights - eta*derivative(E_b)
~~~


Ventajas de este approach:
- Approximates $E$ with the average error of a batch of samples
- Fewer updates $\Rightarrow$ faster optimization process

Algunas notas:
- Batch size $bs = 1 \Rightarrow$ Regular GD
- Common batch sizes: $\{16, 32, 64, 128, 256\}$


## Multilayer Perceptron
Lamentablemente, no todos los problemas en la realidad son lineales

<img src="./images/Screenshot 2023-02-18 at 18.22.25.png">

### Non-linear Transformations
Una forma de solucionar estas situaciones es hacer transformaciones no lineales. Por ejemplo,

- Crear una nueva feature:<br> $$x_2 = x_1^2$$ $$x_3 = x_2*x_1$$
- Selección de features: usar solo un subconjunto de todas las variables disponibles

### Multilayer Perceptron
Consecutive linear operations are equivalent to a single linear operation. ***Deep Learning*** enables the use of non-linear activation functions that result in the solution to non-linear problems.

- We end up with: **input**, **hidden**, and **output layers**
- Intermediate representations correspond feature engineering
- However, features are learned rather than engineered
- End-to-end process
- Information abstracion increases with depth

In general, the more difficult the problem looks, the more chances are it is non-linearly separable. Therfore, the deeper the model, de better.

### Backpropagation
Para poder encontrar las derivadas correspondientes a cada peso se usa la regla de la cadena

Tomemos en cuenta las siguientes definiciones:

$$s=\sum_{i}w_ix_i + b$$
$$a = \sigma(s)$$

Las funciones lineales y no lineales, respectivamente.

<img src="./images/Screenshot 2023-02-18 at 18.23.28.png">

Y etonces nos queda la derivada como sigue,

$$
\frac{\partial E}{\partial w_i} = \frac{\partial E}{\partial y} \frac{\partial y}{\partial a_j} \frac{\partial a_j}{\partial s_j} \frac{\partial s_j}{\partial a_i} \frac{\partial a_i}{\partial s_i} \frac{\partial s_i}{\partial w_i}
$$

Si tenemos conexiones múltiples, entonces se suman todos los posibles caminos a cada peso,

<img src="./images/Screenshot 2023-02-18 at 18.23.52.png">


$$
\frac{\partial E}{\partial w_1} = \frac{\partial E}{\partial a_5} \frac{\partial a_5}{\partial s_5} \frac{\partial s_5}{\partial a_3} \frac{\partial a_3}{\partial s_3} \frac{\partial s_3}{\partial a_1} \frac{\partial a_1}{\partial s_1} \frac{\partial s_1}{\partial w_1} + \frac{\partial E}{\partial a_5} \frac{\partial a_5}{\partial s_5} \frac{\partial s_5}{\partial a_4} \frac{\partial a_4}{\partial s_4} \frac{\partial s_4}{\partial a_1} \frac{\partial a_1}{\partial s_1} \frac{\partial s_1}{\partial w_1}
$$

## Multi-variate regression

One output perceptron works well for uni-variate regression, $\hat {y}$ is a scalar.<br>
More perceptrons can be used for a multi-variate proble, $\hat {y}$ is a vector

<img src="./images/Screenshot 2023-02-18 at 18.24.01.png">
