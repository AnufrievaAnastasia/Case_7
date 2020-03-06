import os, os.path
path = '/Users/.../Desktop/Files' #вместо точек имя пользователя + скопируй папочку себе на рабочий стол
print(path)
print('1.Просмотр каталога \n'
      '2.На уровень вверх \n'
      '3.На уровень вниз \n '
      '4.Количество файлов и каталогов \n '
      '5.Размер текущего каталога \n'
      '6.Поиск файла \n'
      '7.Выход из программы')
ans = int(input('Выберете пункт меню: \n'))

def File(path, level = 1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            print('Спускаемся', path+'/'+i)
            File(path+'/'+i, level+1)
            print('Возвращаемся в', path)
if ans == 1:
    File(path)
