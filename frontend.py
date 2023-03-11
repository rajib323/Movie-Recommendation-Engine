import streamlit as st
import pickle
import webbrowser
from PIL import Image

def callmehero(text):
    mv_name=[]
    index=movies[movies['original_title']==text].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x:x[1])
    for i in distance[1:11]:
        mv_name.append(movies.iloc[i[0]])
    return mv_name


movies = pickle.load(open('./movie_list.pkl','rb'))
similarity = pickle.load(open('./similarity.pkl','rb'))
movie_list = movies['original_title']



st.title("Movie Recommender System")
if st.button("Git @adi323"):
    webbrowser.open_new_tab("https://github.com/adi323")

selected_movie = st.selectbox(
    label="Type or select a movie from the dropdown",
    options=movie_list,
    label_visibility='visible'
)
image = Image.open('./img.webp')
if st.button("Show Recommendation"):
    mv_name=callmehero(selected_movie)
    st.header('Recommendation for {}'.format(selected_movie))
    for i in mv_name:
        col1,col2=st.columns(2)
        with col1:
            st.image('https://image.tmdb.org/t/p/w500{}'.format(i['poster_path']))
        with col2:
            st.header(i['original_title'])
            st.markdown('#')
            st.text('Language : {}'.format(i['spoken_languages']))
            st.text('Duration : {} mins'.format(i['runtime']))
            st.markdown('#')
            st.text('Release : {}'.format(i['release_date']))
            st.text('Voting Average : {}⭐'.format(i['vote_average']))
            with st.expander("Description"):
                st.write(i['overview'])



