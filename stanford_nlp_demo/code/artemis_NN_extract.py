import nltk
import pandas as pd
from ast import literal_eval
from text_clean import artemis_text_clean
from stanfordcorenlp import StanfordCoreNLP
#斯坦福句子解析，名词标注
from nltk.parse.stanford import StanfordParser
from tqdm import tqdm
#指明安装路径和语言类型(中文)

demo_path='F:/work/style_emotion/stanford_nlp_demo'

nlp = StanfordCoreNLP(demo_path+'/sources/lib/stanford-corenlp-full-2018-02-27', lang='en')

my_path_to_models_jar = demo_path+'/sources/lib/stanford-corenlp-full-2018-02-27/stanford-corenlp-3.9.1-models.jar'
my_path_to_jar = demo_path+'/sources/lib/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'
parser = StanfordParser(path_to_models_jar=my_path_to_models_jar, path_to_jar=my_path_to_jar)



NN_words=[]
def traverse_tree(tree):
    """
    深度遍历nltk.tree
    :param tree: nltk.tree对象
    :return: 无
    """
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            traverse_tree(subtree)
            if str(subtree)[1:-1].find('(')==-1:
                result = str(subtree)[1:-1].split(' ')
                if result[0] in ['NN','NR','NT','NNS','NNP','NNPS']:
                    NN_words.append(result[1])


if __name__=='__main__':
    #读取文件
    df = pd.read_csv(demo_path+'/sources/data_file/artemis_dataset_release_v0.csv')
    text_list = df['utterance'].tolist()[:20]
    
    #文件清理
    clean_text = [artemis_text_clean(sent) for sent in text_list]
    
    NN_words = []
    for sent in tqdm(text_list):
        (result, )=parser.parse(nlp.word_tokenize(artemis_text_clean(sent)))
        traverse_tree(result)
    
    data = NN_words
    f = open(demo_path+'/output/txt/NN_words.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()