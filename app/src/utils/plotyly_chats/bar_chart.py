import pandas as pd
import plotly.express as px
import streamlit as st


def bar(
    df: pd.DataFrame,
    x: str,
    y,
    title: str = "Gráfico",
    color=None,
    orientation="v",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    barmode: str = None, 
):
    if isinstance(y, list):
        df = df.melt(id_vars=[x], value_vars=y, var_name="Categoria", value_name="Valor")
        y = "Valor"
        color = "Categoria"
    
    labels = {x: x_label if x_label else x, y: y_label if y_label else y}
    if color and color_label:
        labels[color] = color_label

    bar_view = px.bar(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        color=color,
        orientation=orientation,
        labels=labels,
        barmode=barmode,
    )
    st.plotly_chart(bar_view)
