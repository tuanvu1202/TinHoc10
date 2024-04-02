danhsach = list(map(int, input().split()))
tong = 0
for i in range(len(danhsach)):
    tong+=danhsach[i]

print('Tong so tien dien cua ca nam:', tong)
print('Tong dien trung binh theo thang:', tong//12)
print('Cac thang co so tien dien nhieu hon tien dien trung binh theo thang:', end=' ')
for i in range(len(danhsach)):
    if(danhsach[i] > tong//12):
        print(i+1, end=' ')
