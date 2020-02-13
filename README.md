# __Postcode_request_json__
## **Program to retrieve info about specific location based on their postcodes**
* The project has been structure in a way that the user can input his personal or any other postcode as first iteration
`arguments = input('input your post code')`
* The software, will incapsulate the user entry in a variable and store it.
`r = requests.get(f'http://api.postcodes.io/postcodes/{arguments}')`
* The new stored variable `r` will be converted to a json file for a better viewing and stored as a new variable `result_json = r.json()`. 

``
result_var = result_json['result']
result_var_dict = json.dumps(result_var, indent=2)
``
The `result_var` will access the json dictionary at key result and retrieve all its data.

the json.dumbs is a json package method will make sure to take our dict output and format it with indentation and make it easy to read.
## **Blockers, Problems, Bugs, Solutions:**
* __Blockers:__ N/A
* __Problems:__ Figure it out that not all UK postcodes are available :satisfied:
* __Bugs:__ N/A
* __Solutions:__
    * __Problems:__ Google it or use the main website to check for the postcode :rage:
    * __Bugs:__


## **Outcomes:**
###### Learned how to extract specific data using requests **package** and json.