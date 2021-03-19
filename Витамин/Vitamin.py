import os
import requests
from bs4 import BeautifulSoup as bs


web = input ( 'Введите ссылку на главу:\n' )
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get ( web, headers=headers )
html = bs ( response.text, 'html.parser' )


path = os.getcwd ( ) + '\\scans\\{}\\'.format ( 'Витамин' )
if not os.path.exists ( os.path.dirname ( path ) ):
    os.makedirs ( os.path.dirname ( path ) )

print ( 'Началось скачивание сканов!' )

num = 0
while True:
    img = html.find ( 'img', { 'id': 'image-{}'.format ( num ) } )
    if img is None:
        break
    #src
    img_src = img[ 'data-src' ].strip ( )
    img_file = img_src.split ( '/' )[ -1 ]
    
    #save
    r = requests.get ( img_src, stream=True, headers=headers )
    
    with open ( path + img_file, 'wb') as outfile:
        outfile.write ( r.content )
    
    #remove
    img.decompose()
    num += 1

input ( 'Все сканы сохранены!\n' )