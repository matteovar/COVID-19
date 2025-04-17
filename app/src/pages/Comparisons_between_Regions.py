import io
import sys

import country_converter as coco
import pandas as pd
import streamlit as st
from src.main import df_confirmed, df_deaths, df_recovered, get_group_agg, vaccinated
from src.utils.merge import merge_data
from src.utils.plotyly_chats.bar_chart import bar

# Dicionário de mapeamento manual para casos especiais
SPECIAL_CASES = {
    "Scotland": None,
    "Wales": None,
    "Northern Ireland": None,
    "Diamond Princess": None,  # Será removido
    "MS Zaandam": None,  # Será removido
    "Timor": "Timor-Leste",  # Corrige para o nome padrão
    "West Bank and Gaza": "Palestine",
    "Taiwan*": "Taiwan",
    "Burma": "Myanmar",
    "Cabo Verde": "Cape Verde",
    "Congo (Brazzaville)": "Congo",
    "Congo (Kinshasa)": "Democratic Republic of the Congo",
    "Korea, South": "South Korea",
    "US": "United States",
}


def padronizar_paises(df, coluna_original, nova_coluna="country"):
    # Temporarily redirect stderr to suppress warnings
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()  # Redirect to a dummy stream

    cc = coco.CountryConverter()
    df[nova_coluna] = cc.convert(df[coluna_original], to="name_short", not_found=None)

    # Restore stderr
    sys.stderr = old_stderr

    df = df.dropna(subset=[nova_coluna])  # Remove rows where country wasn't recognized
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
    merge = merge_data(df1=specfic_confirmed, df2=date_deaths, on="country")
    merge_final = merge_data(df1=merge, df2=date_recovered, on="country")

    merged_df = merge_data(
        df1=date_vaccinated, df2=merge_final, on="country", how="inner"
    )
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
        y_label="Values",
        log_y=True,
    )


show_cbr()
