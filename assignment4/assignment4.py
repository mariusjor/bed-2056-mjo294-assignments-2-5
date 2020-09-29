from bs4 import BeautifulSoup
import pandas as pd
from requests import get
from time import sleep
from random import randint
import datetime

url = "http://timeplan.uit.no/emne_timeplan.php?sem=20h&module%5B%5D=BED-2056-1&View=list"

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Create an empty data frame
df = pd.DataFrame(columns=['Dato', 'Tid', 'Rom', 'Emnekode', 'Beskrivelse', 'Lærer'])

course_tables = html_soup.find_all('tr', class_='table-primary')

# Iterate each course table
for table in course_tables:

    tds = table.find_all('td')

    # Extract and format date
    date = str(tds[0])
    date = date.replace('<td>', '').replace('</br></td>', '')
    date = date.split('<br>')[-1]
    date = datetime.datetime.strptime(date, '%d.%m.%Y')

    # Create a data frame row using the data in the table
    new_row = {'Dato':date.date(), 'Tid':tds[1].text, 'Rom':tds[2].text, 'Emnekode':tds[3].text, 'Beskrivelse':tds[4].text, 'Lærer':tds[5].text}
    
    # Append the row to the dataframe
    df = df.append(new_row, ignore_index=True)

# Save the dataframe to csv
df.to_csv('timetable.csv', index=False)
