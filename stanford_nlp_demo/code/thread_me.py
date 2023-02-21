import _thread
import pandas as pd
from artemis_NN_extract import get_NNS

demo_path='F:/github_code/nlp/stanford_nlp_demo'
#读取文件
df = pd.read_csv(demo_path+'/sources/data_file/artemis_dataset_release_v0.csv')
text_list = df['utterance'].tolist()
try:
    _thread.start_new_thread( get_NNS,( text_list[:100], 1) )
    _thread.start_new_thread( get_NNS, (text_list[101:200], 2) )
except:
    print ("Error: 无法启动线程")