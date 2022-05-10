import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import contractions

from sklearn.base import BaseEstimator,TransformerMixin


class TextPreprocessing(BaseEstimator,TransformerMixin):
  def __init__(self,stopwords=stopwords.words('english')):
    self.stopwords = stopwords
    
  def fit(self,X,y=None):
    return self

  def to_lowercase(phrase):
    new_phrase = []
    for word in phrase:
        new_word = word.lower()
        new_phrase.append(new_word)
    return "".join(new_phrase)
  
  etapasCancer= {"stage 0":"stage0",
                 "stage i":"stage1",
                 "stage ii":"stage2",
                 "stage iii":"stage3",
                 "stage iv":"stage4"}
  def get_stages(phrase):
    words=phrase.split(" ")
    new_phrase = []
    prev_word=False

    for word in words:
      
      # Caso donde la palabra anterior es "stage"
      if prev_word:
        stage = "stage"+" "+word
        etapa=etapasCancer.get(stage)
        if etapa != None:
          # Si efectivamente es una etapa, añado esto a la palabra
          new_phrase.append(etapa+" ")
        prev_word=False
      else:
        if word != "stage":
          new_phrase.append(word)
          new_phrase.append(" ")
        else:
          prev_word=True
    return "".join(new_phrase)[:-1]

  def remove_punctuation(phrase):
    return phrase.translate(str.maketrans('','',string.punctuation))

  def remove_stopwords(phrase, stopwords=stopwords.words('english')):
    words=phrase.split(" ")
    new_phrase = []
    for word in words:
        if word not in stopwords:
            new_phrase.append(word)
            new_phrase.append(" ")
    return "".join(new_phrase)[:-1]

  def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

  def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

  def stem_and_lemmatize(words):
    words = lemmatize_verbs(words)
    words = stem_words(words)
    return words

    
  def transform(self,X,y=None):
    new_X_train = X.apply(contractions.fix) #Aplica la corrección de las contracciones
    new_X_train=new_X_train.apply(to_lowercase)
    new_X_train=new_X_train.apply(get_stages)
    new_X_train=new_X_train.apply(remove_punctuation)
    new_X_train=new_X_train.apply(remove_stopwords)
    new_X_train = new_X_train.apply(word_tokenize)
    new_X_train = new_X_train.apply(stem_and_lemmatize)
    new_X_train = new_X_train.apply(lambda x: ' '.join(map(str, x)))
    return new_X_train