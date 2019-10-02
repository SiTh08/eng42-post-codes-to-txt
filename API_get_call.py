import requests

request_postcode = requests.get('http://api.postcodes.io/postcodes/IG12TP')

post_code_dict = request_postcode.json()

print(post_code_dict['result']['postcode'])
print(post_code_dict['result']['country'])
print(post_code_dict['result']['nhs_ha'])



