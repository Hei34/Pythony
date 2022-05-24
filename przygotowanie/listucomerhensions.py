def zamienromana(rom):
    romania=rom
    romania = romania.replace('IIII', 'IV')
    romania = romania.replace('VIIII','IX')
    romania = romania.replace('XXXX','XL')
    romania = romania.replace('LXXXX','XC')
    romania = romania.replace('CCCCC','D')
    romania = romania.replace('CCCC', 'CD')
    romania = romania.replace('DCCCC','CM')
    return romania

def rom_to_ar(number):
    romanian_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    number = number.replace('IV', 'IIII')
    number = number.replace('IX', 'VIIII')
    number = number.replace('XL', 'XXXX')
    number = number.replace('XC', 'LXXXX')
    number = number.replace('CD', 'CCCC')
    number = number.replace('CM', 'DCCCC')
    for i in number:
        n += romanian_numerals[i]
    return n
print(rom_to_ar('IX'))

def ar_to_rom(num1):
    znaki={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',0:''}
    n=0
    cyfry=0
    romania=''
    for i in str(num1):
        cyfry+=1
    if num1>9 and cyfry==2:
        for i in range(0,int((float(num1)/10))):
            romania+='X'
        romania+=znaki[num1%10]
    if num1>99 and cyfry==3:
        for i in range(0,int((float(num1)/100))):
            romania+='C'
        num2=num1%100
        for i in range(0,int((float(num2)/10))):
            romania+='X'
        romania += znaki[num2%10]
    romania=zamienromana(romania)
    print(cyfry)
    return romania

print(ar_to_rom(134))

