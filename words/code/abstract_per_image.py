import pandas as pd
from tqdm import tqdm
from ast import literal_eval
from demo_settings.get_demo_path import get_path
demo_path = get_path()+'/words'
if __name__=='__main__':
    df = pd.read_csv(demo_path+'/source/new_output/artemis_abstract_features.csv')
    df['abstract_NNs']=df['abstract_NNs'].apply(literal_eval)
    paintings=[]
    abstract_words=[]
    abstract_words_len=[]
    for painting,g in tqdm(df.groupby('painting')):
        paintings.append(painting)
        tmp_words=[]
        for NNs in g['abstract_NNs'].tolist():
            tmp_words=tmp_words+NNs
        abstract_words.append(tmp_words)
        abstract_words_len.append(len(tmp_words))
    df_new=pd.DataFrame({'paintings':paintings,'abstract_words':abstract_words,'abstract_words_len':abstract_words_len})
    df_new.to_csv(demo_path+'/source/new_output/painting_abstract_words.csv')        