string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#string = "http://www.pythonchallenge.com/pc/def/map.html"
#print(string)

output = ""

# string.maketrans()
# for i in string:
#   if i.isalpha():
#     output += chr(ord(i)+2)
#
#   else:
#     output += i
# print(output)

def do_print():
    print(string.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))


if __name__ == '__main__':
    do_print()
