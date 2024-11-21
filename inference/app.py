import streamlit as st
import pandas as pd
from ai_chat import AIChatGenerator
from apply_sequence import apply_transformations

st.title("Data Transformation App")
st.markdown("Please upload your CSV file and provide a query to transform your data.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.subheader("Original DataFrame")
    st.dataframe(dataframe)

    user_query = st.text_input("Enter your transformation query (e.g., Please filter rows where age > 30 and select name and age)")

    if st.button("Apply Transformations"):
        if user_query:
            try:
                api_key = st.secrets["OPENAI_API_KEY"]
                ai_chat = AIChatGenerator(api_key=api_key)

                transformations = ai_chat.generate_transformations(user_query)
                st.subheader("Generated Transformations")
                st.json(transformations)

                transformed_df = apply_transformations(dataframe, transformations)
                st.subheader("Transformed DataFrame")
                st.dataframe(transformed_df)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a transformation query.")

