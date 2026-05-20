# import requests
# import pandas as pd
# def get_api_data():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#     data = response.json()
#     print(data)
#     df = pd.DataFrame([data])
#     print(df)
#     df.shape

# get_api_data()


import requests

key = "39d52398d53e8b5a482e9ee2dd0b7ffc"

url = f"https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={key}"

response = requests.get(url)

print(response.status_code)
print(response.text)