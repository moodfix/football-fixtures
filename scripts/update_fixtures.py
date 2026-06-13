import requests
import pandas as pd

API_KEY="123"

LEAGUES={

"EPL":"4328",
"LaLiga":"4335",
"SerieA":"4332",
"Bundesliga":"4331",
"Ligue1":"4334",
"ChampionsLeague":"4480"

}

all_matches=[]

for league,league_id in LEAGUES.items():

    url=f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventsseason.php?id={league_id}&s=2025-2026"

    try:

        r=requests.get(url)

        data=r.json()

        events=data.get("events",[])

        for match in events:

            all_matches.append({

                "Date":match.get("dateEvent"),
                "League":league,
                "HomeTeam":match.get("strHomeTeam"),
                "AwayTeam":match.get("strAwayTeam")

            })

    except Exception as e:

        print(e)

df=pd.DataFrame(all_matches)

df.to_csv(
"fixtures.csv",
index=False
)

print("fixtures.csv updated")
