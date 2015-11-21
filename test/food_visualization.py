from gensim.models import word2vec
import gensim
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

from transcript_corpus_word2vec import getWord2Vec

ignoredIndices = []

model = getWord2Vec("./data/recipes_phrases.bin", True)
testTitles = ['lime', 'lemon', 'oranges', 'turkey', 'chicken', 'pasta', 'noodles', 'rice', 'beef']
testVectors = []
for i, title in enumerate(testTitles):
    vectorWords = title.split(', ')
    result = None
    for vec in vectorWords:
        vec = vec.replace(' ', '_')
        try:
            if result is None:
                result = model[vec]
            else:
                result += model[vec]
        except:
            print "vector for word %s not found" % vec
    if result is None:
        ignoredIndices.append(i)
        testVectors.append([0] * 50)
    else:
        testVectors.append(result.tolist())

testVectorsArray = np.array(testVectors)

modelTSNE = TSNE(n_components=2, random_state=0)
X_2d = modelTSNE.fit_transform(testVectorsArray)
for i in xrange(len(testTitles)):
    if not i in ignoredIndices:
        plt.text(X_2d[i,0], X_2d[i,1], testTitles[i], bbox=dict(facecolor='green', alpha=0.1))

plt.xlim((np.min(X_2d[:,0]), np.max(X_2d[:,0])))
plt.ylim((np.min(X_2d[:,1]), np.max(X_2d[:,1])))

plt.show()