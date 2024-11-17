import requests
import json

# Obtener los datos de la API
response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json')
if response.status_code == 200:
    data = response.json()
    with open('productos.txt', 'w') as file:
        json_data = json.dumps(data, indent=4)
        file.write(json_data)
else:
    print('Error al obtener los datos de la API')


    

