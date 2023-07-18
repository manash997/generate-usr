import os
def check_punctuation(sentence):
    flag=0
    list_punc_with_space=[" |"," ?"," !"," ।"," ."]
    list_punc_without_space=["|","?","!","।"]
    
    
    if sentence.endswith(tuple(list_punc_with_space))==True:
        flag=1
        length=len(sentence)
        last_word=sentence[-1]
        if last_word=="।" or last_word=="|":
            sentence=sentence.replace(last_word,".")
    elif sentence.endswith(tuple(list_punc_without_space))==True: 
        flag=1
        length=len(sentence)
        last_word=sentence[-1]
        if last_word=="।" or last_word=="|":
            sentence=sentence.replace(last_word," "+".")
        else:
            sentence=sentence.replace(last_word," "+last_word)
    elif sentence.endswith(tuple("."))==True:
        flag=1
        sentence=sentence.replace("."," "+".")
    elif sentence.endswith(tuple(" ."))==True:
        flag=1
        sentence=sentence.replace(".",".")

    if flag==0:
        sentence=sentence+" ."
    

    return sentence
def remove_allpunc(sentence):
    # define punctuation
    punctuations = [",","#","<",">","(",")"]
    for sym in punctuations:
        if sym in sentence:
            sentence=sentence.replace(sym," ")
    return sentence

if __name__=="__main__":
    file_name_input="txt_files/bh-1"
    file_name_output="txt_files/bh-1"
    #file_name_input="tmp_files/temp1.txt"
    #file_name_output="tmp_files/temp1.txt"
    
    with open(file_name_input,"r",encoding="UTF-8") as f:
        sentence=f.readline()
        sentence=sentence.strip()
        #print(sentence)
        #sentence=remove_allpunc(sentence)
        sentence=check_punctuation(sentence)
        sentence=remove_allpunc(sentence)

    os.remove(file_name_input)    
    f=open(file_name_output,"w",encoding="UTF-8")
    f.write(sentence)