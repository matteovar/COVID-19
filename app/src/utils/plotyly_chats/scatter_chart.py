import pandas as pd
import plotly.express as px
import streamlit as st


def scatter(
    df: pd.DataFrame,
    x: str,
    y,
    color=None,
    hover_name=None,
    size=None,
    title: str = "Gráfico",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    hover_label: str = None,
    log_y: bool = False,
    color_sequence=None,  # <- novo parâmetro para definir cores
):
    # Verifica se y é múltiplo (lista)
    if isinstance(y, list):
        df_long = df.melt(
            id_vars=[x], value_vars=y, var_name="Tipo", value_name="Valor"
        )
        y = "Valor"
        color = "Tipo"

        labels = {
            x: x_label if x_label else x,
            y: y_label if y_label else "Valor",
            color: color_label if color_label else "Tipo",
        }
    else:
        labels = {x: x_label if x_label else x, y: y_label if y_label else y}
        if color and color_label:
            labels[color] = color_label

    if hover_name and hover_label:
        labels[hover_name] = hover_label

    scatter_view = px.scatter(
        data_frame=df_long if "df_long" in locals() else df,
        x=x,
        y=y,
        color=color,
        hover_name=hover_name,
        size=size,
        title=title,
        labels=labels,
        log_y=log_y,
        color_discrete_sequence=color_sequence,  # <- usa sequência de cores personalizada
    )
    st.plotly_chart(scatter_view)
