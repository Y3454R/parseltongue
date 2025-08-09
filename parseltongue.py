import spacy
import pyphen

nlp = spacy.load("en_core_web_sm")
dic = pyphen.Pyphen(lang='en')

def bold_first_syllable_html(word):
    syllables = dic.inserted(word).split('-')
    if len(syllables) == 0:
        return word
    first = syllables[0]
    return f"<strong>{first}</strong>{word[len(first):]}"

def bionic_reading_html(text):
    doc = nlp(text)
    output_tokens = []

    for token in doc:
        if token.is_punct or token.is_space:
            output_tokens.append(token.text)
        else:
            output_tokens.append(bold_first_syllable_html(token.text))

    return ''.join(output_tokens)
