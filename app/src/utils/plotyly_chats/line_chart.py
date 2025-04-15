import pandas as pd
import plotly.express as px
import streamlit as st


def line(
    df: pd.DataFrame,
    x: str,
    y,
    title: str,
    x_title: str = "X Axis Title",
    y_title: str = "Y Axis Title",
    log_y: bool = False,  # New parameter to enable log scale
):
    line_view = px.line(data_frame=df, x=x, y=y, title=title)

    # Update layout with optional log scale
    line_view.update_layout(
        xaxis_title=x_title,
        yaxis_title=y_title,
        yaxis_type="log" if log_y else "linear",  # Conditional log scale
    )

    st.plotly_chart(line_view)
