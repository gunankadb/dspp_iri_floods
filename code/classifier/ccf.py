#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import numpy as np

def ccf(x, y, tupList=False):
    if tupList:
        assert len(x) == len(y) and np.prod([x[i][0] == y[i][0] for i in range(len(x))]) == 1
        x = [i[1] for i in x]
        y = [i[1] for i in y]
    result, pval = spearmanr(x,y)
    result2, pval2 = pearsonr(x,y)
    print('Spearmen Corr, pval: {}, p-val={}, n={}'.format(round(result,4), pval, len(x)))
    print('Pearson Corr, pval: {}, p-val={}, n={}'.format(round(result2,4), pval2, len(x)))
    return (round(result,4), pval, len(x)), (round(result2,4), pval2, len(x))