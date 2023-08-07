import re 
f=open("txt_files/parser-output.txt")
pos_tag=[]
matched_span=[]
for line in f:
    try:
        cat=line.split("\t")[3].strip()
        pos_tag.append(cat)
    except:
        pass
f.close()
#print("pos_tag_before:",pos_tag)
mapper_dict={"NN":"n","NST":"nst","NNP":"n","NEG":"avy","PRP":"p",
             "PSP":"prsg","DEM":"p","VM":"v","VAUX":"v","JJ":"adj",
             "RB":"adv","RP":"avy","CC":"avy","CL":"avy","WQ":"p",
             "QF":"avy","QC":"num","QO":"num","INTF":"avy","INJ":"avy",
             "UT":"avy","UNK":"unk","SYM":"s","XC":"c"}
for inx in range(len(pos_tag)):
    if pos_tag[inx] in mapper_dict:
        mapped_op=mapper_dict[pos_tag[inx]]
        pos_tag[inx]=mapped_op
#print("pos_tag_after:",pos_tag)
f=open("txt_files/morph-output.txt","r")
#print("hello")
item_c=0
for line in f:
    matches=re.findall("<cat:([^>]*)",line.strip())
    if len(matches)==0:
        matched_span.append(line)
        continue
    #print("match:",matches)
    for word in matches:
        if word in pos_tag:
            first_inx=matches.index(word)
            #print(first_inx)
            sent=line.split("/")[first_inx+1]
            #print(sent)
            matched_span.append("/"+sent.strip())
            break
f.close()
#print("ms",matched_span)
        
    
#split_by_dol=line.split("$")
#split_by_dol=[x for x in split_by_dol if x!=""]
#print(split_by_dol)
###Extract the original words and store them in a list
original_word=[]
f=open("txt_files/morph-output.txt","r")
for sent in f:
    input_str=sent
    start_marker="^"
    end_marker="/"
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    original_word.append(input_str[start_index+1:end_index])
original_word.pop()
#print("og:",original_word)

###Extract root words
root_word=[]
for sent in matched_span:
    #print("sent:",sent)
    input_str=sent.strip()
    start_marker="/"
    end_marker="<"
    if "<"  not in input_str:
        #print("yes")
        end_marker="$"
    
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    root_word.append(input_str[start_index+1:end_index])
#print(original_word)
#print(root_word)

###Extract GNP and tam
gender=[]
number=[]
person=[]
tam=[]
for sent in matched_span:
    input_str=sent
    start_marker="<gen:"
    end_marker=">"
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    if start_index!=-1:
        gender.append(input_str[start_index+1:end_index])
    else:
        gender.append("gen:unk")
    
    start_marker="<num:"
    end_marker=">"
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    if start_index!=-1:
        number.append(input_str[start_index+1:end_index])
    else:
        number.append("num:unk")
    
    start_marker="<per:"
    end_marker=">"
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    if start_index!=-1:
        person.append(input_str[start_index+1:end_index])
    else:
        person.append("per:unk")

    start_marker="<tam:"
    end_marker=">"
    start_index=input_str.find(start_marker)
    end_index=input_str.find(end_marker,start_index)
    if start_index!=-1:
        tam.append(input_str[start_index+1:end_index])
    else:
        tam.append("tam:unk")
#print(gender)
#print(number)
#print(person)
#print(tam)
#print(root_word)
#print("Sentence:")
#print("Morph Output")
#print("<Sentence id=1>")
#print("</Sentence>")
#print("Sentence:")
#print("Pruning Output")
#print("<Sentence id=1")
#print("org:",original_word)
#print("rw",root_word)
f=open("txt_files/prune-output.txt","w")
for i in range(len(original_word)):
    try:
        #ogw=original_word[i] if not None else "unk"
        #rw=root_word[i].strip("*") if not None else "unk"
        #gn=gender[i].split(":")[1] if not None else "unk"
        #no=number[i].split(":")[1] if not None else "unk"
        #per=person[i].split(":")[1] if not None else "unk"
        #tam=tam[i].split(":")[1] if not None else "unk"

        #print(root_word[i])
        f.write(str(i+1)+","+original_word[i]+","+root_word[i].strip("*")+","+gender[i].split(":")[1]+","+number[i].split(":")[1]+","+person[i].split(":")[1]+","+tam[i].split(":")[1]+"\n")
    except:
        f.write(str(i+1)+","+original_word[i]+","+root_word[i].strip("*")+","+"unk"+","+"unk"+","+"unk"+","+"unk"+"\n")
    

#print("1	ram	unk	<fs af=’root,category,gender,number,person,case,tam,tam’>")
#print("</Sentence")
#print("NER Output")
#print("<Sentence id=1>")
#for i in range(len(original_word)):
#    print(str(i+1)+"\t"+original_word[i]+"\t"+"unk")
#print("</Sentence>")
