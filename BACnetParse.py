from bs4 import BeautifulSoup
import pandas

infile = open("config.xml","r")
contents = infile.read()
soup=BeautifulSoup(contents,'xml')
BACnetDevice = soup.find_all("node",class_='tridiumx.bacnet.objects.BACnetDevice')
dataList=[]
# AnalogValuesList=[]
# Points=[]
# i=0
for item in BACnetDevice:
    instanceNumber=item.find('instanceNumber').get_text("| ", strip=True)
    objectName=item.find('objectName').get_text("| ", strip=True)
    networkNumber=item.find('networkNumber').get_text("| ", strip=True)
    macAddress=item.find('macAddress').get_text("| ", strip=True)
    # AnalogOutputs=item.find_all("node",class_="tridiumx.bacnet.objects.lite.BACnetAnalogOutputLite")
    # AnalogValues=item.find_all('node',class_="tridiumx.bacnet.objects.lite.BACnetAnalogValueLite")
    # AnalogOverrides=item.find_all('node',class_="tridium.control.AnalogOverrideNode" )
    # LogicBlocks=item.find_all('node',class_="tridium.control.LogicNode")
    # BinaryValuePriority=item.find_all('node',class_="tridiumx.bacnet.objects.lite.BACnetBinaryValuePriorityLite")

    # for item in AnalogOutputs:
    #     name = item['name']
    # AvNamesList=[objectName]
    # for item in AnalogValues:
    #     AvNames = item['name']
    #     AvNamesList.append(AvNames)
    #     # AvInstanceNum=item.find('instanceNumber').get_text("| ", strip=True)
    #     # if item.find('units') != None:
    #     #     AvUnits=item.find('units').get_text("| ", strip=True)
    #     # else:
    #     #     AvUnits='none'
    #     #AVList=[AvNames,AvInstanceNum,AvUnits]
    #     #.append(AVList)
    # for item in AnalogOverrides:
    #     AvOvrdNames = item['name']
    # for item in LogicBlocks:
    #     LogicBlockName = item['name']
    # for item in BinaryValuePriority:
    #     BVPNames = item['name']

    # Points.append(AvNamesList)
    #for item in AnalogOuputs:

    itemList=[objectName,instanceNumber,networkNumber,macAddress]
    print(itemList)
    dataList.append(itemList)
# dfPoints=pandas.DataFrame(Points)

df=pandas.DataFrame(dataList)
df.columns=['objectName','instanceNumber','networkNumber','macAddress']
print(df)
# df.to_csv('RAYBACnet_test.csv')
