def intToRoman(s):
	M = s // 1000
	remain = s - M*1000
	ro_M = "M"

	D = remain // 500
	remain = remain - D*500
	ro_D = "D"

	C = remain // 100
	remain = remain - C*100
	if C == 4 and D == 0:
		ro_C = "CD"
		C = 1
	elif C == 4 and D == 1:
		ro_C = "CM"
		C = 1
		D = 0
	else: 
		ro_C = "C"

	L = remain // 50
	remain = remain - L*50
	ro_L = "L"

	X = remain // 10
	remain = remain - X*10
	if X == 4 and L == 0:
		ro_X = "XL"
		X = 1
	elif X == 4 and L == 1:
		ro_X = "XC"
		X = 1
		L = 0
	else:
		ro_X = "X"

	V = remain // 5
	remain = remain - V*5
	ro_V = "V"

	I = remain // 1
	remain = remain - I*1
	if I == 4 and V == 0:
		ro_I = "IV"
		I = 1
	elif I == 4 and V == 1:
		ro_I = "IX"
		I = 1
		V = 0
	else:
		ro_I = "I"

	return ro_M*M + ro_D*D + ro_C*C + ro_L*L + ro_X*X + ro_V*V + ro_I*I

# print(intToRoman(45))



# roman = []
# for i in range(1, 3999):
# 	roman.append(intToRoman(i))

# roman_dict = {}
# for i, item in enumerate(roman):
# 	roman_dict[item] = i+1

# print(roman_dict)

# print(roman_dict['LVIII'])


def get_roman_dict():
    roman_dict = {}
    for i in range(1, 4000):
        roman_dict[intToRoman(i)] = i

    return roman_dict


def romanToInt(s):
	return get_roman_dict()[s]

# print(romanToInt("IV"))
# commit on git
# commit2 on git


# this is editing for issue1
# i dont know how to turn this on 
# conflicts!!! i wanna remain this line 

# edit1
# edit2
# edit3
# edit on personally
# edit on lang





