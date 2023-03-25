import random
pas = ''
len_pas = int(input("длина"))
for x in range(len_pas):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
print(pas)
