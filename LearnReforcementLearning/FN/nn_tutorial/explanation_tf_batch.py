import numpy as np
import tensorflow as tf

# 权重 (row=4 x col=2).
a = tf.Variable(np.random.rand(4, 2))

# 偏置 (row=4 x col=1).
b = tf.Variable(np.random.rand(4, 1))

# 输入(x) (row=2 x col=1).
x = tf.compat.v1.placeholder(tf.float64, shape=(2, 1))

# 输出(y) (row=4 x col=1).
y = tf.matmul(a, x) + b


with tf.Session() as sess:
    # 初始化参数
    init = tf.global_variables_initializer()
    sess.run(init)

    # 生成数据批次
    batch = []
    for i in range(3):
        x_value = np.random.rand(2, 1)
        batch.append(x_value)

    # 执行计算
    y_outputs = []
    for x_value in batch:
        y_output = sess.run(y, feed_dict={x: x_value})
        y_outputs.append(y_output)

    y_output = np.array(y_outputs)
    print(y_output.shape)  # 变成(3, 4, 1)
