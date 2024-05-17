s='伟大的中国梦'
#编码str->byte
scode=s.encode(errors='replace') #默认utf-8编码，utf-8中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace') #gbk中文占2个字节
print(scode_gbk)

#编码中出错问题
a='耶✌'
ascode=a.encode('gbk',errors='ignore')
print(scode)

ascode=a.encode('gbk',errors='replace')
print(ascode)

# scode=a.encode('gbk',errors='strict')
# print(scode)

#解码过程
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))