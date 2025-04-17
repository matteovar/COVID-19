import pandas as pd
import streamlit as st
from src.main import df_deaths, df_recovered, get_group_agg
from src.utils.plotyly_chats.scatter_chart import scatter


def load_and_prepare_data(date_str="2021-05-29"):
    df_deaths["Dates"] = pd.to_datetime(df_deaths["Dates"], format="%m/%d/%y")
    df_recovered["Dates"] = pd.to_datetime(df_recovered["Dates"], format="%m/%d/%y")

    deaths_on_date = df_deaths[df_deaths["Dates"] == date_str]
    recover_on_date = df_recovered[df_recovered["Dates"] == date_str]

    top_deaths = get_group_agg(deaths_on_date, "Country/Region", "Deaths", "sum")
    top_recover = get_group_agg(recover_on_date, "Country/Region", "Recovered", "sum")
    top_recover = top_recover.sort_values("Recovered", ascending=False)

    merged_df = top_deaths.merge(top_recover, on="Country/Region")
    return merged_df, top_deaths


def plot_scatter(df):
    scatter(
        df=df,
        x="Country/Region",
        y=["Deaths", "Recovered"],
        log_y=True,
        color_sequence=["crimson", "seagreen"],
    )


def show_table(title, df, column, ascending=True):
    top10 = df.nsmallest(10, column) if ascending else df.nlargest(10, column)
    max_value = float(top10[column].max())  # <-- Aqui o fix

    st.markdown(f"#### {title}")
    st.dataframe(
        top10,
        column_order=("Country/Region", column),
        hide_index=True,
        width=None,
        column_config={
            "Country/Region": st.column_config.TextColumn("States"),
            column: st.column_config.ProgressColumn(
                column,
                format="%f",
                min_value=0,
                max_value=max_value,
            ),
        },
    )


def show_mor_rec():
    st.markdown(
        "<h1 style='text-align: center; font-family: Arial, sans-serif;'>Mortality and Recovery Rates</h1>",
        unsafe_allow_html=True,
    )

    merged_df, top_deaths = load_and_prepare_data()

    plot_scatter(merged_df)

    col1, col2 = st.columns(2)
    with col1:
        show_table(
            "States With the Highest Mortality Rates",
            top_deaths,
            "Deaths",
            ascending=False,
        )
    with col2:
        show_table(
            "States With the Lowest Mortality Rates",
            top_deaths,
            "Deaths",
            ascending=True,
        )


show_mor_rec()
