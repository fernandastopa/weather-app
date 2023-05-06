import requests
from math import trunc

print('\nWelcome to the Weather App! ')
lang = int(input("""
Please, enter the language:

[1] English
[2] Portuguese

"""))

if lang == 1:
    city_name = input('\nEnter the location: ')
    API_KEY = 'd5bb6e006b26945105019bc489256f99'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f'{base_url}q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print(f'\n[ERROR] Location not found. Please, check the location field and try again.')
    else:
        temperature = weather_data
        temp_celsius = trunc(temperature['main']['temp'])
        temp_fahrenheit = trunc((temp_celsius * 9/5) + 32)
        temp_kelvin = trunc(temp_celsius + 273.15)
        temp_unity = int(input("""
Enter the temperature unity:
    
[1] Celsius
[2] Fahrenheit
[3] Kelvin
        
"""))
        if temp_unity == 1:
            print(f'\nThe current temperature in {city_name.title()} is {temp_celsius} ºC')
        elif temp_unity == 2:
            print(f'\nThe current temperature in {city_name.title()} is {temp_fahrenheit} ºF')
        elif temp_unity == 3:
            print(f'\nThe current temperature in {city_name.title()} is {temp_kelvin} K')
        else:
            print('\n[ERROR] Invalid option! Please, check the option field and try again.')
elif lang == 2:
    print('\nBem vindo!')
    city_name = input('\nInsira a localização: ')
    API_KEY = 'd5bb6e006b26945105019bc489256f99'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f'{base_url}q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print(f'\n[ERRO] Localização não encontrada. Por favor, confira os dados inseridos e tente novamente.')
    else:
        temperature = weather_data
        temp_celsius = trunc(temperature['main']['temp'])
        temp_fahrenheit = trunc((temp_celsius * 9 / 5) + 32)
        temp_kelvin = trunc(temp_celsius + 273.15)
        temp_unity = int(input("""
Insira a unidade de temperatura:
    
[1] Celsius
[2] Fahrenheit
[3] Kelvin

"""))
        if temp_unity == 1:
            print(f'\nA temperatura atual em {city_name.title()} é {temp_celsius} ºC')
        elif temp_unity == 2:
            print(f'\nA temperatura atual em {city_name.title()} é {temp_fahrenheit} ºF')
        elif temp_unity == 3:
            print(f'\nA temperatura atual em {city_name.title()} é {temp_kelvin} K')
        else:
            print('\n[ERROR] Opção inválida. Por favor, confira os dados inseridos e tente novamente..')
else:
    print('\n[ERROR] Opção inválida. Por favor, confira os dados inseridos e tente novamente..')
