from bs4 import BeautifulSoup
import requests
#Gathers wave hight and frequency from 3 Central Florida Beaches on any given sunday


def sundayCalc(): #Sunday must be found and scaped from page as the find in the other functions relies on this variable which changes per week
    source = requests.get('https://magicseaweed.com/Cocoa-Beach-Surf-Report/350/').text
    soup = BeautifulSoup(source, 'lxml')
    chart = str(soup.find('tbody').find_all("th"))
    day = "Sunday"
    #print(chart)
    occurences = chart.count(day) #this tells the program how many times to run
    first = chart.index(day) # start variable will be used to move through the occurences
    count = 0 #how many times the element has been found
    lst = [] #lst to attach results to
    while count < occurences-1:
        text = chart[chart.index(day,first):chart.index(day, first+1)]
        lst.append(text)
        first = chart.index(day, first+1)
        count += 1
    lstFirst = str(lst[0])
    global sunday
    sunday = lstFirst[0:10]
      

def sundayCocoaSurfReport():
    lst = []
    source = requests.get('https://magicseaweed.com/Cocoa-Beach-Surf-Report/350/').text
    soup = BeautifulSoup(source, 'lxml')
    chart = soup.find('tbody') #contains all information needed for output
    data = chart.find_all(attrs={"data-date-anchor": sunday}) #The Sunday Variable gather with the above function
    global dataString
    dataString = str(data)
    element = '<span class="h4 nomargin ">' #The element the data is in
    elementEnd = '</span>' #The end of the element to the data that I need
    occurences = dataString.count(element) 
    first = dataString.index(element)
    count = 0 
    while count < occurences-1:
        text = dataString[dataString.index(element,first):dataString.index(elementEnd, first+1)]
        lst.append(text)
        first = dataString.index(element, first+1)
        count += 1
        
    lstEdit = [s.replace('<span class="h4 nomargin ">', '') for s in lst]
    lstEdit = [s.replace('<small class="unit">', '') for s in lstEdit]
    lstEdit = [s.replace('</small> ', '') for s in lstEdit]
    global cocoabeachData
    cocoabeachData = lstEdit
    heightCounter = 2
    frequencyCounter = 3
    timeCounter = 3
    end = 11
    print('Cocoa Beach Surf Report')
    while True:
        print(str(timeCounter) + ':00 ' + cocoabeachData[heightCounter] + ' @ ' + cocoabeachData[frequencyCounter]) 
        timeCounter += 3
        frequencyCounter += 2
        heightCounter += 2
        if frequencyCounter == end:
            break
        
def sundaySateliteReport(): #Same as above function only page scraped is changed
    source = requests.get('https://magicseaweed.com/Satellite-Beach-Surf-Report/548/').text
    soup = BeautifulSoup(source, 'lxml')
    chart = soup.find('tbody')
    data = chart.find_all(attrs={"data-date-anchor": sunday})
    dataString = str(data)
    element = '<span class="h4 nomargin ">' 
    elementEnd = '</span>' 
    occurences = dataString.count(element) 
    first = dataString.index(element) 
    count = 0 
    lst = [] 
    while count < occurences-1:
        text = dataString[dataString.index(element,first):dataString.index(elementEnd, first+1)]
        lst.append(text)
        first = dataString.index(element, first+1)
        count += 1
        
    lstEdit = [s.replace('<span class="h4 nomargin ">', '') for s in lst]
    lstEdit = [s.replace('<small class="unit">', '') for s in lstEdit]
    lstEdit = [s.replace('</small> ', '') for s in lstEdit]
    cocoabeachData = lstEdit
    heightCounter = 2
    frequencyCounter = 3
    timeCounter = 3
    end = 11
    print('Sat Beach Surf Report')
    while True:
        print(str(timeCounter) + ':00 ' + cocoabeachData[heightCounter] + ' @ ' + cocoabeachData[frequencyCounter]) 
        timeCounter += 3
        frequencyCounter += 2
        heightCounter += 2
        if frequencyCounter == end:
            break

def sundayPonceInletReport():#Same as above function only page scraped is changed

    source = requests.get('https://magicseaweed.com/Ponce-Inlet-New-Smyrna-Surf-Report/348/').text
    soup = BeautifulSoup(source, 'lxml')
    chart = soup.find('tbody')
    data = chart.find_all(attrs={"data-date-anchor": sunday})
    dataString = str(data)
    element = '<span class="h4 nomargin ">' 
    elementEnd = '</span>' 
    occurences = dataString.count(element) 
    first = dataString.index(element) 
    count = 0 
    lst = [] 
    while count < occurences-1:
        text = dataString[dataString.index(element,first):dataString.index(elementEnd, first+1)]
        lst.append(text)
        first = dataString.index(element, first+1)
        count += 1
        
    lstEdit = [s.replace('<span class="h4 nomargin ">', '') for s in lst]
    lstEdit = [s.replace('<small class="unit">', '') for s in lstEdit]
    lstEdit = [s.replace('</small> ', '') for s in lstEdit]
    cocoabeachData = lstEdit
    heightCounter = 2
    frequencyCounter = 3
    timeCounter = 3
    end = 11
    print('New Smyrna Surf Report')
    while True:
        print(str(timeCounter) + ':00 ' + cocoabeachData[heightCounter] + ' @ ' + cocoabeachData[frequencyCounter]) 
        timeCounter += 3
        frequencyCounter += 2
        heightCounter += 2
        if frequencyCounter == end:
            break
    
def getThoseReports():    
    print('-------------------------')
    sundayCocoaSurfReport()
    print('-------------------------')
    sundaySateliteReport()
    print('-------------------------')
    sundayPonceInletReport()
    
sundayCalc()
getThoseReports()
