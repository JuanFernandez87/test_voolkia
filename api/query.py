import requests
import json
import pickle
from api.models.items import Items

def query_api(seller_id, site_id):
    '''
    Funcion que realiza una consulta por medio de api, 
    genera un archivo de LOG que contiene 
    los siguientes datos de cada ítem: 
    - "id" del ítem
    - "title" del item
    - "category_id" donde está publicado
    '''
    filename = 'query.log'
    # Permite listar ítems por vendedor.    
    url = f'https://api.mercadolibre.com/sites/{site_id}/search?seller_id={seller_id}'

    # Obtengo los resultados de la consulta a la API
    response = requests.get(url)
    
    if response.status_code == 200:
        # Convierto el archivo json a diccionario
        response_json = json.loads(response.text)
        # Creo una lista para guardar los items
        l = []
        for i in response_json['results']:     
            # Creo la clase item para guardar los datos solicitados    
            item = Items()
            item.id_item = i['id']
            item.title = i['title']
            item.category_id = i['category_id']
            # Agrego el item a la lista
            l.append(item)

        file = open(filename, 'wb')
        # Guardo la lista en el archivo .log
        pickle.dump(l, file)
 
        file.close()

