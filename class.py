import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Tomorrow is Friday :smile:")
df = pd.read_csv("tips.csv")
st.dataframe(df)

value_counts = df["sex"].value_counts()
st.dataframe(value_counts)

with st.container():
    fig, ax = plt.subplots()
    ax.pie(value_counts, autopct="%0.2f%%", labels=["Male", "Female"])
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts)
    st.pyplot(fig)

data_types = df.dtypes
cat_cols = tuple(data_types[data_types == "object"].index)
with st.container():
    feature = st.selectbox("Feature to plot", cat_cols)
    value_counts = df[feature].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.header("Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.2f%%", labels=value_counts.index)
        st.pyplot(fig)

    with col2:
        st.header("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

st.markdown("----")
st.header("Finally we will work with Seaborn")
with st.container():
    fig, ax = plt.subplots()
    sns.boxplot(x="sex", y="total_bill", data=df, ax=ax)
    st.pyplot(fig)

with st.container():
    chart_options = ("box", "violin", "Kdeplot", "histogram")
    chart_selection = st.selectbox("Graph to use: ", chart_options)

    fig, ax = plt.subplots()
    if chart_selection == "box":
        sns.boxplot(x="sex", y="total_bill", data=df, ax=ax)
    elif chart_selection == "violin":
        sns.violinplot(x="sex", y="total_bill", data=df, ax=ax)
    elif chart_selection == "Kdeplot":
        sns.kdeplot(x=df["total_bill"], hue=df["sex"], data=df, ax=ax)
    else:
        sns.histplot(x="total_bill", hue="sex", data=df, ax=ax)

    st.pyplot(fig)
