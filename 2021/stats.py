from datetime import datetime
import json
data = json.load(open("stats.json"))
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