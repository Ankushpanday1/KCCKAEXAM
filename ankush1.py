import re
def fun(s):
    patten = "^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    return re.search(patten,s)!=None

def filter_mail(email):
    return list(filter(fun, email))

if __name__ == '__main__':
    n = int(input())
    email = []
    for _ in range(n):
        email.append(input())

filtered_email = filter_mail(email)
filtered_email.sort()
print(filtered_email)
