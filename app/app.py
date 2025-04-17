import pandas as pd
import streamlit as st

st.set_page_config(page_title="COVID-19", layout="wide")


def main():

    pages_1 = {
        "Pages": [
            st.Page("src/pages/Vision_on_Pandemic.py", title="Pandemic Overview"),
            st.Page("src/pages/Geographic_Analysis.py", title="Geographic Analysis"),
            st.Page("src/pages/Comparisons_between_Regions.py", title="Comparisons between Regions"),
            st.Page("src/pages/Mortality_and_Recovery.py", title="Mortality and Recovery")
            
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
