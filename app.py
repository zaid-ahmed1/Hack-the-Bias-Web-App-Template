import streamlit as st
import pandas as pd

# Read the data
df = pd.read_csv('imdb_top_1000.csv')

# Set page title
st.title('Movie Recommendation System')

# Create sidebar filters
st.sidebar.header('Filter Movies')

# Genre filter
all_genres = [genre.strip() for genres in df['Genre'].str.split(',') for genre in genres]
unique_genres = sorted(list(set(all_genres)))
selected_genre = st.sidebar.selectbox('Select Genre', unique_genres)

# Rating filter
rating_range = st.sidebar.slider(
    'Select IMDB Rating Range',
    min_value=float(df['IMDB_Rating'].min()),
    max_value=float(df['IMDB_Rating'].max()),
    value=(float(df['IMDB_Rating'].min()), float(df['IMDB_Rating'].max()))
)

# Filter the dataframe
filtered_df = df[
    (df['IMDB_Rating'].between(rating_range[0], rating_range[1])) &
    (df['Genre'].str.contains(selected_genre, case=False))
]

# Display results
st.subheader(f'Found {len(filtered_df)} movies matching your criteria')

# Show movies in a simpler format
for idx, row in filtered_df.iterrows():
    st.markdown("---")  # Add a separator between movies
    
    # Movie title and rating in a header
    st.header(f"{row['Series_Title']} ({row['Released_Year']})")
    st.markdown(f"⭐ **Rating:** {row['IMDB_Rating']}")
    
    # Two columns: Image and Basic Info
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(row['Poster_Link'], width=200)
    
    with col2:
        st.markdown(f"🎬 **Genre:** {row['Genre']}")
        st.markdown(f"👨‍💼 **Director:** {row['Director']}")
        st.markdown(f"⏱️ **Runtime:** {row['Runtime']}")




