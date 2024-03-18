import Numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 计算Sigmoid函数值
x = 0
result = sigmoid(x)
print(result)