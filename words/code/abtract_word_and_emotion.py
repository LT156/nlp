import pandas as pd
import numpy as np
from ast import literal_eval
from tqdm import tqdm 
demo_path='F:/work/style_emotion/words'

f = open(demo_path+'/source/new_output/artemis_abstract_1000.txt','r')
content=f.read()
f.close()
artemis_abstract_1000 = literal_eval(content)

ARTEMIS_EMOTIONS = ['amusement', 'awe', 'contentment', 'excitement',
                    'anger', 'disgust',  'fear', 'sadness', 'something else']

def get_abstractWords_info(NN_list,emotion_list):
    abstract_NNs=[]
    abstract_NNs_len=[]
    abstract_features = []
    abstract_emotions_dict={}
    index=0
    for NNs in tqdm(NN_list):
        tmp = []
        tmp_feature = np.zeros((1000))
        for word in NNs:
            if word in artemis_abstract_1000:
                tmp.append(word)
                i=artemis_abstract_1000.index(word)
                tmp_feature[i]=tmp_feature[i]+1
                abstract_emotions_dict=record_word_emotion(word,emotion_list[index],abstract_emotions_dict)
        abstract_NNs.append(tmp)
        abstract_NNs_len.append(len(tmp))
        abstract_features.append(tmp_feature)
        index=index+1
    return abstract_NNs,abstract_NNs_len,abstract_features,abstract_emotions_dict
        
        
def record_word_emotion(word,emotion,abstract_emotions_dict):
    abstract_emotion = np.zeros((9))
    if word not in abstract_emotions_dict.keys():
        abstract_emotion[ARTEMIS_EMOTIONS.index(emotion)]=1
        abstract_emotions_dict[word]=abstract_emotion
    else:
        abstract_emotion=abstract_emotions_dict[word]
        abstract_emotion[ARTEMIS_EMOTIONS.index(emotion)]=abstract_emotion[ARTEMIS_EMOTIONS.index(emotion)]+1
        abstract_emotions_dict[word]=abstract_emotion
    return abstract_emotions_dict
    
        
if __name__=='__main__':
    df = pd.read_csv(demo_path+'/source/new_output/artemis_abstract_dict_df.csv')
    df['NNS']=df['NNS'].apply(literal_eval)
    NN_list=df['NNS'].tolist()
    emotion_list=df['emotion'].tolist()
    abstract_NNs,abstract_NNs_len,abstract_features,abstract_emotions_dict =  get_abstractWords_info(NN_list,emotion_list)
    
    df['abstract_NNs']=abstract_NNs
    df['abstract_NNs_len']=abstract_NNs_len
    
    
    feature_dict=dict(zip(df['painting'].tolist(),abstract_features))
    
    data = abstract_emotions_dict
    f = open(demo_path+'/source/new_output/artemis_abstract_emotions.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    df.to_csv(demo_path+'/source/new_output/artemis_abstract_features.csv')
    df['abstract_features']=abstract_features
    print("特征保存")
    np.savez_compressed(demo_path+'/source/new_output/words_feature.npz', feature_df=df,columns=df.columns)
