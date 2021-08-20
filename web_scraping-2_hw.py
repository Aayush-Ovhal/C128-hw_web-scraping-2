from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)

soup = BeautifulSoup(page.text, 'html.parser')

dwarfs = soup.find_all('table')

rows = dwarfs[4].find_all('tr')
temp_list = []
for tr in rows:
     td = tr.find_all('td')
     row = [i.text.rstrip() for i in td]
     temp_list.append(row)
print(temp_list)

dwarf_name = []
radius = []
mass = []
dist = []

for i in range(1, len(temp_list)):
     dwarf_name.append(temp_list[i][0])
     dist.append(temp_list[i][5])
     mass.append(temp_list[i][7])
     radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(dwarf_name, radius, mass, dist)), columns = ["Star", "Radius", "Mass", "Distance"])
print(df)
# df.to_csv("final_output.csv")