# import re

# string = input("Enter any word:- ")
# result = re.findall("[A-Za-z]+", string)
# print(result)

# import re

# a = input("Enter any word:- ")
# pat = re.sub("[aeiouAEIOU]", "", a)
# print(pat)


"""Exercise: एक paragraph (multiple lines/sentences) मध्ये अनेक emails लपलेले आहेत — काही valid, काही invalid
(जसं की domain मध्ये extension नसणे, किंवा @ नसणे). तुला:

सगळे valid emails शोधून काढायचे आहेत (pattern: username + @ + domain + . + extension, extension किमान 2 letters)
प्रत्येक valid email ची position (start, end) पण दाखवायची आहे
शेवटी, सगळ्या emails मधलं domain भाग (@ नंतरचा भाग) mask करायचं आहे (उदा. "abc@gmail.com" → "abc@*****")

हे तीन भाग आहेत — म्हणजे तीन वेगळे concepts (findall/finditer for extraction+position, आणि sub for masking) एकत्र वापरावे लागतील.
"""

import re

inp = input("Enter a passage:- ")

pattern = r"(\b[a-zA-Z0-9_]+@)[a-z]+\.[a-z]{2,}\b"
results = re.compile(pattern)

for result in results.finditer(inp):
    gmail = result.group()
    start = result.start()
    end = result.end()
    print(f"Gmail: {gmail} | start: {start} | end: {end}")

mask = re.sub("@[a-z]+\.[a-z]{2,}", "******", inp)
print(mask)
