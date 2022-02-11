from api import query

SELLER_ID = 179571326
SITE_ID = "MLA"

if __name__ == '__main__':
    '''
    Llama a la funcion que recorre todos los ítems publicados por el 
    seller_id = 179571326 del site_id = "MLA"
    '''
    query.query_api(SELLER_ID, SITE_ID)
