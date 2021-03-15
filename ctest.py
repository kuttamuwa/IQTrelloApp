import mongoengine

print("Baglanmayi deneyelim")
con = mongoengine.connect('iqmongodb')
print("baglandik gibi ? : {0}".format(con))

