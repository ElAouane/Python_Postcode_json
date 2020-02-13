import requests
import json

arguments = input('input your post code')
r = requests.get(f'http://api.postcodes.io/postcodes/{arguments}')
result_json = r.json()
result_var = result_json['result']
result_var_dict = json.dumps(result_var, indent=2)

result_ccg = result_json['result']['ccg']
result_nuts = result_json['result']['nuts']
result_latitude = result_json['result']['latitude']
result_longitude = result_json['result']['longitude']
result_ccg_nested = result_json['result']['codes']['ccg']

# print(result_var_dict)
print(f'ccg=> {result_ccg}\n'
      f'nuts=> {result_nuts}\n'
      f'latitude=> {result_latitude}\n'
      f'longitude=> {result_longitude}\n'
      f'codes_ccg=> {result_ccg_nested}')
