# Garden Path Sentences

This Python program demonstrates the use of spaCy library to tokenize sentences and perform entity recognition on garden path sentences.

## Installation

* Make sure you have Python installed on your machine (version 3.6 or above).

* Install the spaCy library by running the following command:

    pip install spacy

* Download the English language model by running the following command:

    python -m spacy download en_core_web_sm

## Usage

* Import the spaCy library in your Python script:

    import spacy

* Load the English language model:

    nlp = spacy.load('en_core_web_sm')

* Define the garden path sentences as a list:

    gardenpathSentences = [    "The old man the boat.",    "The complex houses married and single soldiers and their families.",    "The horse raced past the barn fell.",    "The man whistling tunes pianos.",    "The cotton clothing is made of grows in Mississippi."]

* Tokenize and perform entity recognition for each sentence:

    for sentence in gardenpathSentences:
        doc = nlp(sentence)
        for token in doc:
            print(token.text, token.pos_, token.dep_, token.ent_type_, spacy.explain(token.ent_type_))
        else:
            print(token.text, token.pos_, token.dep_)

* Interpret the results to understand the entities recognized by spaCy.

## Entity Recognition

The program performs entity recognition using the spaCy library. For each token in a sentence, the program outputs its text, part-of-speech tag, dependency label, entity type, and an explanation of the entity type if available.

Here are the looked-up entities for two sentences:

 *  Looked-Up Entity 1: FAC (Facility)
    Explanation: Buildings, airports, highways, bridges, etc.
    This entity makes sense in terms of the word/adjective "complex" in the sentence "The complex houses married and single soldiers and their families."

 *  Looked-Up Entity 2: ORG (Organization)
    Explanation: Companies, agencies, institutions, etc.
    This entity makes sense in terms of the word/noun "man" in the sentence "The man whistling tunes pianos."

## Credits

This program was created by Your Name. Feel free to modify and use it according to your needs.

If you have any questions or suggestions, please feel free to reach out to Your Email Address.