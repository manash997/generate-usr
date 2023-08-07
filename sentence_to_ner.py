from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("AI4bharatner_tokenizer")

model = AutoModelForTokenClassification.from_pretrained("AI4bharatner")

def get_predictions( sentence, tokenizer, model ):
  # Let us first tokenize the sentence - split words into subwords
  tok_sentence = tokenizer(sentence, return_tensors='pt')

  with torch.no_grad():
    # we will send the tokenized sentence to the model to get predictions
    logits = model(**tok_sentence).logits.argmax(-1)
    
    # We will map the maximum predicted class id with the class label
    predicted_tokens_classes = [model.config.id2label[t.item()] for t in logits[0]]
    
    predicted_labels = []
    
    previous_token_id = 0
    # we need to assign the named entity label to the head word and not the following sub-words
    word_ids = tok_sentence.word_ids()
    for word_index in range(len(word_ids)):
        if word_ids[word_index] == None:
            previous_token_id = word_ids[word_index]
        elif word_ids[word_index] == previous_token_id:
            previous_token_id = word_ids[word_index]
        else:
            predicted_labels.append( predicted_tokens_classes[ word_index ] )
            previous_token_id = word_ids[word_index]
    
    return predicted_labels
  
  # let us try with some example sentences here
def call_ner_model(sentence):
    #sentence = 'लगातार हमलावर हो रहे शिवपाल और राजभर को सपा की दो टूक, चिट्ठी जारी कर कहा- जहां जाना चाहें जा सकते हैं'
    sentence=sentence
    predicted_labels = get_predictions(sentence=sentence, 
                                    tokenizer=tokenizer,
                                    model=model
                                    )
    final_op=[]
    for index in range(len(sentence.split(' '))):
        final_op.append( sentence.split(' ')[index] + '\t' + predicted_labels[index] )
    return final_op
if __name__=="__main__":
    f=open("txt_files/bh-1","r")
    sent=f.readline()
    ner_op=call_ner_model(sent)
    f.close()
    #print(ner_op)
    f=open("txt_files/ner_output","w")
    for ner_val in ner_op:
        f.write(ner_val+"\n")
    f.close()
