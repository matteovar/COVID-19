import pandas as pd
from data.ouput.dates import dates

confirmed = pd.read_csv("app/data/input/time_series_covid_19_confirmed.csv", header=0)
deaths = pd.read_csv("app/data/input/time_series_covid_19_deaths.csv")
recovered = pd.read_csv("app/data/input/time_series_covid_19_recovered.csv")
vaccinated = pd.read_csv("app/data/input/country_vaccinations.csv")

df_confirmed = pd.melt(
    confirmed,
    id_vars=["Province/State", "Country/Region", "Lat", "Long"],
    value_vars=dates(),
    var_name="Dates",
    value_name="Confirmed",
)

df_deaths = pd.melt(
    deaths,
    id_vars=["Province/State", "Country/Region", "Lat", "Long"],
    value_vars=dates(),
    var_name="Dates",
    value_name="Deaths",
)


def get_data_agg(df: pd.DataFrame, column_name: str, agg_type: str = None):
    return df[column_name].agg(agg_type)


def get_group_agg(
    df: pd.DataFrame, group_col: str, agg_col: str, agg_type: str = None
) -> pd.DataFrame:
    if agg_type is None:
        return df[
            [group_col, agg_col]
        ].drop_duplicates()  # Remove duplicatas para mostrar uma vez por data
    else:
        return df.groupby(group_col)[agg_col].agg(agg_type).reset_index()
