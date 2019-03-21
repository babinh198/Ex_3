
import string
alphabets = string.ascii_lowercase
words = ['python', 'patience', 'documents', 'students', 
         'homework','practice', 'success', 'english', 
         'university', 'congratulation']
results = []
for word in words:
    sum_value = 0
    for char in word:
        value = alphabets.index(char) + 1
        sum_value = sum_value + value
    results.append([word, sum_value])
print(results)

"""""""""""""""
[['python', 98], ['patience', 73], ['documents', 114], ['students', 122], ['homework', 108], ['practice', 75],
['success', 89], ['english', 74], ['university', 162], ['congratulation', 170]]
"""""""""""""''
