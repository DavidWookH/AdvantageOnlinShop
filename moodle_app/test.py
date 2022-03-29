# href = 'view.php?id=3833&course=1'
# start ='id='
# end ='&'
# startid =href.find(start)+len(start)
# print(startid)
# endid = href.rfind(end)
# print(endid)
# user_system_id = href[startid:endid]
# print(user_system_id)
#
# user_system_id = href[href.find('id=')+len(start):href.rfind('&')]

text = 'geeks for geeks'


# Splits at space
print(text.split())

word =  text.split()
print(word)
len1 =len(word)
print(len1)

for i in range(len1):
    print(f'word {i} : {word[i]} ')
