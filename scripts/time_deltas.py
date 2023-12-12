from datetime import timedelta
from pprint import pprint
from requests_cache import CachedSession
import argparse
import json
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--leaderboard_id')
parser.add_argument('-d', '--day')

args = parser.parse_args()

data = json.loads(
    CachedSession(expire_after=timedelta(hours=1))
    .get(
        f"https://adventofcode.com/2023/leaderboard/private/view/{args.leaderboard_id}.json",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)


def getIt(dayId):
    result = []
    day = str(dayId)
    for entry in data["members"].values():
        try:
            first = entry["completion_day_level"][day]["1"]["get_star_ts"]
            second = entry["completion_day_level"][day]["2"]["get_star_ts"]
            if entry["name"]:
                result.append((second - first, entry["name"]))
        except:
            pass
    return result


tops = sorted(getIt(args.day))[:20]
nameWidth = 1 + max(len(name) for _, name in tops)

for i, (time, name) in enumerate(tops, 1):
    print(f'{i:3} {name:<{nameWidth}} {time:5}s')