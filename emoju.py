"""Convert emoji.csv into yaml
"""
import re
from os import system
import yaml
from os.path import exists

EMOJI_CSV = "emoji.csv"

if not exists(EMOJI_CSV):
    system("cat README.md|cut -d '|' -f 2,3|sed 's/|/,/g' >emojis.csv")

emojus = {}
pack = {"title": "slack-emoji-for-techies",
"emojis": emojus} 
for line in open("emojis.csv", "r"):
    if not line.strip():
        continue
    try:
        name,url = line.split(',')
        url = re.match(".*img src=\"(.*)\" width.*", url).groups()[0]
        emojus[name.strip()] = url
    except (AttributeError, ValueError) as e:
        print("skipping %s" % line)
        pass

open("anythingcodes-techies.yaml", "w").write(yaml.dump(pack))
