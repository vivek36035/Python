import plotly.express as px

def plot_top_countries(df, metric="TotalConfirmed", top_n=10):
    """Plot top countries by selected metric."""
    top_countries = df.nlargest(top_n, metric)
    fig = px.bar(
        top_countries,
        x="Country",
        y=metric,
        color="Country",
        title=f"Top {top_n} Countries by {metric}"
    )
    return fig

def plot_pie_chart(df):
    """Show world proportion of confirmed, deaths, recovered."""
    totals = {
        "Confirmed": df["TotalConfirmed"].sum(),
        "Deaths": df["TotalDeaths"].sum(),
        "Recovered": df["TotalRecovered"].sum(),
    }
    fig = px.pie(
        names=list(totals.keys()),
        values=list(totals.values()),
        title="Global COVID-19 Proportion"
    )
    return fig
