import re
from pprint import pprint
import os
dirname = os.path.dirname(__file__)

data = [d.replace('\n', ' ') for d in  open(f'{dirname}/04-input.txt').read().split("\n\n")]
data = [(d, [
        re.search(f, d)
        for f in (
            '(byr):(\d\d\d\d)( |$)', '(iyr):(\d\d\d\d)( |$)', '(eyr):(\d\d\d\d)( |$)', 
            '(hgt):(\d+(in|cm))( |$)', '(hcl):(#[0-9a-f]{6})( |$)', 
            '(ecl):(amb|blu|brn|gry|grn|hzl|oth)( |$)', '(pid):(\d{9})( |$)') 
    ])
    for d in data
]

data = [
    (   
        d, m, 
        m[0] and 1920 <= int(m[0].group(2)) <= 2002,
        m[1] and 2010 <= int(m[1].group(2)) <= 2020,
        m[2] and 2020 <= int(m[2].group(2)) <= 2030,
        m[3] and ((
                m[3].group(2).endswith('in') and 59 <= int(m[3].group(2)[:-2]) <= 76
            ) or (
                m[3].group(2).endswith('cm') and 150 <= int(m[3].group(2)[:-2]) <= 193
            )),
        bool(m[4]),
        bool(m[5]),
        bool(m[6]) 
    ) 
    for d, m in data]
pprint(data)
pprint(len([(d, m, *rest) for d, m, *rest in data if all(rest)]))


