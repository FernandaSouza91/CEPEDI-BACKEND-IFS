import re
padrao_email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
emails = []
e = str(input('Digite um email:'))
emails.append(e)
for email in emails:
    if padrao_email.match(email):
        print(f"{email} é um email válido.")
    else:
        print(f"{email} NÃO é um email válido.")
