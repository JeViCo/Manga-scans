import cv2
import os.path
import numpy as np
import matplotlib.pyplot as plt

gFolderEng = 'Vitamin_Scans'
gFolderRu = 'Витамин'
gMask = '{:03d}'

def getDivs ( h ):
    lst = [ ]
    for i in range(  h - 1, 1, -1 ):
        if ( h % i == 0 ):
            lst += [ i ]
    return lst

def processScan ( img ):
    num = 0
    height = img.shape[ 0 ]

    path = os.path.join ( os.getcwd ( ), 'scans', gFolderEng )
    if not os.path.exists ( path ):
        os.makedirs ( path )
    
    print ( 'Формирование сканов началось!\nВыберите высоту сканов. Рекомендуемые значения:' )
    print ( *getDivs ( height ), sep=", " )
    
    pageSize = int ( input ( ) )
    comp = int ( input ( 'Выберите качество изображений (0-100):\n' ) )
    
    for y in range ( 0, height, pageSize ):
        tilePath = os.path.join ( path, '{:03d}.jpg'.format ( num ) )
        cv2.imwrite ( tilePath, img[ y: y+pageSize, 0:1024 ].copy ( ), [cv2.IMWRITE_JPEG_QUALITY, comp] )
        num += 1
    print ( 'Формирование сканов завершено!' )
    input ( '\nФрагменты были сохранены по пути:\n{}\n'.format ( path ) )

def mergeScans ( ):    
    num = 1
    height = 0
    imgs = [ ]

    print ( 'Склейка сканов началась!' )    

    while True:
        path = os.path.join ( os.getcwd ( ), 'scans', gFolderRu, gMask.format ( num ) + '.jpg');
        if not os.path.isfile ( path ):
            print ( 'Склейка сканов завершена!\n' )
            processScan ( cv2.vconcat ( imgs ) )
            break
        imgs += [ plt.imread ( path )[..., ::-1] ]
        num += 1

mergeScans ( ) # start
