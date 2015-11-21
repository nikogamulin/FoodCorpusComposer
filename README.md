#FoodCorpusComposer

##Main Objective
Generate corpus from cooking episodes subtitles

##Current Data
The subtitles files are included in data/subtitles folder. The current data does not suffice to create relevant word vector. Nevertheless you can run the project to generate test vectors and visualize them using t-SNE


##How to use the code
To visualize the vectors, just clone the repo and run python food_visualization.py

###Code description
####subtitles_corpus_composer.py contains the code for creating a corpus .txt file from subtitles files included in data/subtitles folder
####transcript_corpus_word2vec.py contains the code for learning word representation vectors from corpus file using gensim library
####food_visualization.py contains the demo code for visualizing food items vectors represented in 2D space using t_SNE


###Invitation to cooperation
The crucial part of AI task is to collect the learning data and this step turns out to be the main obstacle in a number of creative ideas. Anyone interested specifically in the field of food or generally in AI is welcome to participate in this project to create a corpus composer which could be useful for specific domains using TV series transcripts.

Consider food just as an example. Similarly, a good transcript parser could be used to generate a multilingual corpus which could be useful for translation, the dialogs from series could be used to emulate specific character responses to your SMS messages or emails etc.


