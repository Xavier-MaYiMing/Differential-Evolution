#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 14:42
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : DE.py
# @Statement : Differential Evolution
# @Reference : Das S, Suganthan P N. Differential evolution: A survey of the state-of-the-art[J]. IEEE Transactions on Evolutionary Computation, 2010, 15(1): 4-31.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(x, lb, ub, dim):
    """
    Check the boundary
    :param x: a candidate solution
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :param dim: dimension
    :return:
    """
    for i in range(dim):
        if x[i] < lb[i]:
            x[i] = lb[i]
        elif x[i] > ub[i]:
            x[i] = ub[i]
    return x


def main(npop, iter, pc, min_beta, max_beta, lb, ub):
    """
    The main function of DE
    :param npop: population size
    :param iter: iteration number
    :param pc: crossover probability
    :param min_beta: the lower bound of scaling factor
    :param max_beta: the upper bound of scaling factor
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    pop = []  # population
    score = []  # the score of population
    dim = len(lb)  # dimension
    ind_list = [i for i in range(npop)]  # the index list
    for _ in range(npop):
        temp_pop = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        pop.append(temp_pop)
        score.append(obj(temp_pop))
    gbest = min(score)  # the global best
    gbest_ind = pop[score.index(gbest)]  # the global best individual
    iter_best = []  # the global best of each iteration
    con_iter = 0  # the convergence iteration

    # Step 2. The main loop
    for t in range(iter):
        for i in range(npop):
            temp_ind_list = random.sample(ind_list, 3)
            while i in temp_ind_list:
                temp_ind_list = random.sample(ind_list, 3)
                r1 = temp_ind_list[0]
                r2 = temp_ind_list[1]
                r3 = temp_ind_list[2]

                # Step 2.1. Mutation
                beta = random.uniform(min_beta, max_beta)
                new_ind = [pop[r1][j] + beta * (pop[r2][j] - pop[r3][j]) for j in range(dim)]
                new_ind = boundary_check(new_ind, lb, ub, dim)

                # Step 2.2. Binomial crossover
                for j in range(dim):
                    if random.randint(0, 1) == 1 or random.random() <= pc:
                        pass
                    else:
                        new_ind[j] = pop[i][j]

                # Step 2.3. Selection
                new_score = obj(new_ind)
                if new_score < score[i]:
                    score[i] = new_score
                    pop[i] = new_ind.copy()
                    if new_score < gbest:
                        gbest = score[i]
                        gbest_ind = new_ind.copy()
                        con_iter = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_ind, 'convergence iteration': con_iter}


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
