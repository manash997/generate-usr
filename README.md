<a href="https://github.com/manash997/generate-usr/stargazers"><img src="https://img.shields.io/github/stars/manash997/generate-usr" alt="Stars Badge"/></a>
<a href="https://github.com/manash997/generate-usr/forks"><img src="https://img.shields.io/github/forks/manash997/generate-usr" alt="Forks Badge"/></a>
<a href="https://github.com/manash997/generate-usr/pulls"><img src="https://img.shields.io/github/issues-pr/manash997/generate-usr" alt="Pull Requests Badge"/></a>
<a href="https://github.com/manash997/generate-usr/issues"><img src="https://img.shields.io/github/issues/manash997/generate-usr" alt="Issues Badge"/></a>
<a href="https://github.com/manash997/generate-usr/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/manash997/generate-usr?color=2b9348"></a>

## Automated USR Generator

This is a project dedicated for generating USRs that will help the models in translating the sentences.

## Table Of Contents

1. Introduction
2. Format of USR
3. Installation
4. Usage/Examples
5. Requirements
6. Documentation
7. Contributing
8. Screenshots
9. License

## Introduction

Welcome to Automated USR Generator, an innovative open-source project developed in Python. This powerful tool is designed to effortlessly generate USRs (Universal Sentence Representations) from any input sentence or a bulk of sentences. USRs play a pivotal role in natural language processing and understanding, enabling various downstream tasks such as sentiment analysis, text classification, and machine translation.

The project leverages several essential modules to achieve its functionality. First, we have the "pos tagger and parser" module, which is utilized effectively to parse the input sentences and extract their syntactic dependencies as well as extract pos tags. This ensures that the subsequent processing steps have access to the correct linguistic structure.

Next up is the "wx" module, which is employed by the "wx" component. This step takes the input in UTF-8 format and then converts it into wx_format.

The "morph_call_1.py" module comes into play with the "morph" component. This stage focuses on deriving and separating root_word, GNP(Gender, Number, Person) and TAM(Tense, Aspect, Modality) from the given input sentence.	

After morphological analysis, the "converter.py" module is there which takes output from apertium.morph and convert it into csv format which will be easy to process.

Furthermore, the "ner_call.py" module is employed for  Named Entity Recognition (NER). This process identifies entities such as names of people, organizations, locations, etc., and enriches the sentence representation with this valuable contextual information.

Finally, the heart of the USR generation process lies in the "generate_usr.py" module. This module orchestrates all the preceding steps, combining the output from the parser, wx, morph, prune, and NER components to create comprehensive and effective Universal Sentence Representations.

Whether you need to process a single sentence or analyze a large dataset of sentences, Automated USR Generator provides a simple yet powerful interface to cater to your needs. The project's open-source nature encourages contributions and collaboration from the community, fostering continuous improvement and expanding its capabilities.

## Format of USR

The meaning is represented in 11 rows in CSV (comma (,) separated value) format. This document
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
```javascript
		cd usrproginst
		python3 -m venv virtual
		source virtual/bin/activate
```	
2. Now, install iscnlp tokenizer, pos-tagger and parser. Please follow the given repository link for the same. 
		
		https://bitbucket.org/iscnlp/

- First, install the tokenizer, then the pos-tagger and lastly install parser.	
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


6. After running the above commands now, run the following to give the required permissions :-

6. After running the above commands now, run the following commands:- 

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
functional_diagram
## Documentation

[Click here to view the Documentation](https://github.com/manash997/generate-usr/blob/main/Documentation_for_generate_usr.python.pdf)

## Contributing

#### Contributions are always welcome! 

Follow the given steps for contributing to this project:-

- Fork the repository on GitHub.

- Clone the forked repository to your local machine using git clone.

- Create a new branch for your contribution using git checkout -b <branch-name>. Choose a meaningful name that describes your changes.

- Make the necessary changes and improvements to the codebase.

- Before committing your changes, ensure that your code follows our coding standards and guidelines.

- Test your changes thoroughly to ensure they work as intended.

- Commit your changes with a descriptive commit message using git commit.

- Push the changes to your forked repository with git push origin <branch-name>.

- Go to the original repository on GitHub and create a Pull Request (PR) from your forked repository.

- Provide a clear and descriptive title for your PR, summarizing the changes you've made.

By following these guidelines, you can contribute to our open-source project effectively and help make it even better! 

Thank you for your contributions and support.

## Screenshots

picture...

## Roadmap

- Flowchart
- Class Diagrams
- we can include the following things into it.

## License

Generate-USR is released under the MIT License.
</a>
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


