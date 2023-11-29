import spacy
nlp_sm = spacy.load("en_core_web_sm")
nlp_md = spacy.load("en_core_web_md")

print("___________extract 1.1_________________")
tokens = nlp_md('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))
# Apart from the exact matches its interesting to see the apple-banana combo is the highest and highe than a cat-monkey combo.I thought the comparison of fruit-fruit and animal-animal would be the same.but seemingly there are more charecteristics that go into seperating them.


print("___________extract 1.2_________________")
tokens = nlp_sm('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# apple-cat and apple-monkey have an interesting hogh realtionship I did not excpect,wonder why.
# the rest of the compariosn have a similar to nlp_md function but all lower actual numbers.

print("__________extract 2.1 _________________")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp_md(sentence_to_compare)
for sentence in sentences:
      similarity = nlp_md(sentence).similarity(model_sentence)
      print(sentence + "-" + str(similarity))
# nlp_md recognises the dog and cat are animals but tnot the same therefore the similarity number decrease as compared to the sentence refering to a car only.

print("__________extract 2.2 _________________")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp_sm(sentence_to_compare)
for sentence in sentences:
      similarity = nlp_sm(sentence).similarity(model_sentence)
      print(sentence + "-" + str(similarity))
# Realtionship stregnths are similar to nlp_md but the numbers are lower.
# Ran the above comaprions on the example file and the overall comments remain the sam on nlp_md vs nlp_sm

print("___________extract 3.1 - own example_________________")
tokens = nlp_md('PABALELO MOEKETSI BANKER FARMER')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# Interesting it matches banker and farmer with a strong similarity - indicating it recoginses those titles as professions
# It does not recoginise a relationship between uncommon names of people.