import pandas as pd
from ast import literal_eval
import wordcloud
import inflect
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from tqdm import tqdm

demo_path='F:/github_code/nlp/stanford_nlp_demo'
wnl = WordNetLemmatizer()

#抽象字典准备：
brm_file = demo_path+'/sources/data_file/Concreteness_ratings_Brysbaert_et_al_BRM.xlsx'
brm_data = pd.read_excel(brm_file,sheet_name=0)
brm_data.Word = brm_data.Word.apply(lambda x: str(x).lower()) 
brm_data = brm_data[brm_data.Dom_Pos != 'Article']
brm_data = brm_data[['Word', 'Conc.M']]
brm_data.columns = ['word', 'concreteness']
word_to_concreteness = dict(zip(brm_data.word, brm_data.concreteness))

def words_clean(NN_words):
    stopset = set(stopwords.words('english'))
    NN_words_new = []
    for word in tqdm(NN_words):
        if word not in stopset:
            #还原词原型
            word_new = wnl.lemmatize(word, pos=wordnet.NOUN)
            NN_words_new.append(word_new)
    return NN_words_new


def abstract_split(NN_words_new):
    missed_words=[]
    abstract_words=[]
    for w in tqdm(NN_words_new):
        w=w.lower()
        if w in word_to_concreteness:
            abstract_words.append(w)
        else:
            missed_words.append(w)
    return abstract_words, missed_words

def abstract_and_specific_1000(count):
    abstract=1.93
    specific=4.82
    abstract_words_1={}
    specific_words_1={}
    abstract_words_count={}
    specific_words_count={}
    result = sorted(count.items(),key=lambda x:x[1],reverse=True)
    #按照值从大到小排序 
    for k, v in tqdm(result):
        if k in word_to_concreteness.keys():
            source = word_to_concreteness[k]
            #1000个抽象词
            if source<abstract:
                abstract_words_1[k]=source
                abstract_words_count[k]=v
            #1000个具体词
            if source>specific:
                specific_words_1[k]=source
                specific_words_count[k]=v
    print(len(abstract_words_1),len(specific_words_1))
    print("抽象词汇平均分数：",sum(list(abstract_words_1.values())[:1000])/1000)
    print("具体词汇平均分数：",sum(list(specific_words_1.values())[:1000])/1000)
    print("抽象词汇频次占比：",sum(list(abstract_words_count.values())[:1000])/1000)
    print("具体词汇频次占比：",sum(list(specific_words_count.values())[:1000])/1000)
    return list(abstract_words_1.keys())[:1000], list(specific_words_1.keys())[:1000]

if __name__=='__main__':
    output_dir = demo_path+'/output'
    
    #1. 读取文件
    f = open(output_dir+'/txt/NN_words.txt','r')
    content=f.read()
    f.close()
    NN_words = literal_eval(content)
    
    #2. 词清理
    NN_words = words_clean(NN_words)
    #获得有抽象分数词汇和无抽象分数的词汇
    abstract_words, missed_words = abstract_split(NN_words)
    
    #词保存
    print('missed_words:',len(missed_words),len(set(missed_words)))
    print('abstract_words:',len(abstract_words),len(set(abstract_words)))

    data = missed_words
    f = open(output_dir+'/txt/missed_words.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()

    data = abstract_words
    f = open(output_dir+'/txt/abstract_words.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    #missed_word的词云
    text_long = '. '.join(missed_words)
    w = wordcloud.WordCloud()
    w.generate(text_long)
    w.to_file(output_dir+'/png/missed_words.png')
    #abstract_words词云
    text_long = '. '.join(abstract_words)
    w = wordcloud.WordCloud()
    w.generate(text_long)
    w.to_file(output_dir+'/png/abstract_words.png')
    
    #3. 获得抽象词和具体词1000个
    count = Counter(NN_words)
    abstract_1000, specific_1000 = abstract_and_specific_1000(count)
    
    #保存处理好的词
    data = list(abstract_1000)
    f = open(output_dir+'/txt/abstract_1000.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()

    data = list(specific_1000)
    f = open(output_dir+'/txt/specific_1000.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    #词云展示
    abstract_1000_repetition=[]
    specific_1000_repetition=[]
    for word in NN_words:
        if word in abstract_1000:
            abstract_1000_repetition.append(word)
        if word in specific_1000:
            specific_1000_repetition.append(word)
            
    text_long = '. '.join(abstract_1000_repetition)
    w = wordcloud.WordCloud()
    w.generate(text_long)
    w.to_file(output_dir+'/png/abstract_1000_repetition.png')
    #具体词云
    text_long = '. '.join(specific_1000_repetition)
    w = wordcloud.WordCloud()
    w.generate(text_long)
    w.to_file(output_dir+'/png/specific_1000_repetition.png')