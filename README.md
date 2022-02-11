# Test Script Voolkia - Python 
----


Este test se realizo en Python y en base a una consigna dispuesta por Voolkia para resolver.
Se utilizaron las siguientes herramientas para el desarrollo del script:
- Para obtener los recursos del sitio http://developers.mercadolibre.com/ se uso la librería ***requests*** .
- Para almacenar los datos del objeto en el archivo log se uso la libreria ***pickle***.
- Para trabajar con la consulta se uso la libreria ***json***


### Objetivo 
----
Para resolver este test se implemento un script que realizaba una consulta por medio del recurso ***/sites/$SITE_ID/search?seller_id=$SELLER_ID*** el cual permite listar ítems por vendedor.

Esa consulta se fue recorriendo como json y por cada iteración se creaba un objeto de tipo Item. En cada instancia se almacena la información solicitada y se guarda en una lista.

Para finalizar el sript, la lista se almacenaba en un archivo log.

### Instalación
----
#### 1 Paso
- ***1 forma***. Dar clic en Code y luego en Donwload Zip 
- ***2 forma***. Crear una carpeta, ingresar a git bash y ejecutar

```css
  git clone https://github.com/JuanFernandez87/test_voolkia.git
```

#### 2 Paso
- Ejecutar el archivo main.py
