user = {
    "name": "dattu",
    "address": "allapalli",
    "phone": 982381145,
    "pass": 1234,
    "country": "India",
}
delete_key = ["address", "pass"]

for i in delete_key:
    user.pop(i)
print(user)
