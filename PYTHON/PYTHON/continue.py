# In các số chẵn từ 1 đến 10 và bỏ qua các số lẻ 
for i in range(1, 11):
    if i % 2 != 0:
        continue 
    print (i)