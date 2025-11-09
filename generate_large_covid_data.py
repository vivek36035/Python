"""
generate_large_covid_data.py

Generates a large synthetic covid_data CSV with:
- 20 countries
- 10-15 states per country (random)
- Male/Female rows
- Multiple age buckets and multiple dates
- Columns: Country,State,Gender,Age,Confirmed,Recovered,Deaths,Date

Usage:
  python generate_large_covid_data.py
This writes: data/covid_data_large.csv
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

out_dir = Path("data")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "covid_data_large.csv"

# 20 countries (strings). Feel free to edit or expand.
countries = [
    "India","USA","UK","Japan","Canada","Germany","France","Italy","Brazil","Australia",
    "Russia","China","South Africa","Spain","Mexico","Argentina","Singapore","UAE","Netherlands","Sweden"
]

# A pool of realistic-ish state names for variety; script will pick or append numbers if states needed.
state_pools = {
    "India": ["Maharashtra","Karnataka","Gujarat","Tamil Nadu","Uttar Pradesh","Rajasthan","Kerala","West Bengal","Telangana","Bihar","Assam","Punjab","Haryana","Odisha","Jharkhand"],
    "USA": ["California","Texas","Florida","New York","Pennsylvania","Illinois","Ohio","Georgia","North Carolina","Michigan","New Jersey","Virginia","Washington","Arizona","Massachusetts"],
    "UK": ["England","Scotland","Wales","Northern Ireland","Greater London","North West","South East","Yorkshire","West Midlands","East Midlands","East of England","South West","North East","London Boroughs","County Durham"],
    "Japan": ["Tokyo","Osaka","Kanagawa","Aichi","Hokkaido","Saitama","Chiba","Hyogo","Fukuoka","Shizuoka","Ibaraki","Tochigi","Gifu","Miyagi","Nagasaki"],
    "Canada": ["Ontario","Quebec","British Columbia","Alberta","Manitoba","Saskatchewan","Nova Scotia","Newfoundland","New Brunswick","Prince Edward Island","Yukon","Northwest Territories","Nunavut","Halifax","Ottawa"],
    "Germany": ["Bavaria","Berlin","North Rhine-Westphalia","Baden-Württemberg","Hesse","Saxony","Lower Saxony","Rhineland-Palatinate","Thuringia","Saarland","Schleswig-Holstein","Mecklenburg-Vorpommern","Saxony-Anhalt","Bremen","Hamburg"],
    "France": ["Île-de-France","Provence-Alpes-Côte d'Azur","Auvergne-Rhône-Alpes","Occitanie","Nouvelle-Aquitaine","Hauts-de-France","Grand Est","Brittany","Normandy","Pays de la Loire","Centre-Val de Loire","Bourgogne-Franche-Comté","Corsica","Guadeloupe","Martinique"],
    "Italy": ["Lombardy","Lazio","Veneto","Campania","Sicily","Piedmont","Emilia-Romagna","Tuscany","Apulia","Calabria","Sardinia","Liguria","Abruzzo","Trentino-Alto Adige","Umbria"],
    "Brazil": ["São Paulo","Rio de Janeiro","Minas Gerais","Bahia","Paraná","Rio Grande do Sul","Pernambuco","Ceará","Goiás","Maranhão","Santa Catarina","Paraíba","Espírito Santo","Alagoas","Mato Grosso"],
    "Australia": ["New South Wales","Victoria","Queensland","Western Australia","South Australia","Tasmania","Australian Capital Territory","Northern Territory","Greater Sydney","Melbourne Metro","Brisbane Metro","Perth Metro","Adelaide Metro","Gold Coast","Sunshine Coast"],
    "Russia": ["Moscow","Saint Petersburg","Moscow Oblast","Krasnodar Krai","Sverdlovsk Oblast","Novosibirsk Oblast","Rostov Oblast","Perm Krai","Bashkortostan","Volgograd Oblast","Khabarovsk Krai","Irkutsk Oblast","Krasnoyarsk Krai","Tatarstan","Nizhny Novgorod"],
    "China": ["Beijing","Shanghai","Guangdong","Zhejiang","Jiangsu","Shandong","Sichuan","Hubei","Fujian","Hebei","Henan","Liaoning","Anhui","Hunan","Yunnan"],
    "South Africa": ["Gauteng","KwaZulu-Natal","Western Cape","Eastern Cape","Limpopo","Mpumalanga","North West","Free State","Northern Cape","Cape Winelands","Johannesburg Metro","Tshwane","eThekwini","Nelson Mandela Bay","Mangaung"],
    "Spain": ["Madrid","Catalonia","Andalusia","Valencia","Galicia","Basque Country","Canary Islands","Castile and León","Castile-La Mancha","Murcia","Navarre","La Rioja","Aragon","Balearic Islands","Extremadura"],
    "Mexico": ["Mexico City","Jalisco","Nuevo León","Puebla","Guanajuato","Chiapas","Veracruz","Yucatán","Baja California","Sonora","Durango","Coahuila","Sinaloa","Tabasco","Morelos"],
    "Argentina": ["Buenos Aires","Córdoba","Santa Fe","Mendoza","Tucumán","Entre Ríos","Salta","Misiones","Chaco","Corrientes","Santiago del Estero","San Juan","San Luis","Neuquén","Formosa"],
    "Singapore": ["Central Region","East Region","North Region","North-East Region","West Region","Central Business District","Marine Parade","Bedok","Tampines","Jurong","Woodlands","Hougang","Yishun","Sembawang","Choa Chu Kang"],
    "UAE": ["Dubai","Abu Dhabi","Sharjah","Ajman","Ras Al Khaimah","Fujairah","Umm Al Quwain","Deyra","Jebel Ali","Al Ain","Al Bateen","Mussafah","Khalifa City","Mirdif","Jumeirah"],
    "Netherlands": ["North Holland","South Holland","Utrecht","Gelderland","North Brabant","Overijssel","Limburg","Friesland","Groningen","Drenthe","Flevoland","Zeeland","Amsterdam Metro","Rotterdam Metro","Eindhoven"],
    "Sweden": ["Stockholm","Västra Götaland","Skåne","Uppsala","Södermanland","Östergötland","Västerbotten","Norrbotten","Dalarna","Gävleborg","Västernorrland","Jönköping","Kalmar","Halland","Blekinge"]
}

# Age buckets or specific ages to simulate more rows
age_buckets = [5, 12, 20, 28, 35, 42, 50, 60, 70]  # kids, teens, young adult, adult, senior

# Dates - we'll create a series of dates (e.g., 30 days)
end_date = datetime(2021, 5, 1)
num_days = 30
dates = [(end_date - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]

rows = []

random.seed(42)

for country in countries:
    # pick 10 to 15 states for this country; prefer pool if available
    pool = state_pools.get(country, [])
    # if pool smaller than needed, we will append numeric suffix states
    n_states = random.randint(10, 15)
    states = pool[:n_states] if len(pool) >= n_states else pool + [f"{country}-State-{i}" for i in range(1, n_states - len(pool) + 1)]

    for state in states:
        # for each state create multiple rows across genders, ages and dates
        for date in dates:
            for gender in ["Male", "Female"]:
                # create several age entries per gender to grow dataset
                for age in age_buckets:
                    # Base numbers vary by country and state
                    base = random.randint(5000, 80000)  # base population-exposed
                    # vary confirmed by age and gender (simulate)
                    confirmed = max(0, int(base * random.uniform(0.02, 0.2) * (1 + (age/100) * random.uniform(-0.5, 0.5))))
                    recovered = max(0, int(confirmed * random.uniform(0.7, 0.98)))
                    deaths = max(0, int(confirmed * random.uniform(0.001, 0.06)))

                    rows.append({
                        "Country": country,
                        "State": state,
                        "Gender": gender,
                        "Age": age,
                        "Confirmed": confirmed,
                        "Recovered": recovered,
                        "Deaths": deaths,
                        "Date": date
                    })

# Shuffle rows for realism
random.shuffle(rows)

# Write CSV
fieldnames = ["Country","State","Gender","Age","Confirmed","Recovered","Deaths","Date"]
with open(out_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print(f"Wrote {len(rows)} rows to {out_file.resolve()}")
