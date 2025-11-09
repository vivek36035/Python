import streamlit as st
import pandas as pd
import plotly.express as px

# ----- Page Setup -----
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("🦠 Global COVID-19 Analytics Dashboard")
st.caption("Analyze COVID-19 data for multiple countries and their states with demographics and trends.")

# ----- Load Data -----
@st.cache_data
def load_data():
    df = pd.read_csv("data/covid_data_large.csv")
    df.fillna("Unknown", inplace=True)
    return df

df = load_data()

# ----- Sidebar -----
st.sidebar.header("🔍 Filters")

countries = sorted(df["Country"].unique())
selected_country = st.sidebar.selectbox("Select Country", countries)

states = sorted(df[df["Country"] == selected_country]["State"].unique())
selected_state = st.sidebar.selectbox("Select State", states)

filtered = df[(df["Country"] == selected_country) & (df["State"] == selected_state)]

# ----- Metrics -----
total_confirmed = int(filtered["Confirmed"].sum())
total_recovered = int(filtered["Recovered"].sum())
total_deaths = int(filtered["Deaths"].sum())
recovery_rate = (total_recovered / total_confirmed * 100) if total_confirmed else 0
death_rate = (total_deaths / total_confirmed * 100) if total_confirmed else 0

st.markdown(f"### 📍 {selected_country} → {selected_state}")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Confirmed", f"{total_confirmed:,}")
c2.metric("Recovered", f"{total_recovered:,}")
c3.metric("Deaths", f"{total_deaths:,}")
c4.metric("Recovery Rate", f"{recovery_rate:.2f}%")
c5.metric("Death Rate", f"{death_rate:.2f}%")

st.divider()

# ----- Charts -----
if not filtered.empty:
    st.subheader("📊 Gender-wise Distribution")
    fig_gender = px.bar(filtered, x="Gender", y="Confirmed", color="Gender",
                        title="Cases by Gender", barmode="group")
    st.plotly_chart(fig_gender, use_container_width=True)

    st.subheader("📈 Age vs Cases")
    fig_age = px.bar(filtered, x="Age", y="Confirmed", color="Gender",
                     title="Cases by Age & Gender", barmode="group")
    st.plotly_chart(fig_age, use_container_width=True)

    st.subheader("🧩 Recovery vs Deaths Ratio")
    pie_data = pd.DataFrame({
        "Category": ["Recovered", "Deaths"],
        "Count": [total_recovered, total_deaths]
    })
    fig_pie = px.pie(pie_data, names="Category", values="Count",
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("🌍 State-wise Comparison (within selected country)")
    summary = df[df["Country"] == selected_country].groupby("State")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()
    fig_state = px.bar(summary, x="State", y=["Confirmed", "Recovered", "Deaths"],
                       barmode="group", title=f"State-wise COVID Data in {selected_country}")
    st.plotly_chart(fig_state, use_container_width=True)
else:
    st.warning("No data for this selection.")

# ----- Insights -----
st.subheader("🧠 Insights")
if total_confirmed > 0:
    if recovery_rate > 90:
        st.success("✅ Excellent recovery rate observed in this region.")
    elif death_rate > 5:
        st.error("⚠️ High fatality rate — further measures recommended.")
    else:
        st.info("ℹ️ Stable condition with moderate recovery rate.")
else:
    st.info("No data available for insights.")

st.subheader("📋 Raw Data View")
st.dataframe(filtered)

st.markdown("---")
st.caption("Developed by Vivek Zambre — Advanced Mini Project using Streamlit, Pandas & Plotly.")
