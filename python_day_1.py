alphabet = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
alphabet_inverse = alphabet[::-1]
print(alphabet_inverse)

ma_string = "Je suis une String"
print(ma_string)

num1 = (40)
num2 = (2)
print(num1+num2)

num1 = (3)
num2 = (14)
print(num1*num2)

nom = "Lait"
prix_unitaire = 2
inflation = prix_unitaire *10/100
prix_unitaire = prix_unitaire + inflation
quantité_en_stock = 15
stock_ajouté = 5
quantité_en_stock = quantité_en_stock + stock_ajouté
requête = int(input("Combien voulez vous de produits ?"))
quantité_en_stock = quantité_en_stock - requête
inventaire = [nom,prix_unitaire,quantité_en_stock]
phrase1 = "Il y a du {0} au prix de {1}, il en reste {2}".format(nom,prix_unitaire,quantité_en_stock)
print(inventaire)
print(requête)
print(phrase1)



