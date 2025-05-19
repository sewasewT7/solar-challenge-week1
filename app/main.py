# app/main.py
import streamlit as st
from app.utils import load_data, plot_boxplots, plot_summary_table, run_stat_tests, plot_ghi_bar, show_heatmap

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("Solar Radiation Dashboard: Benin | Sierra Leone | Togo")

# Load data
data = load_data()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose View", ["Boxplot Comparisons", "Summary Table", "GHI Bar Chart", "Correlation Heatmap", "Statistical Testing"])

# Boxplot
if page == "Boxplot Comparisons":
    st.header("GHI / DNI / DHI Comparison by Country")
    plot_boxplots(data)

# Summary Table
elif page == "Summary Table":
    st.header("Summary Stats Table")
    plot_summary_table(data)

# Bar Chart
elif page == "GHI Bar Chart":
    st.header("Average GHI by Country")
    plot_ghi_bar(data)

# Heatmap
elif page == "Correlation Heatmap":
    st.header("Environmental Correlation Heatmap")
    show_heatmap(data)

# ANOVA / Kruskal-Wallis
elif page == "Statistical Testing":
    st.header("NOVA / Kruskal–Wallis Test on GHI")
    run_stat_tests(data)
