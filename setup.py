from os.path import exists
from datetime import datetime
from os import system
if not exists("last_updated"):
    with open("version.txt", "w") as f:
        f.write(str(datetime.now().date()))
    system("python3 -m pip install -r requirements.txt")

