from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json
from rich import pretty
from rich.progress import track
import time

pretty.install()  # rich


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


driver = webdriver.Safari()

events = {
    "event1": {"number": 1, "pages": 99},
    "event2": {
        "number": 2,
        "pages": 14,
    },
    "event3": {
        "number": 3,
        "pages": 3,
    },
    "event4": {
        "number": 4,
        "pages": 1,
    },
}

base_url = "https://fortnitetracker.com/events/epicgames_S15_FNCS_Qualifier1_NAE?window=S15_FNCS_Qualifier1_NAE_"
urls: list[str] = []
for i in range(99):
    full = f"{base_url}Event1&page={i}"
    urls.append(full)
for i in range(14):
    full = f"{base_url}Event2&page={i}"
    urls.append(full)
for i in range(3):
    full = f"{base_url}Event3&page={i}"
    urls.append(full)
for i in range(1):
    full = f"{base_url}Event4&page={i}"
    urls.append(full)

for url in track(urls[103:], description="Getting pages...", total=len(urls)):
    driver.get(url)

    total_teams = []

    """The teams are gotten in order, which is nice"""
    elements = driver.find_elements_by_class_name("fne-leaderboard__player-name")
    places = driver.find_elements_by_class_name("trn-lb-entry__rank")
    stats = driver.find_elements_by_class_name("trn-lb-entry__stat")
    split_stats = list(chunks(stats, 5))
    for elem, place, stat in zip(elements, places, split_stats):
        team = dict()

        if "Event1" in url:
            team["round"] = "Round1"
        elif "Event2" in url:
            team["round"] = "Round2"
        elif "Event3" in url:
            team["round"] = "Round3"

        elif "Event4" in url:
            team["round"] = "Round4"
        else:
            raise ValueError("invalid round")

        team["players"] = elem.text.strip()
        team["round_placement"] = int(place.text.strip())
        team["points"] = int(stat[0].text.strip())
        team["matches"] = int(stat[1].text.strip())
        team["wins"] = int(stat[2].text.strip())
        team["avg_elims"] = float(stat[3].text.strip())
        team["avg_place"] = float(stat[4].text.strip())
        total_teams.append(team)

    with open("teams.json", "r") as f:
        data = json.load(f)
    data.get("results").extend(total_teams)
    with open("teams.json", "w") as f:
        json.dump(data, f)


driver.close()

for i, url in enumerate(urls):
    start = time.time()
    if url.startswith("http"):
        print("not ecure")
    elif url.startswith("https"):
        print("secure")
    elif url.startswith("www"):
        print("unknown")
    end = time.time()
    duration = end - start
