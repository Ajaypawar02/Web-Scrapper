import streamlit as st
import pandas as pd
import sys
import base64
sys.path.append("/home/ajay/Listed_2/src")
from scrapper import Scrapper_Web

# Function to process the keyword and return the top-k results
def process_keyword(keyword, top_k):
    # Add your code to process the keyword and generate the desired output
    # Return the top-k results
    
    # Example placeholder
    results = [f"Result {i}" for i in range(1, top_k+1)]
    return results

# Streamlit app
def main():
    # Set app title
    st.title("Web Scrapper")

    # User input - Keyword
    keyword = st.text_input("Enter a keyword:")

    # User input - Top-k number
    top_k = st.text_input("Select the number of top results:")

    # Process the keyword and display the results
    if st.button("Process"):
        if keyword:
            with st.spinner("Processing..."):
                results = Scrapper_Web(int(top_k),keyword)
                # st.write(f"Top {top_k} results for '{keyword}':")
                # for i, result in enumerate(results):
                #     st.write(f"{i+1}. {result}")

                df = results.get_url()

                # Create a DataFrame from the results
                # df = pd.DataFrame({'Results': results})
                st.write(df)

                # # Download the DataFrame as a CSV file
                csv = df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="results.csv">Download CSV</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.write("Please enter a keyword.")

# Run the app
if __name__ == "__main__":
    main()
