import spacy

nlp = spacy.load('en_core_web_sm')

# doc = nlp("this is a test sentence")
# print([(w.text, w.pos_) for w in doc])



gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The horse raced past the barn fell.",
    "The man whistling tunes pianos.",
    "The cotton clothing is made of grows in Mississippi."
]


# Tokenize and perform entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.ent_type_, spacy.explain(token.ent_type_))

    else:
            print(token.text, token.pos_, token.dep_)



# Looked-Up Entity 1: FAC (Facility)
# Explanation: Buildings, airports, highways, bridges, etc.
# This entity makes sense in terms of the word/adjective "complex" in the sentence "The complex houses married and single soldiers and their families."

# Looked-Up Entity 2: ORG (Organization)
# Explanation: Companies, agencies, institutions, etc.
# This entity makes sense in terms of the word/noun "man" in the sentence "The man whistling tunes pianos."
