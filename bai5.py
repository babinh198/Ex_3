

.Tạo 1 list chứa N số 2

result = [2 for i in range(10)]
print(result)
#  
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

.Tạo 1 list chứa các số nguyên dương dưới 100, chia hết cho 3 hoặc 5

result = [number for number in range(100) if number % 3 == 0 or number % 5 == 0]
print(result)
# 
[0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99]

.Tạo ra 1 list có dạng như sau: ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN], với N = 20

result = [str(number) * 6 for number in range(21)]
print(result)
 #
['000000', '111111', '222222', '333333', '444444', '555555', '666666', '777777', '888888', '999999', '101010101010', '111111111111', '121212121212', '131313131313', '141414141414', '151515151515', '161616161616', '171717171717', '181818181818', '191919191919', '202020202020']

.Tạo 1 list chứa N số nguyên ngẫu nhiên, gợi ý sử dụng thư viện random: import random

import random
for _ in range(10):  
    print(random.randint(0, 10))

#2
8
4
3
7
4
1
3
4
5
