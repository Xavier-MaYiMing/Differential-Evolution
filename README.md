

### Differential Evolution

##### Reference: Das S, Suganthan P N. Differential evolution: A survey of the state-of-the-art[J]. IEEE Transactions on Evolutionary Computation, 2010, 15(1): 4-31.

| Variables | Meaning                                            |
| --------- | -------------------------------------------------- |
| npop      | Population number                                  |
| iter      | Iteration number                                   |
| CR        | Crossover rate                                     |
| F         | Mutation scalar number                             |
| min_beta  | The lower bound of scaling factor                  |
| max_beta  | The upper bound of scaling factor                  |
| lb        | The lower bound (list)                             |
| ub        | The upper bound (list)                             |
| pop       | The set of solutions (list)                        |
| Obj       | The objective of solutions (list)                  |
| dim       | Dimension                                          |
| gbest     | The objective of the global best solution          |
| gbest_sol | The global best solution                           |
| iter_best | The global best objective of each iteration (list) |
| con_iter  | The last iteration number when "gbest" is updated  |

#### Test problem: Rastrigin function

$$
f(x)=10n+\sum_{i=1}^n\left[x_i^2-A\cos(2\pi x_i)\right], \qquad x_i\in[-5.12, 5.12]
$$


#### Example

```python
if __name__ == '__main__':
    npop_t = 50
    iter_t = 1000
    CR_t = 0.2
    F_t = 0.6
    lb_t = np.full(10, -5.12)
    ub_t = np.full(10, 5.12)
    print(main(npop_t, iter_t, CR_t, F_t, lb_t, ub_t))
```

##### Output:

##### DE/rand/1/exp

![DE_rand_1_exp](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_1_exp.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([-7.26979764e-10,  7.96471332e-10, -3.27939236e-09, -4.54907431e-10,
        3.25985218e-09, -4.21017489e-09, -4.38079588e-09, -2.09913545e-09,
        4.61489663e-09, -3.18562336e-09]), 
  'convergence iteration': 529
}
```

##### DE/rand/1/bin

![DE_rand_1_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_1_bin.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([ 8.32594475e-10, -3.07269155e-09,  1.42293505e-09, -4.22553344e-09,
       -1.52310568e-09, -4.00181604e-09, -3.93625638e-09,  4.35601021e-09,
        6.25184696e-10, -6.03956570e-09]), 
  'convergence iteration': 606
}
```

##### DE/best/1/exp

![](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_best_1_exp.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([-8.14679667e-10, -7.90141882e-10,  2.39824117e-09,  2.78828907e-11,
       -3.97154331e-09, -1.16577903e-09, -3.07603399e-09, -1.02643038e-09,
       -6.74386538e-09,  2.21909705e-09]), 
  'convergence iteration': 409
}
```

##### DE/best/1/bin

![DE_best_1_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_best_1_bin.png)

```python
{
  'gbest': 0.9949590570932827, 
  'gbest solution': array([-1.38588156e-09,  9.94958634e-01,  5.01073138e-11,  3.00826194e-09,
       -1.89123948e-09, -5.21478462e-10, -1.49024011e-09, -3.63493810e-09,
       -4.88070128e-09,  2.55506085e-09]), 
  'convergence iteration': 315
}
```

##### DE/target-to-best/1/exp

![DE_target-to-best_1_exp](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_target-to-best_1_exp.png)

```python
{
  'gbest': 2.984877440752996, 
  'gbest solution': array([ 9.94953208e-01,  1.47212269e-07,  3.02552362e-05,  9.39520560e-07,
        9.94956863e-01, -2.49234174e-06,  9.94942163e-01,  5.73782697e-06,
        9.81838518e-06, -1.60497478e-06]), 
  'convergence iteration': 986
}
```

##### DE/target-to-best/1/bin

![DE_target-to-best_1_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_target-to-best_1_bin.png)

```python
{
  'gbest': 2.0203034398072504, 
  'gbest solution': array([-4.27551078e-04, -3.76974977e-03, -6.17861695e-04, -9.90948066e-01,
       -1.23564288e-03,  9.31183308e-03, -3.66420290e-03, -2.47117464e-03,
        9.96145001e-01,  3.62772532e-03]), 
  'convergence iteration': 972
}
```

##### DE/best/2/exp

![DE_best_2_exp](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_best_2_exp.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([ 2.03776116e-09, -4.07521716e-09, -1.33888372e-09, -1.53352749e-09,
       -6.38359731e-11, -4.67234367e-09, -4.54734321e-09,  4.45601520e-09,
        6.68322468e-10, -6.77052786e-09]), 
  'convergence iteration': 562
}
```

##### DE/best/2/bin

![DE_best_2_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_best_2_bin.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([-1.05880147e-09, -1.80082556e-09, -1.74409904e-09,  2.42234295e-10,
        5.85843650e-11, -4.08310610e-09,  1.28732000e-09, -2.76756855e-09,
        8.85028673e-10,  5.71658496e-09]), 
  'convergence iteration': 705
}
```

##### DE/rand/2/exp

![DE_rand_2_exp](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_2_exp.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([-1.84716217e-09, -3.89810740e-09,  1.42406560e-09,  5.39030561e-09,
        3.28428210e-09, -7.53682592e-10,  2.35718077e-09,  2.36516638e-10,
        4.02270228e-10, -2.52707134e-09]), 
  'convergence iteration': 691
}
```

##### DE/rand/2/bin

![DE_rand_2_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_2_bin.png)

```python
{
  'gbest': 1.5631940186722204e-13, 
  'gbest solution': array([-8.39539034e-09,  1.20618822e-08, -7.79473731e-09,  3.75828367e-09,
       -6.53319125e-09, -7.27417574e-09, -7.50482297e-10, -2.63856681e-09,
        1.99746872e-08,  4.66376499e-09]), 
  'convergence iteration': 998
}
```

##### DE/rand/2/dir/exp

![DE_rand_2_dir_exp](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_2_dir_exp.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([ 7.39358874e-10, -1.56502678e-09,  1.69823238e-09,  3.45744743e-09,
       -3.21767535e-09, -1.54514618e-09, -3.74288765e-09, -4.81328766e-09,
        5.69122312e-09,  3.56782454e-09]), 
  'convergence iteration': 506
}
```

##### DE/rand/2/dir/bin

![DE_rand_2_dir_bin](/Users/xavier/Desktop/Xavier Ma/个人算法主页/Differential Evolution/DE_rand_2_dir_bin.png)

```python
{
  'gbest': 0.0, 
  'gbest solution': array([ 3.32373628e-09, -1.63993502e-09,  1.41951613e-09, -2.73454640e-09,
       -3.68247827e-09,  4.09255167e-09,  4.33626030e-09, -1.62537869e-09,
       -4.99862043e-09, -1.25810345e-09]), 
  'convergence iteration': 540
}
```

