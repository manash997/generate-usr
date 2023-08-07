import os
os.system("isc-parser -i txt_files/bh-1 > txt_files/parser-output.txt")
os.system("python3 dependency.py") 
os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")
os.system("python3 sentence_to_morph.py")
os.system("python3 parser_postag_based_prunedmorph.py")
os.system("python3 sentence_to_ner.py ")
os.system("python3 generate_usr.py") 
