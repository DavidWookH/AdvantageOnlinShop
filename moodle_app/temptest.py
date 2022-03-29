
href = 'http://52.39.5.126/user/view.php?id=4069&course=1'

startid = href[href.find('=') + 1:href.rfind('&')]

print(startid)
