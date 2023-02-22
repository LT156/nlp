import pandas as pd
from ast import literal_eval
import nltk
import wordcloud
from tqdm import tqdm
from collections import Counter
from nltk.corpus import stopwords
from get_demo_path import get_path
demo_path = get_path()+'/words'

wnl = nltk.stem.WordNetLemmatizer()
stopset = set(stopwords.words('english'))

#抽象字典准备：
brm_file = demo_path+'/resource/data_file/Concreteness_ratings_Brysbaert_et_al_BRM.xlsx'
brm_data = pd.read_excel(brm_file,sheet_name=0)
brm_data.Word = brm_data.Word.apply(lambda x: str(x).lower()) 
brm_data = brm_data[brm_data.Dom_Pos != 'Article']
brm_data = brm_data[['Word', 'Conc.M']]
brm_data.columns = ['word', 'concreteness']
word_to_concreteness = dict(zip(brm_data.word, brm_data.concreteness))

def get_NNwords(text):
    #获取名词
    # 分割句子
    words = nltk.word_tokenize(text)
    # 词性标注
    taged_sent = nltk.pos_tag(words)
    #输出名词https://blog.csdn.net/qq_36652619/article/details/77252497
    labels = ['NN','NNS','NNP','NNPS']
    NN_words = []
    # 复数还原/非停用词
    for w,l in taged_sent:
        if w not in stopset and l in labels:
            if l in ['NNS','NNPS']:
                w=wnl.lemmatize(w,'n')
            NN_words.append(w.lower())
    return NN_words 

if __name__=='__main__':
    
    df = pd.read_csv(demo_path+'/resource/data_file/artemis_preprocessed.csv')
    text_list = df['utterance'].tolist()
    text_list = [text.lower() for text in text_list]
    
    #获取名词
    NN_words = []
    artemis_NN_df = []
    for text in tqdm(text_list):
        result=get_NNwords(text) 
        NN_words=NN_words+result
        artemis_NN_df.append(result)
    df['NNS']=artemis_NN_df
        
    print('NN_words:',len(NN_words),len(set(NN_words)))
        
    data = NN_words
    f = open(demo_path+'/resource/new_output/NN_words.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    count = Counter(NN_words)
    cc=sorted(count.items(),key=lambda x:x[1],reverse=True) #按照值从大到小排序
    data = cc
    f = open(demo_path+'/resource/new_output/artemis_NN_counter.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    missed_words=[]
    abstract_words=[]
    words_2=[]
    values = 0
    
    for w in NN_words:
        if w in word_to_concreteness:
            abstract_words.append(w)
            values=values+word_to_concreteness[w]
            if word_to_concreteness[w]<2:
                words_2.append(w)
        else:
            missed_words.append(w)
        
            
    print('missed_words:',len(missed_words),len(set(missed_words)))
    print('abstract_words:',len(abstract_words),len(set(abstract_words)))
    print('words_2:',len(words_2),len(set(words_2)))
    
    print('abstract_words_avg_resource:',values/len(abstract_words))
    
    data = set(missed_words)
    f = open(demo_path+'/resource/new_output/artemis_missed_words.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    artemis_abstract_dict={}
    for word in abstract_words:
        artemis_abstract_dict[word]=word_to_concreteness[word]
        
    artemis_abstract_dict = sorted(artemis_abstract_dict.items(), key=lambda x: x[1])
        
    data = artemis_abstract_dict
    f = open(demo_path+'/resource/new_output/artemis_abstract_dict.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    df.to_csv(demo_path+'/resource/new_output/artemis_abstract_dict_df.csv')
    
    
    
    
    
    