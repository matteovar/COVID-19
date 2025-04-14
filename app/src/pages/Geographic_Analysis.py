import pandas as pd
import streamlit as st
from src.main import (
    confirmed,
    deaths,
    df_confirmed,
    df_deaths,
    get_data_agg,
    get_group_agg,
    recovered,
    vaccinated,
)
from src.utils.plotyly_chats.bar_chart import bar


def show_geo():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Geographical Distribution of the Pandemic
        </h1>
        """,
        unsafe_allow_html=True,
    )

    specific_date = df_confirmed[df_confirmed["Dates"] == "5/29/21"]
    nao_sei = (
        get_group_agg(
            df=specific_date,
            group_col="Country/Region",
            agg_col="Confirmed",
            agg_type="sum",
        )
        .sort_values("Confirmed", ascending=False)
        .head(10)
    )

    
    specific_date_deaths = df_deaths[df_deaths["Dates"] == "5/29/21"]
    date_deaths = (
        get_group_agg(
            df=specific_date_deaths,
            group_col="Country/Region",
            agg_col="Deaths",
            agg_type="sum",
        ).sort_values("Deaths", ascending=False)
        .head(10)
    )

    merge = nao_sei.merge(date_deaths, left_on='Country/Region', right_on="Country/Region")
    bar(df=merge, x = "Country/Region", y="Deaths", color="Confirmed",x_label="Country", y_label="Deaths", title="Top 10 Countries - Confirmed vs Deaths (05/29/21)")

show_geo()
