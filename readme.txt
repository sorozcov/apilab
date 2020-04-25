La base de datos ya se encuentra populada con los parents siguientes:

username="papacito1" pasword="python123"
username="papacito2" pasword="python123"
username="papacito3" pasword="python123"
username="papacito4" pasword="python123"
username="papacito5" pasword="python123"
[
    {
        "name": "Antonio",
        "id": 16,
        "user_id": 64,
        "user": 64
    },
    {
        "name": "Sergio",
        "id": 17,
        "user_id": 65,
        "user": 65
    },
    {
        "name": "Samuel",
        "id": 18,
        "user_id": 66,
        "user": 66
    },
    {
        "name": "Gerardo",
        "id": 19,
        "user_id": 67,
        "user": 67
    },
    {
        "name": "Andy",
        "id": 20,
        "user_id": 68,
        "user": 68
    }
]
se puede popular de nuevo con estos usuarios con
python manage.py shel
exec(open('initialParents.py').read())

Los apis son los siguientes:

Para realizar el login y el refresh
Enviar en el body username y password
#  \url(r'^api/v1/token-auth/', obtain_jwt_token),
#  url(r'^api/v1/token-refresh/', refresh_jwt_token)



#Para realizar todas las acciones necesarias del api
#api/babies
La operacion list no hay permisos.
Los permisos de crear estan implementado solo para usuarios autenticados.
Los permisos de editar, ver y eliminar estan dados unicamente para el papa mismo que ha creado el evento.
Body para crear y editar: parent=parent_id,name,lastname,age
Tiene un api/babies/baby_id/events para obtener todos los bebes del papa si tiene el permiso de ver solo si es su papa.

#api/events
La operacion list no hay permisos.
Los permisos de crear estan implementado solo para usuarios autenticados.
Los permisos de editar, ver y eliminar estan dados unicamente para el papa mismo que ha creado el evento.
Body para crear y editar: name,type,notes,baby=baby_id


#api/parents
Sus operaciones create no estan implementados por parte de postman salvo que ya se haya creado un usuario.
Los permisos de editar, ver y eliminar estan dados unicamente para el papa mismo.
Tiene un api/parents/user_id/babies para obtener todos los bebes del papa si tiene el permiso de ver solo si es su papa.


Para utilizar el api, haga lo siguiente:
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
Utilice una herramientas como postman para acceder a los apis.
