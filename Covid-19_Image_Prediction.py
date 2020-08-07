import requests
import json
import base64
import os

def get_prediction(image_data):
  url = 'https://l47syleshe.execute-api.us-east-1.amazonaws.com/Predict/3a467aeb-1330-4325-8eb7-41e315c89bde'
  r = requests.post(url, data=image_data)
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response


rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
  for file in files:
    with open(file, "rb") as image:
      payload = base64.b64encode(image.read())
    print('file: ', file)
    response = get_prediction(payload)
    prediction = json.loads(response)['predicted_label']
    print('prediction',prediction)
