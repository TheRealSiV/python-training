list_2 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(sorted(list_2))
print(sorted(list_2, reverse=True))
print(list_2[1::2][0:2:1] + list_2[1::2][3::1] + list_2[0::2][3:4:])
print(list_2[0::2][0:3:1] + list_2[0::2][4::] + list_2[1::2][2:3:1])
print(list_2[2:3:1] + list_2[4:5:1] + list_2[-1:-2:-1])
