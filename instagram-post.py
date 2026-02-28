#!/usr/bin/env python3
from instagrapi import Client

USERNAME = "maan_na_yaar"
PASSWORD = 'B.M.W. M-6'

CAPTION = """We see what we believe, not what is. 👁️

Shatter the mirrors of illusion. Question everything. Break the chains of inherited fear.

What you perceive is not the truth — it's your limitation.

#perception #awareness #philosophy #truth #consciousness #growth #selfdiscovery #mysticism #wisdom"""

client = Client()
client.login(USERNAME, PASSWORD)
client.photo_upload("./post.jpg", CAPTION)
print("Posted!")
client.logout()
