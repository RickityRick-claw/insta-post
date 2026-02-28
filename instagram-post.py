#!/usr/bin/env python3
from instagrapi import Client

USERNAME = "maan_na_yaar"
PASSWORD = 'B.M.W. M-6'

CAPTION = """Every version of you is dying.
The child you were is gone.
The person you are now...
Will also be gone.

You are not a static being.
You are a river, not a stone.

Character development isn't becoming someone new.
It's letting go of who you were.

🕸️

#characterdevelopment #growth #emotions #becoming #selfimprovement #innerwork #transformation #personalgrowth #spiderman #miless morales"""

client = Client()
client.login(USERNAME, PASSWORD)
client.photo_upload("./post.jpg", CAPTION)
print("Posted!")
client.logout()
