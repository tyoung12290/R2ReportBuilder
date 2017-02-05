from bs4 import BeautifulSoup
import pandas

infile = open("config.xml","r")
contents = infile.read()
soup=BeautifulSoup(contents,'xml')
graphics = soup.find_all('node',class_ = "tridium.containers.GxPageNode")

dataList=[]
for item in graphics:

    pointName=item['name']
    if item.find('description')!= None:
        description=item.find('description').get_text("|", strip=True)
    else:
        description='0'




    itemList=[pointName,description]
    dataList.append(itemList)

df=pandas.DataFrame(dataList)
df.columns=['pointName','description']
df.to_csv('CIR_Graphics.csv')
