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
from src.utils.plotyly_chats.line_chart import line


def format_value(value, precision=1):
    return mf(value, precision=precision)


def display_title():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Pandemic Overview 
        </h1>
        <h2 style="color: #0638a1; text-align: center;">
            From December 2020 to May 2021
        </h2>
        """,
        unsafe_allow_html=True,
    )


def get_vaccinated_filtered_df():
    vaccinated["date"] = pd.to_datetime(vaccinated["date"], format="%Y-%m-%d")
    return vaccinated[
        (vaccinated["date"] >= pd.to_datetime("2020-12-01"))
        & (vaccinated["date"] <= pd.to_datetime("2021-05-29"))
    ]


def display_summary_cards(filtered_df):
    cols = st.columns(4)

    with cols[0]:
        total_confirmed = get_data_agg(
            df=confirmed, column_name="5/29/21", agg_type="sum"
        )
        create_cards("Total of Confirmed Cases", format_value(total_confirmed))

    with cols[1]:
        total_death = get_data_agg(df=deaths, column_name="5/29/21", agg_type="sum")
        create_cards("Total Deaths", format_value(total_death))

    with cols[2]:
        total_recovered = get_data_agg(
            df=recovered, column_name="5/29/21", agg_type="sum"
        )
        create_cards("Total of Recovered", format_value(total_recovered))

    with cols[3]:
        total_vaccinated = get_data_agg(
            filtered_df, column_name="daily_vaccinations", agg_type="sum"
        )
        create_cards("Total Vaccinated", format_value(total_vaccinated, precision=2))


def display_line_chart():
    total_confirmed = get_group_agg(
        df=df_confirmed, group_col="Dates", agg_col="Confirmed", agg_type="sum"
    )
    total_confirmed["Dates"] = pd.to_datetime(
        total_confirmed["Dates"], format="%m/%d/%y"
    )
    total_confirmed = total_confirmed.sort_values(by="Dates")

    total_deaths = get_group_agg(
        df=df_deaths, group_col="Dates", agg_col="Deaths", agg_type="sum"
    )
    total_deaths["Dates"] = pd.to_datetime(total_deaths["Dates"], format="%m/%d/%y")

    total_deaths = total_deaths.sort_values(by="Dates")

    merged_df = pd.merge(total_confirmed, total_deaths, on="Dates", how="inner")

    line(
        df=merged_df,
        x="Dates",
        y=["Confirmed", "Deaths"],
        y_title="People",
        x_title="Date",
        log_y=True,
        title="Confirmed Cases Compared to Deaths",
    )


def show_pandemic():
    display_title()
    filtered_df = get_vaccinated_filtered_df()
    display_summary_cards(filtered_df)
    display_line_chart()


show_pandemic()
