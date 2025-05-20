import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/data.csv", sep=';')
result = pd.read_csv("data/result.csv")

merged = result.copy()

st.title("KMeans Clustering Dashboard")
st.markdown("Prototype untuk eksplorasi dan visualisasi hasil clustering menggunakan algoritma K-Means.")

if st.checkbox("Tampilkan Data Awal"):
    st.write(data.head())

if st.checkbox("Tampilkan Hasil Clustering"):
    st.write(merged.head())

st.subheader("Distribusi Cluster")
cluster_count = merged['student_segment'].value_counts().sort_index()
st.bar_chart(cluster_count)

st.subheader("Visualisasi Scatter Plot")
col_mapping = {
    "Rata-rata Nilai": "avg_grade",
    "Tingkat Persetujuan": "total_approval_rate",
    "Skor Pendidikan Orang Tua": "parents_education_score"
}

available_cols = {display: col for display, col in col_mapping.items() if col in merged.columns}

if len(available_cols) == 0:
    st.error("Tidak ada kolom yang tersedia untuk visualisasi.")
else:
    x_display = st.selectbox("Pilih X-axis", list(available_cols.keys()), index=0)
    y_default_index = 1 if len(available_cols) > 1 else 0
    y_display = st.selectbox("Pilih Y-axis", list(available_cols.keys()), index=y_default_index)

    x_axis = available_cols[x_display]
    y_axis = available_cols[y_display]

    fig, ax = plt.subplots()
    sns.scatterplot(data=merged, x=x_axis, y=y_axis, hue='student_segment', palette='Set1', ax=ax)
    st.pyplot(fig)
