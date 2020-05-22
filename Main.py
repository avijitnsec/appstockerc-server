print ("Stocker server")

from firebase import firebase

fb = firebase.FirebaseApplication("https://fir-demo-9cfba.firebaseio.com/", None)

data = {
    'Name' : 'Avijit Das',
    'email' : 'avijitnsec@gmail.com'

}

result = fb.post('/fir-demo-9cfba/student', data)

print(result)