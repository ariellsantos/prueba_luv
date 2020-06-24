# Prueba LUV API DJANGO

## Uso basico

El api permite crear productos a partir de una lista y consultar los roductos ya creados

Ejemplo de peticion valida para crear una lista de productos 
```shell
curl --location --request POST 'http://luv-env.eba-h5bkmu5g.us-west-2.elasticbeanstalk.com/api/products/bulk_insert' \
--header 'Content-Type: application/json' \
--data-raw '{
	"products": [
		{
			"name": "Producto 1",
			"value": 20.1,
			"discount_value": 1,
			"stock": 1
		},	
		{
			"name": "Product 2",
			"value": 30.1,
			"discount_value": 18,
			"stock": 2
		}
		
	]
}'
```

Ejemplo de request para consultar productos
```shell
curl --request GET 'http://luv-env.eba-h5bkmu5g.us-west-2.elasticbeanstalk.com/api/products'
```





