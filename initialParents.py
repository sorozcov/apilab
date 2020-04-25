#Inicializamos los usuarios

#Importamos los modelos
from django.contrib.auth.models import User
from parents.models import Parent

#Creamos el usuario y luego lo ligamos a un Parent


#Usuario 1
user=User.objects.create_user(username="papacito1",password="python123")
user.save()
parent= Parent.objects.create(name="Antonio",user=user)
parent.save()

#Usuario 2
user=User.objects.create_user(username="papacito2",password="python123")
user.save()
parent= Parent.objects.create(name="Sergio",user=user)
parent.save()


#Usuario 3
user=User.objects.create_user(username="papacito3",password="python123")
user.save()
parent= Parent.objects.create(name="Samuel",user=user)
parent.save()


#Usuario 4
user=User.objects.create_user(username="papacito4",password="python123")
user.save()
parent= Parent.objects.create(name="Gerardo",user=user)
parent.save()

#Usuario 5
user=User.objects.create_user(username="papacito5",password="python123")
user.save()
parent= Parent.objects.create(name="Andy",user=user)
parent.save()
