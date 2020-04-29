

inputs = './data/weibo_senti_100k.txt'

outputs = './data/weibo_senti_100k_random.txt'


embedding_dim = 300

epochs = 1

batch_size = 64

# epochs = 20      #迭代次数
# batch_size = 512*2  #每个batch大小

path_checkpoint = './lstm_model/sentiment_checkpoint10.keras'

model_path = './lstm_model/sentiment_checkpoint10.h5'