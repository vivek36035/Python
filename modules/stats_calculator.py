def global_summary(df):
    total_cases = df["TotalConfirmed"].sum()
    total_deaths = df["TotalDeaths"].sum()
    total_recovered = df["TotalRecovered"].sum()
    return total_cases, total_deaths, total_recovered

def country_summary(df, country_name):
    data = df[df["Country"] == country_name]
    if not data.empty:
        return {
            "Confirmed": int(data["TotalConfirmed"].values[0]),
            "Deaths": int(data["TotalDeaths"].values[0]),
            "Recovered": int(data["TotalRecovered"].values[0])
        }
    else:
        return {"Confirmed": 0, "Deaths": 0, "Recovered": 0}
