import gensim,nltk
import string
from gensim.models.phrases import Phrases
import subtitles_corpus_composer

def getWord2Vec(modelFile, useExistingCorpus = False):
    if useExistingCorpus:
        return gensim.models.Word2Vec.load(modelFile)

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    corpus = subtitles_corpus_composer.getCorpus(useExistingCorpus)
    sents = tokenizer.tokenize(corpus)
    tokenized = []
    for s in sents:
        tokens = nltk.word_tokenize(s.strip(string.punctuation).replace("\"", ""))
        tokenized.append(tokens)

    bigramTransformed = Phrases(tokenized)
    modelCom = gensim.models.Word2Vec(bigramTransformed[tokenized], size=50)

    modelCom.init_sims(replace=True)
    modelCom.save(modelFile)
    #in case you want to save the non-binary format, uncomment the following line
    #modelCom.save_word2vec_format("./data/recipes_sw2v", binary=False)

    return modelCom

def queryModels(q, model):
    c =  model.most_similar(positive=[(q)], topn=20)
    for i in range(1,20):
        print c[i][0]
    print '----------'

if __name__ == "__main__":
    modelCom = getWord2Vec("./data/recipes_vec.bin")

    queryModels('orange', modelCom)
    queryModels('lemon', modelCom)
    queryModels('butter', modelCom)
    queryModels('milk', modelCom)