import requests

resp = requests.get('https://litipsum.com/api/json')

excerpt = ""
counter = 0

for line in resp.json()["text"]:
    if counter < 2:
        excerpt += line
        counter += 1
    else:
        break
print("This is a random excerpt retrieved using the Lit Ipsum API.\n")
print("---------------------------------------------------------------------\n")
print(excerpt)



