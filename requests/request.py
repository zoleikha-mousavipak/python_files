import requests


params = {"q": "pizza"}
r = requests.get("https://www.bing.com/search", params=params)

print("status: ", r.status_code)
print(r.url)

f = open("./page2.html", "w+")
f.write(r.text)