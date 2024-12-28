import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Users\tnayy\Downloads\chromedriver-win64')
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
