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
        if token.is_space:
            continue  # spaces handled by whitespace_
        elif token.is_punct:
            output_tokens.append(token.text + token.whitespace_)
        else:
            emphasized = bold_first_syllable_html(token.text)
            output_tokens.append(emphasized + token.whitespace_)

    return ''.join(output_tokens)
