### Differential Evolution

##### Reference: Das S, Suganthan P N. Differential evolution: A survey of the state-of-the-art[J]. IEEE Transactions on Evolutionary Computation, 2010, 15(1): 4-31.

| Variables | Meaning                                           |
| --------- | ------------------------------------------------- |
| npop      | Population size                                   |
| iter      | Iteration number                                  |
| pc        | Crossover probability                             |
| min_beta  | The lower bound of scaling factor                 |
| max_beta  | The upper bound of scaling factor                 |
| lb        | The lower bound (list)                            |
| ub        | The upper bound (list)                            |
| pop       | The set of individuals (list)                     |
| score     | The score of individuals (list)                   |
| dim       | Dimension                                         |
| gbest     | The score of the global best individual           |
| gbest_ind | The position of the global best individual (list) |
| iter_best | The global best score of each iteration (list)    |
| con_iter  | The last iteration number when "gbest" is updated |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Differential-Evolution/blob/main/Pressure%20vessel%20design.png)

$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    npop = 50
    iter = 2000
    pc = 0.2
    min_beta = 0.2
    max_beta = 0.8
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(npop, iter, pc, min_beta, max_beta, lb, ub))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Differential-Evolution/blob/main/Convergence%20curve.png)

The DE converges at its 1890-th iteration, and the global best value is 8051.07421220017 

```python
{
    'best score': 8051.07421220017, 
    'best solution': [1.3005554054902362, 0.6428792568908404, 67.38602231180363, 10.000092332537305], 
    'convergence iteration': 1890
}
```

