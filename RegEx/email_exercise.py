import re

inp = input("Enter a passage:- ")

pattern = r"(\b[a-zA-Z0-9_]+@)[a-z]+\.[a-z]{2,}\b"
results = re.compile(pattern)

for result in results.finditer(inp):
    gmail = result.group()
    start = result.start()
    end = result.end()
    print(f"Gmail: {gmail} | start: {start} | end: {end}")

mask = re.sub("@[a-z]+\.[a-z]{2,}", "********", inp)
print(mask)
