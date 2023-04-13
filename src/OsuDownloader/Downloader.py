import requests
import os
from tqdm import tqdm

def getBmpList():

    maps_path = r"C:\Users\{0}\AppData\Local\osu!\Songs".format(os.getlogin())

    ListofBeatmaps = list()

    with open('maps/maps.txt', 'w') as mapsF:
        for xe,x in enumerate(os.listdir(maps_path)):
            if x == 'Failed':
                print('cont')
                continue
            mapsF.writelines(x)
            mapsF.writelines(' \n')
            ListofBeatmaps.append(x.split(" ", 1))

    ListofBeatmapsTest = ListofBeatmaps

    del ListofBeatmapsTest [:-4]

    print(ListofBeatmapsTest)
    return ListofBeatmapsTest

def getDownloadBmp(bmpNumber):
    # download
    mirrors = 'https://kitsu.moe'
    payload = {'noVideo': None}
    try:
        kitsumoeR = requests.get(mirrors+'/api/d/'+bmpNumber[0], params=payload)
    except ConnectionError as e : 
        print(e)
    return kitsumoeR

def saveBmp(response, bmpData):
    # save
    testmap = '1853515'
    urlweb = 'maps/Maps/'+testmap+''+'.zip'
    urlweb = 'maps/Maps/'+bmpData[0]+' '+ bmpData[1]+'.zip'
    with open(urlweb, 'wb') as out_file:
        out_file.write(response.content)
    os.rename('maps/Maps/'+bmpData[0]+' '+bmpData[1]+'.zip', 'maps/Maps/'+bmpData[0]+' '+bmpData[1]+'.zip')

def DownloadBmps(listofBmps):
    bar = tqdm(listofBmps)
    for bmpe, _ in enumerate(bar):
        currentBmp = getDownloadBmp(listofBmps[bmpe])
        saveBmp(currentBmp, listofBmps[bmpe])
