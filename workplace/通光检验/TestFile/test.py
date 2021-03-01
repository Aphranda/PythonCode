# # a = "0101020203030404050506060707080809090A0A0B0B0C0C0D0D0E0E0F0F101011111212131314141515161617171818"
# # for i in range(24):
# #     print([a[4*i:4*i+2], a[4*i+2:4*i+4]])

# a = [1, 2, 3, 4]
# b = a * 4
# c = []
# d = 0
# for i in range(len(a)):
#     for j in  range(4):
#         c.append(b[j*4 + d])
#     d += 1
# print(c)
a = "1"
b = a.zfill(3)
print(b)