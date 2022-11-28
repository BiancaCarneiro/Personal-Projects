import nltk
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import tqdm
from pdfminer.high_level import extract_text
from sklearn.decomposition import PCA

def get_text(file_path, encoding='utf-8'): # OK
    if '.pdf' in file_path:
            text = extract_text(file_path, codec=encoding)
    else:
        with open(file_path, 'r', encoding=encoding) as f:
            text = f.read()
            f.close()
    return text


def lsi(document_folder, language='portuguese'):
    stopwords = nltk.corpus.stopwords.words(language)
    word_document = {}
    print('Creating document embeddings')
    for i, file in enumerate(tqdm.tqdm(os.listdir(document_folder))):
        file_path = f'{document_folder}/{file}'
        tokenized_words = nltk.tokenize.word_tokenize(get_text(file_path).lower(), language=language)
        tokenized_words = [word for word in tokenized_words if word not in stopwords and len(word)>3]
        for word in tokenized_words:
            if word in word_document:
                word_document[word].append(i)
            else:
                word_document[word]= [i]
    term_document_matrix = np.zeros((len(word_document),len(os.listdir(document_folder))))
    for i, key in enumerate(word_document.keys()):
        for j in word_document[key]:
            term_document_matrix[i,j]=1
          
    U, S, Vt = np.linalg.svd(term_document_matrix)
    word_embeddings = U
    document_embeddings = Vt.T
    return word_embeddings, list(word_document.keys()), document_embeddings

def plot_word_embeddings(words, embeddigns):
    pca = PCA(n_components=2)
    embed_2d = pca.fit_transform(embeddigns)
    fig, ax = plt.subplots()
    ax.scatter(embed_2d[:, 0], embed_2d[:, 1])

    for i, txt in enumerate(words):
        ax.annotate(txt, (embed_2d[i][0], embed_2d[i][1]))
    plt.show()
    return 0

if __name__ == '__main__':
    word_embeddinds, words, document_embeddinds = lsi('documents')
    plot_word_embeddings(words[-15:], word_embeddinds[-15:])
    plot_word_embeddings(range(len(document_embeddinds)), document_embeddinds)