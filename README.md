#FoodCorpusComposer

##Main Objective
Generate corpus from cooking episodes subtitles

##Current Data
The subtitles files are included in data/subtitles folder. The current data does not suffice to create relevant word vector. Nevertheless you can run the project to generate test vectors and visualize them using t-SNE


##How to use the code
To visualize the vectors, just clone the repo and run ```python food_visualization.py```

###Code description
```subtitles_corpus_composer.py``` contains the code for creating a corpus .txt file from subtitles files included in data/subtitles folder

```transcript_corpus_word2vec.py``` contains the code for learning word representation vectors from corpus file using gensim library; examples of similarity calculation for word orange:
```
modelCom = getWord2Vec("./data/recipes_vec.bin")
>>>queryModels('orange', modelCom)
with
oil
day
flavour
hear
pepper
-just
top
salt
will
```

```test/food_visualization.py``` contains the demo code for visualizing food items vectors represented in 2D space using t_SNE;example visualization for words:

![Alt text](https://github.com/nikogamulin/FoodCorpusComposer/blob/master/visualization_example.png "Visualization of word vectors using t-SNE")

```test/lstm_text_generation.py``` is an example of LSTM recurrent NN from keras library which learns to generate text from corpus; examples of generated text:

Iteration 1:
```----- Generating with seed: "oking  i can't think"
oking  i can't think ore rt rto or rnr ee rre rt tne rrr rr on tre rot  oee rte rr oe rrrrl ee n ote  orte  torn oe trre t ore rrr tt rre rte ror trr on te te rrrt te nr oe rer rrr ter rrre rnr er nrrt ort o rt ree tr to tre ert re ner orr ryo rr on tt ite rrnn rrt nrr trr rre rt rr et rne rtr ot ror rtr oe rr aro  ote tr on otr ntr ta rtt e oor  tth rte rertr rrn rn orr on ry tse ortr rt ot ror rrrl ne rrr rtt rrer```

Iteration 23:
```----- Generating with seed: "they're absolutely f"
they're absolutely fantastic serad to do is that they really - so what i deen things like that  and i think that and that i've got this preat of chucken -  you can use that comeanous cos it us  i just think it all togst they really flavours of alave olive oil and i just werl chiffer  and then like that -  the gerl come of chocolate thing cold in and just star it all togsthings llave that in the over - lovely.  that t```

Iteration 59:
```----- Generating with seed: "m from the supermark"
m from the supermarket and the engh the skis  the make some crample to make sore very cricky and stirf -  and bust of salt of the poplice in there.  so i'll see how a bit more haver  and it's like beired ticked i've fold be kind of salt  it to tastes now and thi```

Obviously there isn't enough data been collected so far from the subtitles to imitate Jamie Oliver although the recurrent network learned to compose sentences, which mention food.

##Using the model trained on larger corpus

In the repository there is a word2vec file recipes_phrases.bin. It is much larger than the model trained from subtitles.
When looking for words most similar to lemon, the model outputs the following:

```
>>> queryModels('orange', modelCom)
lime
lemon
peach
oranges
tangerine
citrus
pineapple
mandarin_orange
zested
kiwi
rind
pear
apple
Zest
mango
beet
strawberries
lemons
strawberry
```

The model trained on larger corpus gives better results.

###Invitation to cooperation
The crucial part of AI task is to collect the learning data and this step turns out to be the main obstacle in a number of creative ideas. Anyone interested specifically in the field of food or generally in AI is welcome to participate in this project to create a corpus composer which could be useful for specific domains using TV series transcripts.

Consider food just as an example. Similarly, a good transcript parser could be used to generate a multilingual corpus which could be useful for translation, the dialogs from series could be used to emulate specific character responses to your SMS messages or emails etc.

####Main objectives:
* Create crawlers to simplify the retrieval of transcript/subtitles files
* Create mechanism to label the trascript dialogs with speaking characters
* Create a generic solution which could be applied to create a corpus for arbitrary domain

