#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
import json
import ssl
import urllib.request

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    
    client = None
    with open("./google_key.json","r") as clientJson :
        client = json.load(clientJson)

    origin          = "37.5728359,126.9746922"
    destination     = "37.5129907,127.1005382"
    mode            = "transit"
    departure_time  = "now"
    key             = client["AIzaSyDY9JXaSCF1_OzdOHv6Md2UMSxCzHItx80"]

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&mode=transit&origins=37.541,126.986&destinations=35.1595454,126.8526012&region=KR&="+ origin \
            + "&destination=" + destination \
            + "&mode=" + mode \
            + "&departure_time=" + departure_time\
            + "&language=ko" \
            + "&key=" + key

    request         = urllib.request.Request(url)
    context         = ssl._create_unverified_context()
    response        = urllib.request.urlopen(request, context=context)
    responseText    = response.read().decode('utf-8')
    responseJson    = json.loads(responseText)

    with open("./Agent_Transit_Directions.json","w") as rltStream :
        json.dump(responseJson,rltStream)


    wholeDict = None
    with open("./Agent_Transit_Directions.json","r") as transitJson :
        wholeDict = dict(json.load(transitJson))

    path            = wholeDict["routes"][0]["legs"][0]
    duration_sec    = path["duration"]["value"]
    start_geo       = path["start_location"]
    end_geo         = path["end_location"]

    print(duration_sec) 
    # // 전체 걸리는 시간을 초로 나타낸 것
    print(start_geo)	
    # // 출발지 위도,경도
    print(end_geo)	
    # // 도착지 위도,경도