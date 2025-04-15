import streamlit as st
import pandas as pd
import country_converter as coco  # Importando o conversor
from src.utils.plotyly_chats.bar_chart import bar
from src.main import df_confirmed, df_deaths, get_group_agg, df_recovered, vaccinated


def padronizar_paises(df, coluna_original, nova_coluna="country"):
    cc = coco.CountryConverter()
    df[nova_coluna] = cc.convert(df[coluna_original], to="name_short", not_found=None)
    df = df.dropna(subset=[nova_coluna])  # Remove os que não foram encontrados
    return df


def show_cbr():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Comparisons between Regions
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Confirmed
    specific_date = df_confirmed[df_confirmed["Dates"] == "5/29/21"]
    specfic_confirmed = get_group_agg(
        df=specific_date,
        group_col="Country/Region",
        agg_col="Confirmed",
        agg_type="sum",
    ).sort_values("Confirmed", ascending=False)
    specfic_confirmed = padronizar_paises(specfic_confirmed, "Country/Region")

    # Deaths
    specific_date_deaths = df_deaths[df_deaths["Dates"] == "5/29/21"]
    date_deaths = get_group_agg(
        df=specific_date_deaths,
        group_col="Country/Region",
        agg_col="Deaths",
        agg_type="sum",
    ).sort_values("Deaths", ascending=False)
    date_deaths = padronizar_paises(date_deaths, "Country/Region")

    # Recovered
    date_recovered = get_group_agg(
        df=df_recovered,
        group_col="Country/Region",
        agg_col="Recovered",
        agg_type="max",
    ).sort_values("Recovered", ascending=False)
    date_recovered = padronizar_paises(date_recovered, "Country/Region")

    # Vaccinated
    specific_date_vaccinated = vaccinated[vaccinated["date"] >= "2021-05-29"]
    date_vaccinated = get_group_agg(
        df=specific_date_vaccinated,
        group_col="country",
        agg_col="daily_vaccinations",
        agg_type="sum",
    )
    date_vaccinated = padronizar_paises(date_vaccinated, "country")

    # Merges
    merge = specfic_confirmed.merge(date_deaths, on="country")
    merge_final = merge.merge(date_recovered, on="country")

    merged_df = pd.merge(date_vaccinated, merge_final, on="country", how="inner")
    merged_df = merged_df.rename(columns={"daily_vaccinations": "Vaccination"})

    # Visualization
    select = st.multiselect(
        "Select a Country",
        options=sorted(merged_df["country"].unique()),
        default=["Brazil"],
    )
    df_filtrado = merged_df[merged_df["country"].isin(select)]
    bar(
        df=df_filtrado,
        x="country",
        y=["Vaccination", "Recovered", "Deaths", "Confirmed"],
        title="Comparação entre Regiões",
        x_label="Country",
        y_label="Values"
    )


show_cbr()
