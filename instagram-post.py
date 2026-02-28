#!/usr/bin/env python3
from instagrapi import Client

USERNAME = "maan_na_yaar"
PASSWORD = 'B.M.W. M-6'

CAPTION = """The lobster represents resilience. 
Dropped in boiling water, it adapts instantly - changing color in seconds.
We like to think we're stronger than creatures without a spine.
But when life throws us into hot water...
Do we adapt? Or do we break?

🦞

#lobster #resilience #adaptation #motivation #philosophy #life #growth #mindset #strength #wisdom"""

client = Client()
client.login(USERNAME, PASSWORD)
client.photo_upload("./post.jpg", CAPTION)
print("Posted!")
client.logout()
