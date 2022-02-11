from api import query

SELLER_ID = 179571326
SITE_ID = "MLA"

if __name__ == '__main__':
    '''
    Funcion que recorre todos los ítems publicados por el 
    seller_id = 179571326 del site_id = "MLA"
    Genera un archivo de LOG que contiene los siguientes datos de
    cada ítem: 
    - "id" del ítem
    - "title" del item
    - "category_id" donde está publicado
    '''
    query.query_api(SELLER_ID, SITE_ID)
