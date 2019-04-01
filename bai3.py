elec_num = [48, 100, 150, 199, 250, 1000]
result = []
elec_bill = 0
for num in elec_num:
     if num <= 50:
         elec_bill = num * 15000
         result.append(elec_bill)
     elif num > 51 and num <= 2000:
         elec_bill = (50 * 15000) + (num - 50)*16500
         result.append(elec_bill)
     else:
         elec_bill = (50 * 15000) + (150 * 16500) + (num - 200)*20000
print(result)

######

[720000, 1575000, 2400000, 3208500, 4050000, 16425000]
