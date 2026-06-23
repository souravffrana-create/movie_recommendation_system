#Import libreries
from pathlib import Path 
import pandas as pd
import ast


#Load-Data
base_dir = Path(__file__).resolve().parent.parent
data_path_movies = base_dir / "data"/ "tmdb_5000_movies.csv"
data_path_credits = base_dir / "data"/ "tmdb_5000_credits.csv"
movies = pd.read_csv(data_path_movies)
credits = pd.read_csv(data_path_credits)

#merge data
dataset = movies.merge(credits,on='title')


#----------------------------------------------------- Data-Preprocessing ---------------------------------------

dataset = dataset[["id","title","overview","genres","keywords","cast","crew"]]
dataset = dataset.dropna()

#Helper functions
def convert(data):
    l = []
    for i in ast.literal_eval(data):
      l.append(i.get("name"))
    return l

#fetch main cast
def transform(obj):
   l = []
   counter = 0
   for i in ast.literal_eval(obj):
      if counter!= 3:
         l.append(i.get("name"))
         counter+=1
      else:
         break
   return l

#fetch director
def fetch_director(data):
   L = []
   for i in ast.literal_eval(data):
      if i["job"] == "Director":
         L.append(i.get("name"))
         break
   return L

#Genres column
dataset["genres"] = dataset["genres"].apply(convert)
dataset["genres"] = dataset["genres"].apply(lambda x:[i.replace(" ","") for i in x])

#keywords column
dataset["keywords"] = dataset["keywords"].apply(convert)
dataset["keywords"] = dataset["keywords"].apply(lambda x:[i.replace(" ","") for i in x])

#cast column
dataset["cast"] = dataset["cast"].apply(transform)
dataset["cast"] = dataset["cast"].apply(lambda x:[i.replace(" ","") for i in x])

#crew column
dataset["crew"] = dataset["crew"].apply(fetch_director)
dataset["crew"] = dataset["crew"].apply(lambda x:[i.replace(" ","") for i in x])

#overview
dataset["overview"] = dataset["overview"].apply(lambda x:x.split())

#tag creation
dataset["tag"] = dataset["overview"] + dataset["genres"] + dataset["keywords"] + dataset["cast"] + dataset["crew"]


#New dataframe
New_dataset = dataset[["id","title","tag"]]
New_dataset["tag"] = New_dataset["tag"].apply(lambda x: " ".join(x))
New_dataset = New_dataset.drop_duplicates(subset="title",keep='first')
New_dataset = New_dataset.reset_index(drop=True)

if __name__ == "__main__":
   pass