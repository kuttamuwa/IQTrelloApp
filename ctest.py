import mongoengine

print("Baglanmayi deneyelim")
con = mongoengine.connect('iqmongodb')
print("baglandik gibi ? : {0}".format(con))

# con2 = mongoengine.register_connection('test', 'django_mongodb', 'django_mongodb', 'db',
#                                        username='root', password='mongoadmin')

print("Djongo ile deneyelim")
from djongo import database
con3 = database.connect('django_mongodb', host='db', username='root', password='mongoadmin')

print(f"Djongo ile baglandik gibi : {con3}")