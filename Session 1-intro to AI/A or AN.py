import nltk
# The noun should be in the capital letter
sentence = 'I Love owl and I Love dog and I Love Bird'
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(sentence)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
print(nouns)
for item in nouns:
    if item[0] in "aeiou":
        sentence=sentence.replace(item, 'An '+item)
    else:
        sentence=sentence.replace(item, 'A '+item)

print(sentence)