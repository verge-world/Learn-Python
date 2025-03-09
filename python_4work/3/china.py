china = ['Changjiang','Huanghe','Taishan','Zhongwen','Beijing']
print(china)
#查看
print(china[3])
print(china[-1])
#调用
message = f'{china[-1]} is capital of China.'
print(message)
#修改
china[1] = 'Huangshan'
print(china)
#插入
china.append('Shanghai')
china.insert(1,'Huanghe')
print(china)
#删除
del china[2]
print(china)
popped_china = china.pop()
print(china)
print(popped_china)
china.remove('Huanghe')
print(china)
#排序
china.sort(reverse=True)
print(china)
print(sorted(china))
print(china)
china.reverse()
print(china)
lengged = len(china)
print(lengged)