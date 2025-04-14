import pandas as pd
import plotly.express as px
import streamlit as st


def line(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    x_title: str = "X Axis Title",  # Adicionando parâmetro para título do eixo X
    y_title: str = "Y Axis Title",  # Adicionando parâmetro para título do eixo Y
):

    line_view = px.line(data_frame=df, x=x, y=y, title=title)

    line_view.update_layout(
        xaxis_title=x_title,  # Usando o parâmetro x_title
        yaxis_title=y_title,  # Usando o parâmetro y_title
    )

    st.plotly_chart(line_view)
