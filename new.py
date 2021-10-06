import spacy
nlp = spacy.load('en_core_web_sm')
sentence =  'how does the weather look tomorrow in chicago?'
doc = nlp(sentence)
c ={}
d=[]
for ent in doc.ents:
    print(ent.text+' '+ent.label_)
    if ent.label_ == 'GPE' or ent.label_ == 'DATE':
        c[ent.label_] = ent.text
        d.insert(0,ent.text)
print(c,d)
