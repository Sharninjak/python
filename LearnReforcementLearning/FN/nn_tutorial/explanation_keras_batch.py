import numpy as np
from tensorflow.python import keras as K

# 2层神经网络
model = K.Sequential([
    K.layers.Dense(units=4, input_shape=((2, )),
                   activation="sigmoid"),
    K.layers.Dense(units=4),
])

# 使批大小为3（数据x的维度为2 ）
batch = np.random.rand(3, 2)

y = model.predict(batch)
print(y.shape)  # 变成(3, 4)
