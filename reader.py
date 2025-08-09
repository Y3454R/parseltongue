import spacy
import pyphen

nlp = spacy.load("en_core_web_sm")
dic = pyphen.Pyphen(lang='en')

def bold_first_syllable(word):
    syllables = dic.inserted(word).split('-')
    if len(syllables) == 0:
        return word
    first = syllables[0]
    return f"**{first}**{word[len(first):]}"

def bionic_reading(text):
    doc = nlp(text)
    output_tokens = []

    for token in doc:
        if token.is_punct or token.is_space:
            output_tokens.append(token.text)
        else:
            if token.pos_ in {'NOUN', 'VERB', 'ADJ'}:
                syllables = dic.inserted(token.text).split('-')
                if len(syllables) > 1:
                    first_two = ''.join(syllables[:2])
                    bolded = f"**{first_two}**{token.text[len(first_two):]}"
                else:
                    bolded = bold_first_syllable(token.text)
                output_tokens.append(bolded)
            else:
                output_tokens.append(bold_first_syllable(token.text))

        # preserve whitespace after token
        if token.whitespace_:
            output_tokens.append(token.whitespace_)

    return ''.join(output_tokens)


sample_text = "Bionic reading helps you read faster by guiding your eyes through important parts."
print(bionic_reading(sample_text))
