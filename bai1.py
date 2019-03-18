data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''

lines = data.split('\n')
result = []
for line in lines[1:-1]:
    result.append(line[0])
print("".join(result))
    
###  CROSSMYHEART
