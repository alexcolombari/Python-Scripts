import os, requests, time

SLEEP = 15
SITE_URL = "http://www.google.com.br"

while True:
    response = requests.get(SITE_URL)
    print(response)

    if response.status_code == 200:
        os.system('notify-send "Website Up" "'+SITE_URL+' is up"')
    else:
        os.system('notify-send "Website Down" "'+SITE_URL+' is down"')

    time.sleep(SLEEP)
