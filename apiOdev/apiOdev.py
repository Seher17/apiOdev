
import requests
response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response.json())

 
ad = input("Adınızı Girin : ")
soyad = input("Soyadınızı Girin : ")
print ("Merhaba  " + ad + " " + soyad)