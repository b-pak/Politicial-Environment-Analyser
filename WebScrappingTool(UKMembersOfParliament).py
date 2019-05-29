import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Request data from page
page = requests.get("https://www.parliament.uk/mps-lords-and-offices/mps/")
soup = BeautifulSoup(page.content, 'html.parser')

# Define global variables
firstname = []
surname = []
party = []

# Scrap data from specific sections of the page
for i in range(9):
    name = 'ctl00_ctl00_FormContent_SiteSpecificPlaceholder_PageContent_rptMembers_ctl0' + str(i+1) + '_tdNameCellLeft'
    results = soup.find(id=name).get_text()
    results_new = " ".join(results.split())
    split = re.split(',', results_new)
    firstname.append(split[0])
    surname.append(re.sub(r'\(.*\)', '', split[1]).strip())
    party.append(re.findall(r'\((.*?)\)', results_new))
for i in range(640):
    name = 'ctl00_ctl00_FormContent_SiteSpecificPlaceholder_PageContent_rptMembers_ctl' + str(i + 10) + '_tdNameCellLeft'
    results = soup.find(id=name).get_text()
    results_new = " ".join(results.split())
    split = re.split(',', results_new)
    firstname.append(split[0])
    surname.append(re.sub(r'\(.*\)', '', split[1]).strip())
    party.append(re.findall(r'\((.*?)\)', results_new))

# Construct DataFrame and print out table
MP = pd.DataFrame({
'First Name': firstname,
'Surname': surname,
'Party': party,
})
print(MP)
