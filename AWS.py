import requests

url = "https://dwdnwwoco7.execute-api.us-east-1.amazonaws.com/Canary_Prod"

payload = {}
headers = {
  'x-api-key': 'UJedIetUpE3qn1yqjkh6Waqka7uqPMJQ9CvsKkCS'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
