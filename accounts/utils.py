import requests

def send_greeting(greeting):
    resp = requests.post("http://127.0.0.1:9000/api/v1/greeting/", data={
        "message": greeting,
    }, headers={
        "Authorization": "Bearer L2IY1MHWMOhk6YSmbU5nAQtuqTxO46"
    })
    
    if resp.status_code == 200:
        print("It worked")
    else:
        print("Something went wrong", resp)
        