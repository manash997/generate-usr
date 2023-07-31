
<<<<<<< HEAD

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)




=======
>>>>>>> f40b7b3364596217fcfd45b7da36bbfc0acd86b9
# Automated USR Generator

This is a project dedicated for generating USRs that will help the models in translating the sentences.


## Table Of Contents

<<<<<<< HEAD
1. Introduction
2. Features
3. Format of USR
4. Installation
5. Usage/Examples
6. Requirements
7. Documentation
8. Contributing
9. Screenshots
10. Roadmap
11. License
12. Badges
=======
1. 
2. 
3. 
4. 
5. 
>>>>>>> f40b7b3364596217fcfd45b7da36bbfc0acd86b9
## Introduction

Universal Semantic Representation (USR) is a meaning representation that models Indian
Grammatical Tradition (IGT). Meaning (or thought) is there in the mind of the speaker (author)
and (s)he while speaking (writing) makes use of language (or linguistic expressions) to express
his/her thought. Thus a discourse (text) represents the speaker's thought.
This guideline is created to help annotators to make USRs of the written discourse. The objective
is to generate multiple natural languages from these USRs using Natural Language Generators.

## Features

Generally, the normal process of conversion of sentences from one language to another takes a lot of time of annotators. 

But, now with the help of USR generation it is very easy and convenient for them to annotate the same within less amount of time. Additionally, it is very efficient in all terms and conditions.

## Format of USR

The meaning is represented in 11 rows in csv (comma (,) separated value) format. This document
guides the annotators to annotate each row. The 11 rows are:

	Row 1 Original Sentence

	Row 2 Concept

	Row 3 Index

	Row 4 Semantic Category of Noun

	Row 5 Morpho-Semantic Information

	Row 6 Dependency Relation

	Row 7 Discourse Element

	Row 8 Speaker’s View

	Row 9 Scope

	Row 10 Sentence Type
	
	Row 11 Construction
## Installation

1. Create a virtual environment inside the **"usrproginst"** folder using following commands:
	
		cd usrproginst
		python3 -m venv virtual
		source virtual/bin/activate

	
2. Now, install iscnlp tokenizer, pos-tagger and parser. Please follow the given repository link for the same. 
		
		https://bitbucket.org/iscnlp/


-   First, install the tokenizer, then the pos-tagger and lastly install parser.	
- Now read the readme given in the repository for all the three (tokenizer, pos-tagger, parser) and run the given commands in terminal.

### Note: 
Run first command in home directory itself.
- Remember to replace python with python3 while running 3rd step of Readme for all 3 i.e tokenizer, pos-tagger,parser i.e sudo python3 setup.py install.
-  While running 3rd command if you get error related to setup tools then it means pip is not installed in your system and you have to run the following command :-
        
		sudo apt install python3-pip


- In pos-tagger and parser,run these dependencies code after installing them with given command:
	       
		   $ pip install -r requirements.txt

3. Run the following commands on terminal inside parser folder:

		sudo apt install python2
		sudo snap install curl
		curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
		sudo python2 get-pip.py
		sudo apt-get install python-requests
		sudo bash install-project.sh

4. To run the NER model, install the transformers and torch usinf following command:

		pip3 install transformers
		pip3 install torch

### Note: 
If any error occurred then run the following command:

		pip3 install transformers[torch]

5. Now, move wx_utf8, utf8_wx and ir_no@ files to bin folder by running the following command on terminal:

			cd /usr/bin/
			sudo cp ~/usrproginst/wx_utf8 .
			sudo cp ~/usrproginst/utf8_wx .
			sudo cp ~/usrproginst/ir_no@ .

<<<<<<< HEAD
6. After running the above commands now, run the following to give the required permissions :-
=======
6. After running the above commands now, run the following commands:- 
>>>>>>> f40b7b3364596217fcfd45b7da36bbfc0acd86b9
	
            sudo chmod +777 utf8_wx
	        sudo chmod +777 wx_utf8 
	        sudo chmod +777 ir_no@	

7. Now, steps for generating USR:-

- Keep the sentences with their respective IDs seperated by double space in the "sentences_for_USR" file.
- Now, run the following command on the terminal:
	
        python3 run_generate_usr.py
        
- Output USR files will be stored in "bulk_USRs" folder.




    
## Usage/Examples



## Requirements
## Documentation

[Documentation](https://file:///C:/Users/91829/Downloads/Usr%20Program%20Documentation.pdf)


## Contributing

Contributions are always welcome!

If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

- Fork the repository.
- Create your feature branch (git checkout -b feature/YourFeature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/YourFeature).
- Open a pull request.


## Screenshots

picture...

## Roadmap

- Flowchart
- Class Diagrams
- we can include the following things into it.



## License

Generate-USR is released under the MIT License. 

[MIT](https://choosealicense.com/licenses/mit/)

<<<<<<< HEAD
=======

## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


>>>>>>> f40b7b3364596217fcfd45b7da36bbfc0acd86b9
