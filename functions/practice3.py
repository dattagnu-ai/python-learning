# marks = [45, 67, 89, 23, 78]

# empty = []
# for i in marks:
#     empty.append(str(i))

# joined = ", ".join(empty)

# print(joined)


# Question: Function lिही product_info(product_name, **specs):

# product_name (required)
# **specs madhе kितीही keyword arguments (jasे price=15000, color="Black", warranty="1 year")
# Return kar: "<product_name> — " त्यानंतर pratyek spec key: value format madhे, comma-spac


def product_info(name, **specs):
    empty = []
    for key, value in specs.items():
        empty.append(f"{key}: {value}")

    return f"{name} - {', '.join(empty)}"


print(product_info("Dattu", laptop=20000, iphone=70000))

# Empty list kуठे ani kा banावी लागेल?
# Loop kाय iterate karेल (specs वर की specs.items() वर — फरक काय)?
# Loop च्या आत pratyek iteration madhे काय होईल?
# शेवटी join() कशावर apply hoईल?

# 1. empty list funtion madhe lagal kaun mala empty list madhe add karaycha ahe je me input denar
# 2. ani mag mala loop use kara lagnar specs.item() kaun ki mala key ani value pahije ahe mhnun specs.item()
# 3. loop cha kam apan je input delo te empty madhe add karte ani repeat karte
# 4. join empty var apply hoil kaun ata empty amdhe key ani value add zale ahe ani aplyala value nantar comma pahije ahe
