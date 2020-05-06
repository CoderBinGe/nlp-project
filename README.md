**说明：由于所有项目是在CPU上跑的，所以没有调参，只是测试代码是否能够正常运行。**

**TextRCNN**
- 构建的词典有存储到本地
- 数据集的划分是train_test_split
- padding调用的是pad_sequences

**TextRCNN2**
- 构建的词典没有存储到本地
- 数据集的划分是train_test_split
- padding调用的是pad_sequences

**TextRCNN3**
- 词典的构建
- 训练数据集构建时自己padding
- 交叉验证StratifiedKFold
