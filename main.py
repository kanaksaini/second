#!/usr/bin/env python3
import requests
import base64
import json, time, pathlib, sys, re
import io, random
from PIL import Image
import threading



final_path = pathlib.Path(__file__).parent.resolve()
print(final_path)

import api_secret


headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': api_secret.api_9
}
# X_path_1 = //*[@id="__next"]/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div/a/div/div/div
X_path_1 = """//*[@id="__next"]/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div/a/div/div/div"""
X_path_2 = """ //*[@id="__next"]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/a/div/div/div"""


# main_element = """//*[@id="HTML1"]/div/button"""
main_element = X_path_1




def main_fun(numb):
    for overall in range(1,200000000000):
    
        try:
            data = {
                "url": api_secret.website_urls(),
                "browserHtml": True,
              "actions": [
            {
                  "action": "waitForSelector",
                  "selector": {
                    "type": "xpath",
                    "value": f'{main_element}'
                  },
                  "timeout": 5
                },
                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": f'{main_element}'
                    },
                    "waitForNavigationTimeout": 5
                },
                {
                        "action": "waitForTimeout",
                        "timeout": 5
                },


                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": '//*[@id="btn-main"]'
                    },
                    "waitForNavigationTimeout": 5
                  },
                {
                        "action": "waitForTimeout",
                        "timeout": 1
                },
                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": '//*[@id="btn-main"]'
                    },
                    "waitForNavigationTimeout": 5
                  },  
                {
                        "action": "waitForTimeout",
                        "timeout": 1
                },       
                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": '//*[@id="btn-main"]'
                    },
                    "waitForNavigationTimeout": 5
                  },  
                {
                        "action": "waitForTimeout",
                        "timeout": 1
                },      
                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": '//*[@id="btn-main"]'
                    },
                    "waitForNavigationTimeout": 5
                  }, 
                {
                        "action": "waitForTimeout",
                        "timeout": 1
                },      
                {
                    "action": "click",
                    "selector": {
                        "type": "xpath",
                        "value": '//*[@id="btn-main"]'
                    },
                    "waitForNavigationTimeout": 5
                  },               

                    # {
                    # "action": "click",
                    # "selector": {
                    #     "type": "xpath",
                    #     "value": "/html/body/section/div/div/div/div/div/form/button"
                    # },
                    # # "waitForNavigationTimeout": 10
                    # },
                {
                        "action": "waitForTimeout",
                        "timeout": 5 
                },        
             ],
              "screenshot": True,  
              "screenshotOptions": {
              "format": "jpeg",
              "fullPage": True
            }
            }
            # /html/body/section/div/div/div/div/div/form/button





            response = requests.post('https://api.proxyscrape.com/v3/accounts/freebies/scraperapi/request', headers=headers, json=data)
            time.sleep(3)
            print(f"\n Done_{numb}_{overall}")
            if response.status_code == 200:
                json_response = response.json()
                if 'browserHtml' in json_response['data']:
                    
                    print(rf"hello_{numb}_{overall}")


                    fetched_website_url = json_response['data']['url']
                    fetched_website_url = re.sub(r'[^a-zA-Z0-9\s]', '_', fetched_website_url)
                    print(fetched_website_url)
                    base_code = json_response['data']['screenshot']
                    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base_code, "utf-8"))))
                    img.save(rf'/project/workspace/imgs/my-image_{overall}_{numb}__{fetched_website_url}.jpeg')
  
                    with open(rf"{final_path}/data/data_{overall}_{numb}.txt", "w" , encoding="utf-8") as f:
                        f.write("BrowserType \n\n")
                        f.write(json_response['data']['browserHtml'])

                else:
                    print(f" No hello_{numb}_{overall}")

                    # print(base64.b64decode(json_response['data']['httpResponseBody']).decode())
                    with open(rf"{final_path}/data/Http_data_{overall}_{numb}.txt", "w", encoding="utf-8") as f:
                        f.write("Html Type \n\n")
                        f.write(base64.b64decode(json_response['data']['httpResponseBody']).decode())

            else:
                print("Error:", response.status_code)
            
                # with open(fr"{final_path}/errorO/error_{overall}_{numb}.txt", "w") as error:
                #     error.write(response.text)
                    
        except:
            pass




# Number of threads
num_threads = 60

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=main_fun, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(5)

# Wait for all threads to complete
for thread in threads:
    thread.join()


print("Everything completed")
