import streamlit as st
from src.main import df_confirmed, df_deaths, get_group_agg
from src.utils.merge import merge_data
from src.utils.plotyly_chats.maps import mapa


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
    nao_sei = get_group_agg(
        df=specific_date,
        group_col="Country/Region",
        agg_col="Confirmed",
        agg_type="sum",
    ).sort_values("Confirmed", ascending=False)

    specific_date_deaths = df_deaths[df_deaths["Dates"] == "5/29/21"]
    date_deaths = get_group_agg(
        df=specific_date_deaths,
        group_col="Country/Region",
        agg_col="Deaths",
        agg_type="sum",
    ).sort_values("Deaths", ascending=False)

    merge = merge_data(
        nao_sei, date_deaths, left_on="Country/Region", right_on="Country/Region"
    )

    mapa(
        df=merge,
        location="Country/Region",
        locationmode="country names",
        color="Deaths",
        hover_name="Country/Region",
        hover_data={"Confirmed": True},
        color_continuous_scale="blues",
        title="Top 10 Countries - Confirmed vs Deaths (05/29/21)",
    )


show_geo()
