
from ast import literal_eval

if __name__=='__main__':
    demo_path = 'F:/work/style_emotion/words'
    
    f = open(demo_path+'/source/new_output/artemis_NN_counter.txt','r')
    content=f.read()
    f.close()
    artemis_NN_counter = dict(literal_eval(content))
    
    f = open(demo_path+'/source/new_output/artemis_abstract_dict.txt','r')
    content=f.read()
    f.close()
    artemis_abstract_dict = dict(literal_eval(content))
    
    words_2=[]
    words_2_2=[]
    w_count=0
    w_count_2=0
    for word,count in artemis_NN_counter.items():
        if word in artemis_abstract_dict.keys():
            if count>13 and artemis_abstract_dict[word]<2.49:
            #if artemis_abstract_dict[word]<2.5:
                words_2.append(word)
                w_count=w_count+count
            if count>13:
                w_count_2=w_count_2+count
                words_2_2.append(word)
    print('words_2:',len(words_2))
    print('w_count:',w_count)
    print('words_2_2:',len(words_2_2))
    print('w_count_2:',w_count_2)
    w_count_2
    
    data = words_2[:1000]
    f = open(demo_path+'/source/new_output/artemis_abstract_1000.txt','w')
    f.write(str(data).encode('gbk','ignore').decode('gbk'))
    f.close()
    
    