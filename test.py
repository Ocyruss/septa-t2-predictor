import requests

response = requests.get("https://www3.septa.org/api/TransitView/index.php?route=T2")
print(response.text)