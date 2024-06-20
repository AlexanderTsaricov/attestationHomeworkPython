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

data.loc[data['whoAmI'] == 'human', 'isHuman'] = True
data.loc[data['whoAmI'] != 'human', 'isHuman'] = False
data.loc[data['whoAmI'] == 'robot', 'isRobot'] = True
data.loc[data['whoAmI'] != 'robot', 'isRobot'] = False
data.drop(columns='whoAmI', axis = 1, inplace= True)
print(data.head(10))
