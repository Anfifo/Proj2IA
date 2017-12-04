def ASCII(s):
    x = 0
    for i in range(len(s)):
        x += ord(s[i])*2**(8 * (len(s) - i - 1))
    return x

def nr_vogals(s):
    x = 0;
    for i in range(len(s)):
        if s[i] in ['a','A','e','E','i','I','o','O','u', 'U']:
            x+=1
    return x
def nr_numbers(s):
	x = 0;
	for i in range(len(s)):
		if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
			x+=1
	return x


def nr_accents(s):
    x = 0
    for i in range(len(s)):
        try:
            if ord(s[i]) > 128:
                x += 1
        except TypeError:
            x += 1
    return x



print(ASCII('A'))
print(nr_vogals('aabbcce'))
print(nr_numbers('abc1'))

print(nr_accents(chr(223)))
x = 'abs'
x = x[0]+x[-1]
print(x)
print(ASCII(x))