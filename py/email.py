import json

def hide_partial_email(email):
    result = []
    dog_pos = email.find("@")
    for s in range(0, len(email)):
        if (s > 3 and s < dog_pos):
            result.append("*")
        else:
            result.append(email[s])

    return str.join("", result)

res = hide_partial_email("kondaurov.dev@gmail.com")

print res