from collections import defaultdict
import numpy as np
import pandas as pd
from django.test import TestCase

# Create your tests here.

if __name__ == '__main__':
    # 방법 1
    dc1 = {}
    dc2 = {}
    dc3 = {}
    ls1 = ['10', '20','30','40','50']
    ls2 = [10, 20, 30, 40, 50]
    # for i in range(0, len(ls1)):
    #     dc1[ls1[i]] = ls2[i]
    # dc1 = { ls1[i]:ls2[i] for i in range(0, len(ls1))}
    dc1.update({ ls1[i]:ls2[i] for i in range(0, len(ls1))})

    # 방법 zip()
    # for i, j in zip(ls1, ls2):
    #     dc2[i] = j
    dc2.update({ i:j for i, j in zip(ls1, ls2) })

    # 방법 enumerate()
    # for i, j in enumerate(ls1):
    #     dc3[j] = ls2[i]
    dc3.update({j: ls2[i] for i, j in enumerate(ls1)} )

    print('*'*30)
    print(dc1)
    print('*'*30)
    print(dc2)
    print('*'*30)
    print(dc3)
    print('*'*30)