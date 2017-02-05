from bs4 import BeautifulSoup, Comment
import pandas
from os import path
from pandas import ExcelWriter
import openpyxl
class Parser:

    def __init__(self,filename):
        file_path=path.relpath(filename)

        infile = open(file_path,"r")
        contents = infile.read()
        self.soup=BeautifulSoup(contents,'xml')



    def alarms(self,soup):
        alarms = soup.find_all('toOffnormal')
        comments=soup.findAll(text=lambda text:isinstance(text, Comment))
        pointStartList=[]
        for alarm in alarms:
            pointStart=alarm.parent.parent.parent
            pointStartList.append(pointStart)
        dataList=[]
        for item in pointStartList:

            pointName=item['name']
            for comment in comments:
                x='/'+pointName
                if x in comment:
                    pointPath = comment
            if item.find('timeDelay') != None:
                timeDelay=item.find('timeDelay').get_text("|", strip=True)
            else:
                timeDelay='0'

            if item.find('eventEnable')!=None:
                toOffnormal=item.find('toOffnormal').get_text("| ", strip=True)
                toFault=item.find('toFault').get_text("| ", strip=True)
                toNormal=item.find('toNormal').get_text("| ", strip=True)
            else:
                toOffnormal='false'
                toFault='false'
                toNormal='false'

            alarmText=item.find('alarmText').get_text("| ", strip=True)

            if item.find('highLimit') != None:
                highLimit=item.find('highLimit').get_text("| ", strip=True)
            else:
                highLimit='N/A'

            if item.find('lowLimit') != None:
                lowLimit=item.find('lowLimit').get_text("| ", strip=True)
            else:
                lowLimit='N/A'

            if item.find('deadband'):
                deadband=item.find('deadband').get_text("| ", strip=True)
            else:
                deadband='N/A'

            if item.find('lowLimitEnabled'):
                lowLimitEnabled=item.find('lowLimitEnabled').get_text("| ", strip=True)
            else:
                lowLimitEnabled='false'

            if item.find('highLimitEnabled'):
                highLimitEnabled=item.find('highLimitEnabled').get_text("| ", strip=True)
            else:
                highLimitEnabled='false'

            itemList=[pointName,pointPath,timeDelay,toOffnormal,toFault,toNormal,alarmText,highLimit,lowLimit,deadband,lowLimitEnabled,highLimitEnabled]
            dataList.append(itemList)

        self.df=pandas.DataFrame(dataList)
        self.df.columns=['pointName','pointPath','timeDelay','toOffnormal','toFault','toNormal','alarmText','highLimit','lowLimit','deadband','lowLimitEnabled','highLimitEnabled']
        return self.df
    def BACnet(self,soup):
        BACnetDevice = soup.find_all("node",class_='tridiumx.bacnet.objects.BACnetDevice')
        dataList=[]
        for item in BACnetDevice:
            instanceNumber=item.find('instanceNumber').get_text("| ", strip=True)
            objectName=item.find('objectName').get_text("| ", strip=True)
            networkNumber=item.find('networkNumber').get_text("| ", strip=True)
            macAddress=item.find('macAddress').get_text("| ", strip=True)

            itemList=[objectName,instanceNumber,networkNumber,macAddress]
            dataList.append(itemList)
        self.dfBACnet=pandas.DataFrame(dataList)
        self.dfBACnet.columns=['objectName','instanceNumber','networkNumber','macAddress']
        return self.dfBACnet
    def history(self,soup):
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

        self.dfHistory=pandas.DataFrame(dataList)
        self.dfHistory.columns=['pointName','bufferSize','interval','ChangeTolerance','units']
        return self.dfHistory
    def reportBuilder(self,excelName,alarms,histories,bacnet):
        self.alarms(self.soup)
        self.BACnet(self.soup)
        self.history(self.soup)
        path=excelName+'.xlsx'
        writer = pandas.ExcelWriter(path)
        if alarms == 1:
            self.df.to_excel(writer,sheet_name='Alarms')
            self.dfHistory.to_excel(writer,sheet_name='histories')
            self.dfBACnet.to_excel(writer,sheet_name='BACnet')

        writer.save()
