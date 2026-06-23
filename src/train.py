#Import libreries
import pandas as pd
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import preprocess


New_dataset = preprocess.New_dataset


#TfidfVectorizer
tfidf = TfidfVectorizer(max_features=3000,stop_words="english")
vectors = tfidf.fit_transform(New_dataset["tag"]).toarray()

#Cosine_Similarity
similarity = cosine_similarity(vectors)

#Recomendation Function
def recomender(movies):
   movies_index = New_dataset[New_dataset["title"] == movies].index[0]
   similarity_score = similarity[movies_index]
   movies_list = sorted(list(enumerate(similarity_score)),reverse=True,key=lambda x:x[1])[1:6]
   for i in movies_list:
      Movie_title = New_dataset.iloc[i[0]].title
      score = i[1]
      print(f" {Movie_title} --> {score}")


#Model save
base_dir = Path(__file__).resolve().parent.parent
model_dr = base_dir / "models"
model_dr.mkdir(exist_ok=True)

pickle.dump(New_dataset,open(model_dr / "movies.pkl","wb"))
pickle.dump(similarity,open(model_dr / "similarity.pkl","wb"))
print("model saved")