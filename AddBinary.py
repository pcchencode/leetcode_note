a = "11"
b = "1"

dec_a = int(a, 2)
dec_b = int(b, 2)

res = str(dec_a + dec_b)

bin_res = bin(int(res))

print(bin_res)
print(bin_res[2:])

#print(int("11", 2))
