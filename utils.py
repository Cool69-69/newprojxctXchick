#This Bot is heavily modified for heaven exclusively By TargetX25 So he deserve a big piece of credits too.

import aiohttp
import asyncio
import os

####################  Tnlink  ####################

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'https://tnshort.net/api'
    params = {'api': '68338f1be9317aa1b3d3346f7d8e6e383bb63c4c',
              'url': link,
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            if data["status"] == "success":
                return data['shortenedUrl']
            else:
                return f"Error: {data['message']}"
            
 
