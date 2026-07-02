import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# ----------------------------- Page Config ----------------------------- #
st.set_page_config(
    page_title="CineMatch Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------- Data ----------------------------- #
movie_dict = pickle.load(open("./notebook/movies.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("./notebook/similarity.pkl", "rb"))


# ----------------------------- Poster Helpers ----------------------------- #
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, API_KEY)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


@st.cache_data(show_spinner=False)
def fetch_background_posters():
    """Fetch popular movie posters to build the faded backdrop collage."""
    posters = []
    try:
        for page in (1, 2, 3):
            url = "https://api.themoviedb.org/3/movie/popular?api_key={}&language=en-US&page={}".format(API_KEY, page)
            data = requests.get(url, timeout=8).json()
            for item in data.get('results', []):
                if item.get('poster_path'):
                    posters.append("https://image.tmdb.org/t/p/w342" + item['poster_path'])
    except Exception:
        pass
    return posters


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# ----------------------------- Background Collage ----------------------------- #
background_posters = fetch_background_posters()
collage_html = "".join(
    '<img src="{}" loading="lazy">'.format(p) for p in background_posters[:60]
)

# ----------------------------- Styling ----------------------------- #
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
        html, body { background-color: #000000; }
        .stApp { background-color: transparent; }

        /* Poster collage sitting BEHIND all content */
        .bg-collage {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: -2;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            grid-auto-rows: minmax(150px, 1fr);
            gap: 4px;
            overflow: hidden;
        }
        .bg-collage img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 1.0;
        }
        .bg-overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: -1;
            background:
                radial-gradient(circle at 50% 12%, rgba(0,0,0,0.30) 0%, rgba(0,0,0,0.82) 70%),
                linear-gradient(to bottom, rgba(0,0,0,0.70), rgba(0,0,0,0.95));
        }

        .block-container {
            position: relative;
            z-index: 1;
            padding-top: 2.5rem;
            max-width: 1200px;
        }

        /* Hero */
        .hero { text-align: center; padding: 2.5rem 1rem 1rem 1rem; }
        .hero-title {
            font-size: 3.8rem;
            font-weight: 800;
            letter-spacing: -2px;
            color: #ffffff;
            margin: 0;
            text-shadow: 0 4px 30px rgba(0,0,0,0.9);
        }
        .hero-title span { color: #e50914; }
        .hero-subtitle {
            font-size: 1.15rem;
            color: #e2e2e2;
            font-weight: 300;
            margin-top: 0.7rem;
            max-width: 640px;
            margin-left: auto; margin-right: auto;
            text-shadow: 0 2px 12px rgba(0,0,0,0.9);
        }

        /* Selectbox */
        div[data-baseweb="select"] > div {
            background-color: rgba(25,25,25,0.92) !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            color: #fff !important;
        }
        .stSelectbox label {
            color: #f0f0f0 !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
        }

        /* Section heading */
        .section-heading {
            font-size: 1.5rem;
            font-weight: 600;
            color: #ffffff;
            margin: 2.5rem 0 1.2rem 0;
            padding-left: 0.6rem;
            border-left: 4px solid #e50914;
        }

        /* Cards */
        .movie-card { text-align: center; transition: transform 0.25s ease; }
        .movie-card:hover { transform: scale(1.06); }
        .movie-card img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.7);
        }
        .movie-title {
            font-size: 0.9rem;
            font-weight: 500;
            color: #f2f2f2;
            margin-top: 0.7rem;
            line-height: 1.25rem;
            min-height: 2.5rem;
        }

        /* Button */
        div.stButton { text-align: center; }
        div.stButton > button {
            background-color: #e50914;
            color: #ffffff;
            border: none;
            border-radius: 6px;
            padding: 0.6rem 2.6rem;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 0.8rem;
            transition: all 0.2s ease;
        }
        div.stButton > button:hover {
            background-color: #f6121d;
            color: #ffffff;
            transform: scale(1.04);
        }

        /* Footer */
        .footer {
            margin-top: 4rem;
            padding: 2.2rem 1rem 1.5rem 1rem;
            border-top: 1px solid rgba(255,255,255,0.12);
            text-align: center;
            color: #9aa0a6;
        }
        .footer-title { font-size: 1.3rem; font-weight: 700; color: #ffffff; }
        .footer-title span { color: #e50914; }
        .footer-sub { font-size: 0.9rem; margin-top: 0.4rem; }
        .footer-sub b { color: #e5e5e5; font-weight: 600; }
        .footer-meta { font-size: 0.78rem; color: #6b7075; margin-top: 0.8rem; }
        .footer-meta a { color: #9aa0a6; text-decoration: none; }
        .footer-meta a:hover { color: #e50914; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------- Background Layers ----------------------------- #
st.markdown(
    '<div class="bg-collage">{}</div><div class="bg-overlay"></div>'.format(collage_html),
    unsafe_allow_html=True,
)

# ----------------------------- Hero ----------------------------- #
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">Cine<span>Match</span></div>
        <div class="hero-subtitle">
            Your next favorite film is one click away. Pick a movie you love and let
            CineMatch surface titles with the same vibe.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------- Controls ----------------------------- #
selected_movie = st.selectbox(
    "Select a movie name",
    movies['title'].values
)

show = st.button('Show Recommendation')

# ----------------------------- Recommendations ----------------------------- #
if show:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    st.markdown('<div class="section-heading">Recommended for you</div>', unsafe_allow_html=True)
    columns = st.columns(5, gap="medium")

    for col, name, poster in zip(columns, recommended_movie_names, recommended_movie_posters):
        with col:
            st.markdown(
                """
                <div class="movie-card">
                    <img src="{}">
                    <div class="movie-title">{}</div>
                </div>
                """.format(poster, name),
                unsafe_allow_html=True,
            )

# ----------------------------- Footer ----------------------------- #
st.markdown(
    """
    <div class="footer">
        <div class="footer-title">Cine<span>Match</span> Movie Recommender</div>
        <div class="footer-sub">Built by <b>Salman Khan</b></div>
        <div class="footer-meta">
            Content-based recommendation engine &nbsp;•&nbsp; Powered by
            <a href="https://www.themoviedb.org/" target="_blank">TMDB</a>
            &amp; Streamlit &nbsp;•&nbsp; Dataset: TMDB 5000 Movies<br>
            © 2026 CineMatch. For educational purposes. This product uses the TMDB API
            but is not endorsed or certified by TMDB.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
