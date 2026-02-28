#!/usr/bin/env python3
from instagrapi import Client

USERNAME = "maan_na_yaar"
PASSWORD = 'B.M.W. M-6'

CAPTION = """EVERY VERSION OF YOU IS DYING.

The child you were... gone.
The person you are now... dying.

You are not static.
You are a RIVER, not a stone.

Character development isn't becoming new.
It's letting go of who you were.

🕸️

#characterdevelopment #growth #emotions #transformation #selfimprovement #innerwork #becoming #personalgrowth #apocalyptic #wisdom"""

client = Client()
client.login(USERNAME, PASSWORD)
client.photo_upload("./post.jpg", CAPTION)
print("Posted!")
client.logout()
