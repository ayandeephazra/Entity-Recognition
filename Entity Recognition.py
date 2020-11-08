import nltk

#getting unique tags and making a string of the data elements from train.txt
fhand = open('train.txt', 'r', encoding="utf8")
tags_from_train = []

for line in fhand:
    if line == "\n":
        continue
    else:
        pair = line.split()
        if len(pair) == 0 :
            continue
        word = pair[0]
        tag = pair[1]
        if word=='.' :
            continue
        if tag !='0':
            #unique tags
            if tag not in tags_from_train:
                tags_from_train.append(tag)

#placing test data in a string
fhand = open('test.txt', 'r', encoding="utf8")
sentence = []
test = []
data = ""
for line in fhand:
    pair = line.split()
    if len(pair) == 0 :
        continue
    word = pair[0]
    if word!='.' :
        data = data + word + " \n"
        sentence.append(word)
    else :
        data = data + word + " \n"
        sentence.append(word)
        test.append(sentence)
        sentence = []   

words = nltk.word_tokenize(data)
pos_tags = nltk.pos_tag(words)
chunks = nltk.ne_chunk(pos_tags, binary=False) 

entities =[]
labels =[]
for chunk in chunks:
    if hasattr(chunk,'label'):
        entities.append(' '.join(c[0] for c in chunk))
        labels.append(chunk.label())
    else:
        entities.append(chunk[0])
        labels.append(chunk[1])
        
f = open("test_results.txt", 'a', encoding="utf8")

for i in range(len(entities)):
    f.write(entities[i])
    f.write("\t")
    
    if labels[i]=="ORGANIZATION":
        f.write("B-corporation")
    elif labels[i]=="ORGANIZATION" and labels[i-1]=="ORGANIZATION":
        f.write("I-corporation")
    elif labels[i]=="PERSON":
        f.write("B-person")
    elif labels[i]=="PERSON" and labels[i-1]=="PERSON":
        f.write("I-person")
    elif labels[i]=="GPE":
        f.write("B-location")
    elif labels[i]=="GPE" and labels[i-1]=="GPE":
        f.write("I-location")
    else:
        f.write("0")
    f.write("\n")
    
