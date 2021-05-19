import requests
from datetime import date
import json
from twilio.rest import Client
from notify_run import Notify
import time
base_url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"

def call_api(params):
    district_id=params['district_id']
    date=params['date']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    data=requests.get(base_url,params=params,headers=headers).json()
    centers=data['centers']
    available=[]
    for center in centers:
        for session in center['sessions']:
            if session["min_age_limit"]==18 and session["available_capacity"]>0:
                appointment="Center name : "+center["name"]+"\nCenter Address : "+center["address"]+"\nDate : "+str(session["date"])+"\nAvailable capacity : "+str(session['available_capacity'])+"\n\n"
                available.append(appointment)
    if len(available)>0:
        print(available)
        #send_whatsaap_msg(available)
        #send_android_noti(available)
        #send_email(available)   
    else:
        print("No slots available")
    
def send_whatsaap_msg(available):
    ACCOUNT_SID="ENTER YOUR TWILIO ACCOUNT SID"
    AUTH_TOKEN="ENTER YOUR AUTH TOKEN"
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    from_whatsapp_number='whatsapp:YOUR TWILIO NUMBER'
    to_whatsapp_number='whatsapp:DESTINATION NUMBER'

    client.messages.create(body=available,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)

def send_android_noti(available):
    notify = Notify()
    notify.send(available)

def api_scheduler():
    params={}
    district_id=725
    dates=date.today().strftime("%d-%m-%Y")
    params["district_id"]=district_id
    params["date"]=dates
    call_api(params)

while True:
    api_scheduler()
    time.sleep(10)













