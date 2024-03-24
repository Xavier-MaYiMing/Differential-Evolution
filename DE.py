#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 15:16
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : DE.py
# @Statement : Differential Evolution
# @Reference : Das S, Suganthan P N. Differential evolution: A survey of the state-of-the-art[J]. IEEE Transactions on Evolutionary Computation, 2010, 15(1): 4-31.
import numpy as np
import matplotlib.pyplot as plt


def cal_obj(x):
    # Rastrigin function
    return 10 * len(x) + sum(x ** 2) - 10 * sum(np.cos(2 * np.pi * x))


def mutation1(pop, npop, F):
    # DE/rand/1
    [r1, r2, r3] = np.random.choice(range(npop), 3, replace=False)
    donor = pop[r1] + F * (pop[r2] - pop[r3])
    return donor


def mutation2(pop, gbest_sol, npop, F):
    # DE/best/1
    [r1, r2] = np.random.choice(range(npop), 2, replace=False)
    donor = gbest_sol + F * (pop[r1] - pop[r2])
    return donor


def mutation3(pop, target, gbest_sol, npop, F):
    # DE/target-to-best/1
    [r1, r2] = np.random.choice(range(npop), 2, replace=False)
    donor = target + F * (gbest_sol - target) + F * (pop[r1] - pop[r2])
    return donor


def mutation4(pop, gbest_sol, npop, F):
    # DE/best/2
    [r1, r2, r3, r4] = np.random.choice(range(npop), 4, replace=False)
    donor = gbest_sol + F * (pop[r1] - pop[r2]) + F * (pop[r3] - pop[r4])
    return donor


def mutation5(pop, npop, F):
    # DE/rand/2
    [r1, r2, r3, r4, r5] = np.random.choice(range(npop), 5, replace=False)
    donor = pop[r1] + F * (pop[r2] - pop[r3]) + F * (pop[r4] - pop[r5])
    return donor


def mutation6(pop, obj, npop, F):
    # DE/rand/2/dir
    [r1, r2, r3] = np.random.choice(range(npop), 3, replace=False)
    r = [r1, r2, r3]
    o = [obj[r1], obj[r2], obj[r3]]
    s = np.argsort(o)
    r1, r2, r3 = r[s[0]], r[s[1]], r[s[2]]
    donor = pop[r1] + F / 2 * (pop[r1] - pop[r2] - pop[r3])
    return donor


def crossover1(target, donor, dim, CR):
    # Exponential crossover
    trail = target.copy()
    L = 1
    while np.random.rand() <= CR and L <= dim:
        L += 1
    n = np.random.randint(0, dim)
    for j in range(n, n + L):
        j %= dim
        trail[j] = donor[j]
    return trail


def crossover2(target, donor, dim, CR):
    # Binomial crossover
    trail = target.copy()
    j = np.random.randint(0, dim)
    trail[j] = donor[j]
    flag = np.random.rand(dim) < CR
    for i in range(dim):
        if flag[i]:
            trail[i] = donor[i]
    return trail


def boundary_check(sol, lb, ub, dim):
    # Check the boundary
    flag1 = sol > ub
    flag2 = sol < lb
    for i in range(dim):
        if flag1[i]:
            sol[i] = ub[i]
        elif flag2[i]:
            sol[i] = lb[i]
    return sol


def main(npop, iter, CR, F, lb, ub):
    """
    The main function of DE
    :param npop: population number
    :param iter: iteration number
    :param CR: crossover rate
    :param F: mutation scalar number
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    dim = len(lb)  # dimension
    pop = np.random.rand(npop, dim) * (ub - lb)  # population
    obj = [cal_obj(pop[i]) for i in range(npop)]  # objectives
    gbest = min(obj)  # the global best
    gbest_sol = pop[obj.index(gbest)]  # the global best solution
    iter_best = []  # the global best of each iteration
    con_iter = 0  # the convergence iteration

    # Step 2. The main loop
    for t in range(iter):
        for i in range(npop):

            # Step 2.1. Mutation
            donor = mutation1(pop, npop, F)
            # donor = mutation2(pop, gbest_sol, npop, F)
            # donor = mutation3(pop, pop[i], gbest_sol, npop, F)
            # donor = mutation4(pop, gbest_sol, npop, F)
            # donor = mutation5(pop, npop, F)
            # donor = mutation6(pop, obj, npop, F)
            donor = boundary_check(donor, lb, ub, dim)

            # Step 2.2. Crossover
            trial = crossover1(pop[i], donor, dim, CR)
            # trial = crossover2(pop[i], donor, dim, CR)

            # Step 2.3. Selection
            new_obj = cal_obj(trial)
            if new_obj < obj[i]:
                obj[i] = new_obj
                pop[i] = trial
                if new_obj < gbest:
                    gbest = new_obj
                    gbest_sol = trial
                    con_iter = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('DE/rand/1/exp')
    plt.savefig('DE_rand_1_exp.png')
    plt.show()
    return {'gbest': gbest, 'gbest solution': gbest_sol, 'convergence iteration': con_iter}


if __name__ == '__main__':
    npop_t = 50
    iter_t = 1000
    CR_t = 0.2
    F_t = 0.6
    lb_t = np.full(10, -5.12)
    ub_t = np.full(10, 5.12)
    print(main(npop_t, iter_t, CR_t, F_t, lb_t, ub_t))
