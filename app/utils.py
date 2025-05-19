# app/utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import f_oneway, kruskal

@st.cache_data
def load_data():
    df_benin = pd.read_csv("data/benin_clean.csv")
    df_sierra = pd.read_csv("data/sierra_leone_clean.csv")
    df_togo = pd.read_csv("data/togo_clean.csv")
    df_benin["Country"] = "Benin"
    df_sierra["Country"] = "Sierra Leone"
    df_togo["Country"] = "Togo"
    return pd.concat([df_benin, df_sierra, df_togo], ignore_index=True)

def plot_boxplots(data):
    for metric in ["GHI", "DNI", "DHI"]:
        st.subheader(f"{metric} Distribution")
        fig, ax = plt.subplots()
        sns.boxplot(x="Country", y=metric, data=data, ax=ax)
        st.pyplot(fig)

def plot_summary_table(data):
    summary = data.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)

def run_stat_tests(data):
    st.write("### One-way ANOVA on GHI")
    grouped = [group["GHI"].dropna() for _, group in data.groupby("Country")]
    f_stat, p_val = f_oneway(*grouped)
    st.write(f"**F-statistic**: {f_stat:.2f}")
    st.write(f"**p-value**: {p_val:.4f}")
    if p_val < 0.05:
        st.success("Statistically significant difference (p < 0.05)")
    else:
        st.warning("No significant difference (p ≥ 0.05)")

def plot_ghi_bar(data):
    avg_ghi = data.groupby("Country")["GHI"].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    avg_ghi.plot(kind="bar", color="skyblue", ax=ax)
    st.pyplot(fig)

def show_heatmap(data):
    corr = data[["GHI", "DNI", "DHI", "Wind Speed", "Tamb"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)