# In indeed where we search the job and its location then the URL becomes something like this https://in.indeed.com/jobs?q=”+job+”&l=”+Location
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.indeed.com/jobs?q=Data%20Engineer&l&vjk=460cce461bec5669")
soup = BeautifulSoup(page.content, 'html.parser')

dejob = soup.find(id= 'resultsBodyContent')

dejob.prettify()

detitle = [deti.get_text() for deti in dejob.select(".tapItem .jobTitle")]

desdesc = [desd.get_text() for desd in dejob.select(".tapItem .job-snippet")]

desal = [desa.get_text() for desa in dejob.select(".tapItem .salaryOnly")]

deloc = [delo.get_text() for delo in dejob.select(".tapItem .companyLocation")]

deconame = [deco.get_text() for deco in dejob.select(".tapItem .companyName")]

# print(detitle)
# print(desdesc)
# print(desal)
# print(deloc)
# print(deconame)

dataengineeringjobs = pd.DataFrame({
    "Title": detitle,
    "Short Description": desdesc,
    "Salary": desal,
    "Location": deloc,
    "Company Name": deconame
})
print(dataengineeringjobs)


"""Save as .csv file"""
dataengineeringjobs.to_csv("dataengineeringjobs.csv", index=False)


## If results are not of same length, use instead:
# dataengineeringjobs = {
#     "Title": detitle,
#     "Short Description": desdesc,
#     "Salary": desal,
#     "Location": deloc,
#     "Company Name": deconame
# }

# df = pd.DataFrame.from_dict(dataengineeringjobs, orient='index')
# df = df.transpose()
# print(df)

## to remove "\n" from results, add to code:
# df = df.replace('\n',' ', regex=True)



"""Test if indeed.py can be scheduled to run at date created"""
from datetime import datetime
now = datetime(2022, 2, 13, 14, 48) # date indeed jobs was extracted
dfs = dataengineeringjobs

with open('ischedule/indeed.txt', 'a')as f:
    f.write('{} : \n Output {}\n'.format(now, dfs))



"""Watch for changes in data using datetime.now"""
now = datetime.now()
dff = dataengineeringjobs

with open('ischedule/indeednow.txt', 'a')as f:
    f.write('{} : \n Output {}\n'.format(now, dff))



















