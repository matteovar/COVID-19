import pandas as pd
import streamlit as st
from millify import millify as mf
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
from src.utils.cards import create_cards


def show_pandemic():

    st.markdown(
        """
    <h1 style='text-align: center; font-family: Arial, sans-serif;'>
        Pandemic Overview 
    </h1>
    <h2 style="color: #0638a1; text-align: center;">From December 2020 to May 2021<br   >
    </h2>
    """,
        unsafe_allow_html=True,
    )

    vaccinated["date"] = pd.to_datetime(vaccinated["date"])
    filtered_df = vaccinated[
        (vaccinated["date"] >= pd.to_datetime("2020-12-01"))
        & (vaccinated["date"] <= pd.to_datetime("2021-05-29"))
    ]

    cols = st.columns(4)

    with cols[0]:
        create_cards(
            "Total of Confirmed Cases",
            f'{mf(get_data_agg(df=confirmed, column_name="5/29/21", agg_type="sum"), precision=1)}',
        )

    with cols[1]:
        create_cards(
            "Total Deaths",
            f"{mf(get_data_agg(df=deaths, column_name="5/29/21", agg_type="sum"), precision=1)}",
        )

    with cols[2]:
        create_cards(
            "Total of Recovered",
            f'{mf(get_data_agg(df=recovered, column_name="5/29/21", agg_type="sum"), precision=1)}',
        )

    with cols[3]:
        create_cards(
            "Total Vaccinated",
            f"{mf(get_data_agg(filtered_df, column_name="daily_vaccinations", agg_type="sum"), precision=2)}",
        )

    total_confirmed = get_group_agg(
        df=df_confirmed, group_col="Dates", agg_col="Confirmed", agg_type="sum"
    )

    total_confirmed["Dates"] = pd.to_datetime(total_confirmed["Dates"])
    total_confirmed = total_confirmed.sort_values(by="Dates")

    # Aggregate deaths
    total_deaths = get_group_agg(
        df=df_deaths, group_col="Dates", agg_col="Deaths", agg_type="sum"
    )

    total_deaths["Dates"] = pd.to_datetime(total_deaths["Dates"])
    total_deaths = total_deaths.sort_values(by="Dates")

    merged_df = pd.merge(total_confirmed, total_deaths, on="Dates", how="inner")

    st.markdown(
        """ 
                #### Confirmed Cases compared to Deaths
                """
    )
    st.line_chart(
        merged_df,
        x="Dates",
        y=["Confirmed", "Deaths"],
        y_label="Person",
        x_label="Date",
    )


show_pandemic()
