singers = ['IU', 'EXO', 'jessica']
singers.append('fx')#增加歌手
print(singers)
singers.insert(2, 'girl generation')#將少女時代塞到第2格
print(singers)
singers.pop()#刪掉最後一位歌手
print(singers)
singers.pop(3)#刪掉第x位歌手
print(singers)
singers.remove('IU')#刪掉第一位歌手
print(singers)
singers.remove('EXO')
print(singers)
singers.clear()#刪光list
print(singers)