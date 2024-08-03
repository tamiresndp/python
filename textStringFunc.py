billing = 1000
cost = 700
profit = billing - cost

print(f"billing the interprise: {billing}, cost: {cost}, profit: {profit}")

client_email = "qualquercoisa@gmail.com"

#maiuscula
client_email = client_email.upper()
print(client_email)

#minusculo
client_email = client_email.lower()
print(client_email)

# "@"
print(client_email.find("@")) # -1 quando nao encontrar

#tamanho do texto
print(len(client_email))

#pegar um caracter
print(client_email[0])
print(client_email[1:5]) #pegar pedaço de texto

#trocar um pedaço do texto
new_email = client_email.replace("@gmail.com", "@hotmail.com")
print(new_email)

name = "tamires nunes"

#trabalhar com nomes
print(name.capitalize())
print(name.title())

#pegar servidor do email
position_caracter = client_email.find("@") 
server = client_email[position_caracter:]
print(server)

#pegar o 1 nome
space_position = name.find(" ")
first_name = name[: space_position]

#pegar o sobrenome
surname = name[space_position:]
print(first_name)
print(surname)

#casos especiais - formataçoes numericas em texto

profit_margin = round(profit_margin, 2)
print(f"billing the interprise: {billing}, cost: {cost}, profit: {profit}, margin: {profit_margin}")

