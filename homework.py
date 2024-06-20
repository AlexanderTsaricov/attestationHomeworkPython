'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data['whoAmI'])
humanOneHot = '01'
robotOneHot = '10'

data.loc[data['whoAmI'] == 'robot', 'whoAmI'] = robotOneHot
data.loc[data['whoAmI'] == 'human', 'whoAmI'] = humanOneHot
print('_______Заменили значения_______')
print(data['whoAmI'])

