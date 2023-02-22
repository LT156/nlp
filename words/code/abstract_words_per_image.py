import numpy as np
import pandas as pd
from get_demo_path import get_path
demo_path = get_path()+'/words'
if __name__=='__main__':
    loaded = np.load('F:/work/style_emotion/words/source/new_output/words_feature.npz',allow_pickle=True)
    df2= pd.DataFrame(loaded['feature_df'],columns=loaded['columns'])
    df2=df2[['painting','abstract_NNs','abstract_NNs_len','abstract_features']]
    abstract_features_df = df2.groupby('painting')['abstract_features'].apply(lambda x:np.sum(x,axis=0)).reset_index(name='abstract_features')
    abstract_NNs_df = df2.groupby('painting')['abstract_NNs'].apply(lambda x:[x for sent in x for word in sent]).reset_index(name='abstract_NNs')
    abstract_NNs_len_df =  df2.groupby('painting')['abstract_NNs_len'].apply(lambda x:sum(x)).reset_index(name='abstract_NNs_len')
    df_new = pd.DataFrame({'painting':abstract_features_df['painting'] ,'abstract_NNs':abstract_NNs_df['abstract_NNs'],'abstract_NNs_len':abstract_NNs_len_df['abstract_NNs_len'],'abstract_features':abstract_features_df['abstract_features']  })
    print("特征保存")
    np.savez_compressed(demo_path+'/source/new_output/words_feature2.npz', feature_df=df_new,columns=df_new.columns)