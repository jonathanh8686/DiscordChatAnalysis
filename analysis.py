import math
import json
import seaborn as sns
from os import walk

CHAT_DIRECTORY = "cs3000"

def load_files(directory):
    return next(walk(directory), (None, None, []))

to_load = load_files(CHAT_DIRECTORY)
messages = []
for f in to_load[2]:
    ob = json.loads(open(to_load[0] + "/" + f, "r", encoding="utf-8").read())
    messages.extend(ob["messages"])

print(messages)

    


