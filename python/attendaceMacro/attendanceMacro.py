import selenium
from selenium import webdriver as wb
import time
# import info
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup as bs
url ='https://edu.ssafy.com'
f=open('info.txt','r',encoding='UTF-8')
id=f.readline().rstrip('\n').split(':')[1].strip().strip('"')
pw=f.readline().rstrip('\n').split(':')[1].strip().strip('"')
f.close()

driver =wb.Chrome()
driver.get(url)
try:
    assert '삼성 청년 SW 아카데미' in driver.title
    login_id = driver.find_element_by_css_selector('input#userId')
    login_pw = driver.find_element_by_css_selector('input#userPwd')
    login_btn=driver.find_element_by_css_selector('div.field-set.log-in > div.form-btn > a')
    login_id.send_keys(id)
    # login_pw.send_keys(pw)
    # login_pw.send_keys(Keys.RETURN)
    login_pw.send_keys(pw+'\n')
    # login_btn.click()
    # driver.quit()

    # attendance=driver.find_element_by_css_selector('')
    # attendance.click()
    print('출첵완료!!!')
    print('OK!!!')
except AssertionError:
    print('삼성 청년 SW 아카데미 page가 아닙니다.')
    print('not edu.ssafy.com page.')

except selenium.common.exceptions.InvalidSelectorException:
    print('출첵버튼이 없네요')
    print('can not find button')

except Exception as e:
    print(e)
finally:
    time.sleep(2)
    driver.quit()