from re import finditer
text="abababbaab"
matcher=finditer("ab",text)
for m in matcher:
    print(m.start(),m.group())  