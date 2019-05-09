import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

# コマンドライン引数を受け取る
words = sys.argv
# 第二引数をwordに格納
word = words[1]

print('"' + word + '"' + 'で検索...')
print('----------------------------------------------')

# setting user agent
ua = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
]
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# init Options
options = Options()
options.add_argument('-headless')
options.add_argument('-user-agent=' + ua[0])

geckodriver = 'geckodriver'

# set Options / chromedriver
driver = webdriver.Firefox(firefox_options=options)
# set window size
driver.set_window_size(450, 3320)
# set default wait
driver.implicitly_wait(6)

# go to URL
driver.get('https://www.google.com/search?ie=UTF-8&ibp=htl;jobs&htivrt=jobs&q=' + word)
# wait for rendering
time.sleep(5)

elements = driver.find_elements_by_css_selector('.tab-sel ul > li')
# print(elements)

if elements:
    for i, li in enumerate(elements):
        h1 = li.find_element_by_css_selector('.gsrt').text
        print(str(i+1) + '位 ' + h1)
        for item in li.find_elements_by_css_selector('.gsrt + div > div'):
            print('- ' + item.text.replace('\n', '、'))
        print('----------------------------------------------')
    driver.save_screenshot('sr_' + now +'.png')
else:
    print('要素がありませんでした...')

driver.quit()
