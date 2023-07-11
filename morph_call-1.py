import os
#import subprocess

input_folder = "txt_files/"
sentence_file = "wx.txt"
single_concept_inp = "concept.txt"
single_concept_out = "concept.txt-out.txt"
output_file = "morph-output.txt"

input_file_path = os.path.join(input_folder,sentence_file)
output_file_path = os.path.join(input_folder,output_file)

with open(output_file_path,"w") as out:
    out.write("")

if os.path.isfile(input_file_path):
   with open(input_file_path,"r") as inp:
        sentence = inp.read().strip()
        words = sentence.split()

        for word in words:
        #print(word)
            with open(single_concept_inp,"w") as sc:
                sc.write(word)
                #print(word)

            os.system("sh run_morph-analyser.sh " + single_concept_inp)
            #subprocess.run(["sh", script, input_folder+"/"+sentence_file])

            with open(single_concept_out,"r") as con_out:
                output = con_out.read().strip()

            with open(output_file_path,"a") as out:
                out.write(output + "\n")

            with open(single_concept_inp,"w") as sc:
                sc.write("")

            with open(single_concept_out,"w") as con_out:
                con_out.write("")



