from pathlib import Path 
import pickle


#Load models
Base_dir = Path(__file__).resolve().parent.parent
Model_dir = Base_dir / "models"

movies     = pickle.load(open(Model_dir / "movies.pkl",     "rb"))
similarity = pickle.load(open(Model_dir / "similarity.pkl", "rb"))

def Recommendation(input):
    movie_idx = movies[movies["title"]==input].index[0]
    score = similarity[movie_idx]
    movies_list = sorted(enumerate(score),reverse=True,key=lambda x:x[1])[1:6]
    recommed = []
    for i in movies_list:
        recommed.append(movies.iloc[i[0]].title)
            
    return recommed

