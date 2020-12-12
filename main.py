from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import yaml

base_url = 'https://bioinfo.ut.ee/primer3-0.4.0/'

with open('gene.txt', 'r', encoding='utf-8') as f:
    a = f.read()
print(a)

ff = open('name_settings.yml', 'r', encoding='utf-8')
sts = yaml.load(ff)
print(sts)
ff.close()

chrome_options = Options()
#chrome_options.add_argument("--headless")
# 对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=(r'D:\pyauto\primer3\chromedriver.exe'), options=chrome_options)
driver.implicitly_wait(10)
driver.get(base_url)
driver.find_element_by_xpath('/html/body/form/p[4]/textarea').send_keys(a)

for i in sts.keys():
    driver.find_element_by_name(i).clear()
    driver.find_element_by_name(i).send_keys(str(sts[i]))
driver.find_element_by_xpath('/html/body/form/p[7]/input[1]').click()
time.sleep(5)

res = driver.find_element_by_xpath('/html/body/pre[1]')
with open('result.txt','w',encoding='utf-8') as result:
    result.write(res.text)
print(res.text)

driver.close()
