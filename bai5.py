

L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]

##Có trong cả A, B
list(set(L1).intersection(set(L2)))

##Chỉ có trong A
set(L1).difference(set(L2))

##Chỉ có trong B
set(L2).difference(set(L1))

##Không có trong cả A và B
set(L1).symmetric_difference(L2)


