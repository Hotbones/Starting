'''Recopilamos una dirección de correo electrónico del usuario y luego vamos a averiguar
si ese email tiene nombre de dominio personalizado o un nombre de un dominio popular. 
Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email está registrado con Google. ¡Eso es genial!.'''

'''We collect an email address from the user and then we're going to find out
if that email has a custom domain name or a popular domain name.
For example:

Input: mary.jane@gmail.com
Output: Hi Mary, I'm seeing that your email is registered with Google.'''

# Best example for this homework

popular_domains = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

user_email = input("What is your email address my friend? ")

user_name = user_email.split('@')[0]
user_domain = user_email.split('@')[-1]
user_domain = user_domain.split('.')[0]

if user_domain in popular_domains.keys():
    print(f"Hey {user_name} it seems like your email is registered with {popular_domains[user_domain]}!")
else:
    print(f"Very nice {user_name}, it seems like you have your own custom domain at {user_domain}!")