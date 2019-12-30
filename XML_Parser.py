from bs4 import BeautifulSoup
import pandas as pd
import os

parsedInfo  = []    # To append media attributes for output

curDir = os.path.dirname(os.path.realpath(__file__))       # Finding the current directory

for root, dirs, files in os.walk(curDir):   # Walk the current directory and all its subfolders
    for eachFile in files:
        if eachFile.endswith('.xml'):           # Find all files ending with a .xml extension
            fileDirectory = os.path.join(root, eachFile)
            contents = open(fileDirectory, "r").read()
            xmlParser = BeautifulSoup(contents, 'xml')
            mediaFiles = xmlParser.find_all('MediaFile')    # Find each MediaFile tag
            for title in mediaFiles:                        # Traverse through each MediaFile tag's information
                try:
                    parsedInfo.append([title.attrs['bitrate'], title.attrs['width'], title.attrs['height'], title.attrs['type'], title.attrs['delivery'], title.get_text()])
                except:
                    parsedInfo.append([title.attrs['maxBitrate'], title.attrs['width'], title.attrs['height'], title.attrs['type'], title.attrs['delivery'], title.get_text()])

df = pd.DataFrame(parsedInfo)       # DataFrame construction
df.columns = ['Bitrate', 'Width', 'Height', 'Type', 'Delivery', 'Media_link']       # Adding DataFrame column names
df.to_csv("extractedMediaInformation.csv", encoding='utf-8')
df.to_excel("extractedMediaInformation.xlsx")