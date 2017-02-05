from bs4 import BeautifulSoup
import pandas

infile = open("config.xml","r")
contents = infile.read()
soup=BeautifulSoup(contents,'xml')
analogHistories = soup.find_all('node',class_ = "tridium.apps.AnalogLogNode")
binaryLogHistories= soup.find_all('node',class_ = "tridium.apps.BinaryLogNode")
Histories=analogHistories+binaryLogHistories
dataList=[]
for item in Histories:

    pointName=item['name']
    if item.find('bufferSize')!= None:
        bufferSize=item.find('bufferSize').get_text("|", strip=True)
    else:
        bufferSize='0'

    if item.find('interval')!= None:
        interval=item.find('interval').get_text("|", strip=True)
    else:
        interval='0'

    if item.find('changeTolerance')!= None:
        changeTolerance=item.find('changeTolerance').get_text("|", strip=True)
    else:
        changeTolerance='0'

    if item.find('units')!= None:
        units=item.find('units').get_text("|", strip=True)
    else:
        units='0'


    itemList=[pointName,bufferSize,interval,changeTolerance,units]
    dataList.append(itemList)

df=pandas.DataFrame(dataList)
df.columns=['pointName','bufferSize','interval','ChangeTolerance','units']
df.to_csv('CIR_Alarms.csv')
