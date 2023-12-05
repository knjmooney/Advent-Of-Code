import json
from pprint import pprint
from requests_cache import CachedSession

data = json.loads(
    CachedSession()
    .get(
        "https://adventofcode.com/2023/leaderboard/private/view/1031571.json",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

def getIt(dayId):
    result = []
    day = str(dayId)
    for entry in data['members'].values():
        try:
            first = entry['completion_day_level'][day]['1']['get_star_ts']
            second = entry['completion_day_level'][day]['2']['get_star_ts']
            if entry['name']:
                result.append((second - first, entry['name']))
        except:
            pass
    return result

pprint(sorted(getIt(4))[:20])