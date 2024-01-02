import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load data
file_path = "datasets_bukuPengembanganDiri.csv"
df = pd.read_csv(file_path)

# Inisialisasi stop words bahasa Indonesia
stop_words = set(stopwords.words('indonesian'))

# Salin DataFrame untuk menyimpan sinopsis asli
df_original = df.copy()

# Proses teks
ps = PorterStemmer()

def preprocess_text(text):
    # Tokenisasi dan stemming menggunakan NLTK
    tokens = word_tokenize(text)
    stemmed_tokens = [ps.stem(token) for token in tokens if token.lower() not in stop_words]
    return ' '.join(stemmed_tokens)

# Preprocessing sinopsis
df['sinopsis'] = df['sinopsis'].apply(preprocess_text)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['sinopsis'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Fungsi pencarian
def search_books(query, df, vectorizer, cosine_sim):
    # Preprocessing query
    query = preprocess_text(query)
    
    # TF-IDF untuk query
    query_vector = vectorizer.transform([query])
    
    # Cosine similarity antara query dan dokumen
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Indexing, ranking, dan filter similarity > 0
    results = pd.DataFrame({'judul': df['judul'], 'penulis': df['penulis'], 'sinopsis': df_original['sinopsis'], 'similarity': similarities})
    results = results[results['similarity'] > 0]
    
    if results.empty:
        return "Tidak ada hasil yang ditemukan untuk '{}'".format(query)
    
    results = results.sort_values(by='similarity', ascending=False)
    
    return results

# UI menggunakan Streamlit
def main():
    st.title("Pencarian Buku Pengembangan Diri")
    
    # Input query dari pengguna
    query = st.text_input("Masukkan kata kunci pencarian:")
    
    if st.button("Cari"):
        # Lakukan pencarian
        search_results = search_books(query, df, vectorizer, cosine_sim)
        
        # Tampilkan hasil
        if isinstance(search_results, str):
            st.warning(search_results)
        else:
            st.success("Hasil pencarian untuk '{}'".format(query))
            st.table(search_results[['judul', 'penulis', 'sinopsis']])

