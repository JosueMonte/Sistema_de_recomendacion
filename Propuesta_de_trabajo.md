## Armar el cronograma de trabajar con Notion para llegar a la fecha
## Resolver el EDA hasta el punto 2.
* Crear un entorno virtual
    * escribir en la terminal: python -m venv venv
    * crear archivos: .gitignore y requirements.txt
    * enviar venv a .gitingore
    * instalar las librerias necesarias 
    * utilizar pip freeze > requirements.txt (para actualizar el .txt, si es necesario instalar mas librerias, hay que ejecutar el codigo de nuevo)
## Desarrollo de la API
* Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:
    * Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
    
* Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil:
    * https://docs.render.com/free#free-web-services
    * https://github.com/HX-FNegrete/render-fastapi-tutorial

* render deployado sistema_de_recomendacion_de_peliculas (api montada en la nube con render):
    * https://sistema-de-recomendacion-de-peliculas-8cnl.onrender.com/

* fastapi (es local, vinculo mi puerto con la api al servidor web):
    * http://127.0.0.1:8000/


