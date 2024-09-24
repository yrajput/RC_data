import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and file upload
st.title("Event Registration Data Analyzer")
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show dataframe preview
    st.write("Here is a preview of the dataset:")
    st.dataframe(df.head())

    # Gender Distribution
    gender_counts = df['Gender of Sproutz Attendee'].value_counts()
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    gender_counts.plot(kind='bar', ax=ax)
    st.pyplot(fig)
