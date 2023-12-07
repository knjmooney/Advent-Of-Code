from datetime import datetime
from requests_cache import CachedSession
import json
import sys


data = json.loads(
    CachedSession()
    .get(
        f"https://adventofcode.com/2023/leaderboard/private/view/{sys.argv[1]}.json",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

members = data['members']
for member in members.values():
    completions = member['completion_day_level']
    days = sorted(completions.keys())
    print(member['name'])
    for day in days:
        for part, star in sorted(completions[day].items()):
            star_ts = star['get_star_ts']
            human_ts = datetime.fromtimestamp(star_ts)
            print(f"Day: {day}, Part: {part}, Time: {human_ts}")