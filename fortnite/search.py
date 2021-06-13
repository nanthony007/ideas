import jmespath
import json
import time
from prerun import configure
from rich import print


configure()

with open("teams.json", "r") as f:
    teams = json.load(f)


result = jmespath.search("results[?contains(@.players, 'Chap') == `true`]", teams)
ic(result)
print(result)


# for _ in track(range(10)):
#     time.sleep(1)
