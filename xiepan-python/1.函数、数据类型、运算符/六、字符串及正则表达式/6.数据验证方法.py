#是否都是十进制的阿拉伯数字
print('123'.isdigit()) #True
print('一二三'.isdigit())#False
print('0b1010'.isdigit())#二进制的123 #False
print('ⅡⅡⅡ'.isdigit())#False
print('-'*30)

#所有字符都是数字
print('123'.isnumeric()) #True
print('一二三'.isnumeric())#True
print('0b1010'.isnumeric())#False
print('ⅡⅡⅡ'.isnumeric())#True
print('壹贰叁'.isnumeric())#True
print('-'*30)

#所有字符都是字母（包含中文字符）
print('hello你好'.isalpha())#True
print('he23'.isalpha())#False
print('hello你好一二三'.isalpha())#True
print('hello你好ⅡⅡⅡ'.isalpha())#False
print('hello你好壹贰叁'.isalpha())#True
print('-'*30)

#所有字符都是数字或字母（包含中文字符）
print('hello你好'.isalnum())#True
print('he23'.isalnum())#False
print('hello你好一二三'.isalnum())#True
print('hello你好ⅡⅡⅡ'.isalnum())#True
print('hello你好壹贰叁'.isalnum())#True
print('-'*30)

#所有字符都是小写
print('AbCd'.islower())#False
print('abcd'.islower())#True
print('abcd123'.islower())#True
print('abcd你好'.islower())#True
print('-'*30)

#所有字符都是大写
print('AbCd'.isupper())#False
print('abcd'.isupper())#False
print('ABCD'.isupper())#True
print('ABCD你好123'.isupper())#True
print('-'*30)

#所有字符都是首字母大写
print('1AbCd'.istitle())#False
print('abcd'.istitle())#False
print('ABCD'.istitle())#False
print('Abv'.istitle())#True
print('A Bv Cd De'.istitle())#True
print('-'*30)

#是否都是空白字符
print('\t'.isspace())#True
print(' '.isspace())#True
print('\n'.isspace())#True
