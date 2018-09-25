# from string import maketrans

# input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input = 'map'
output = ""
for letter in input:

    # print(binascii.a2b_base64(letter))

    letter = int(format(ord(letter), "x"), 16)
    # print(letter)
    # # letter = int(letter, 16)
    if letter >= 97 and letter <= 122:
        letter = letter + 2
        if letter > 122:
            letter = letter - 26
        print(letter)
    # letter = str(letter)
    output = output + format(letter, 'x')

# print(output)
print(bytes.fromhex(output))    # b'spam'

intab = 'yzabcdefghijklmnopqrstuvwx'
outtab = 'abcdefghijklmnopqrstuvwxyz'
trantab = str.maketrans(intab, outtab)

print(input.translate(trantab))
