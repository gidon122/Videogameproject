import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Video Game Sales", layout="wide")
st.title("Video Game Sales Dashboard")


@st.cache_data
def load_and_clean(source):
    """Load the CSV and apply the same cleaning steps as the notebook."""
    df = pd.read_csv(source)

    df = df.drop_duplicates()
    df["Region"] = df["Region"].fillna("North")

    # Strip "$" and convert to numeric
    df["NA_Sales"] = df["NA_Sales"].replace("[$]", "", regex=True)
    df["NA_Sales"] = pd.to_numeric(df["NA_Sales"], errors="coerce")
    average_sales = int(df["NA_Sales"].mean())
    df["NA_Sales"] = df["NA_Sales"].fillna(average_sales)

    df["Country"] = df["Country"].replace({"USA": "United States"})
    df["Country"] = df["Country"].str.title()

    df = df.rename(
        columns={
            "NA_Sales": "National Sales",
            "Global_Sales": "Global Sales",
            "NA_Profit": "National Profit",
            "Global_Profit": "Global Profit",
        }
    )

    # Cap outliers at the 95th percentile
    sales_cap = df["National Sales"].quantile(0.95)
    df["National Sales"] = np.where(
        df["National Sales"] > sales_cap, sales_cap, df["National Sales"]
    )
    return df


# ---- Data source: upload a file, or fall back to a local copy ----
uploaded = st.sidebar.file_uploader("Upload VideoGamesSales.csv", type="csv")

try:
    df = load_and_clean(uploaded if uploaded else "VideoGamesSales.csv")
except FileNotFoundError:
    st.info("Upload VideoGamesSales.csv in the sidebar to begin.")
    st.stop()

# ---- Cleaned data preview ----
st.subheader("Cleaned data (first 5 rows)")
st.dataframe(df.head(5), use_container_width=True)

# ---- Bar chart ----
st.subheader("National Sales by Region and Country")

national_sales = (
    df.groupby(["Region", "Country"], as_index=False)["National Sales"]
    .sum()
    .rename(columns={"National Sales": "National_Sales"})
    .sort_values(by="National_Sales", ascending=False)
)

fig, ax = plt.subplots(figsize=(16, 5))
sns.barplot(data=national_sales, x="Region", y="National_Sales", hue="Country", ax=ax)
ax.set_title("National Sales by Region and Country", fontweight="bold")
ax.set_xlabel("Region", fontweight="bold")
ax.set_ylabel("National Sales", fontweight="bold")
st.pyplot(fig)

# ---- Pie chart ----
st.subheader("Global Sales by Region")

global_sales_by_region = (
    df.groupby("Region", as_index=False)["Global Sales"]
    .sum()
    .rename(columns={"Global Sales": "Global_Sales"})
    .sort_values("Global_Sales", ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(10, 10))
ax2.set_title("Global Sales by Region", fontweight="bold", pad=25)

wedges, texts, autotexts = ax2.pie(
    global_sales_by_region["Global_Sales"],
    labels=global_sales_by_region["Region"],
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    wedgeprops={"edgecolor": "white", "linewidth": 1},
    labeldistance=1.1,
    pctdistance=0.7,
    rotatelabels=False,
)

for text in texts + autotexts:
    text.set_fontsize(10)

ax2.axis("equal")
fig2.tight_layout()

# Center the pie so it doesn't stretch across the full page width
_, middle, _ = st.columns([1, 2, 1])
with middle:
    st.pyplot(fig2)