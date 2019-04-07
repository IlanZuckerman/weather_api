
def pretty_print(response_dict):
    try:
        print("City: %s\n"
              "Belongs to Coutry: %s\n"
              "City ID: %s\n"
              % (response_dict['city']['name'],
                 response_dict['city']['country'],
                 response_dict['city']['id']))
    except:
        print("Current weather in City: %s\n"
              "City ID: %s\n"
              % (response_dict['name'],
                 response_dict['id']))

    try:
        for item in response_dict['list']:
            print('*** Forecast for: %s ***'  % item['dt_txt'])
            print('Condition: %s\n'
                  'Wind Speed: %s\n'
                  'Max Temp: %s\n'
                  'Min Temp: %s\n'
                  %(item['weather'][0]['description'],
                    item['wind']['speed'],
                    item['main']['temp_max'],
                    item['main']['temp_min']))
    except:
        print('Condition: %s\n'
              'Wind Speed: %s\n'
              'Max Temp: %s\n'
              'Min Temp: %s\n'
              %(response_dict['weather'][0]['description'],
                response_dict['wind']['speed'],
                response_dict['main']['temp_max'],
                response_dict['main']['temp_min']))
