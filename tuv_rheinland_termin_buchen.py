from playwright.sync_api import sync_playwright ,Page, expect, Playwright
import time
from bs4 import BeautifulSoup

prüfung_stellen_NRW = [
    'krefeld',
    'Bergheim',
    'Düsseldorf',
    'Dormagen',
    'Brauweiler',
    'Köln',
    'Leverkusen',
    'Porz',
    'Bonn',
    'Euskirchen',
    'Rheinbach',
    'Siegburg',
    'Bornheim',
    'Brühl',
    'Bergisch Gladbach',
    'Wipperfürth',
    'Wuppertal',
    'Neuss',
    'Solingen',
    'Ratingen',
    'Willich-Münchheide',
    'Grevenbroich',
    'Mönchengladbach',
    'Nettetal',
    'Viersen',
    'Kempen',
    'Erkelenz',
    'Hückelhoven'
]

content = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
for stadt in prüfung_stellen_NRW:
    content += f"*************************************{stadt}******************************************"
    print(f"*************************************{stadt}******************************************")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(slow_mo=50)
            page = browser.new_page()
            page.goto('https://www.tuv.com/germany/de/termin-f%c3%bchrerschein/')
            page.locator('//*[@id="c-right"]/a[2]').click()
            page.fill('input#input_hutvLocation',stadt)
            page.keyboard.press('Enter')
            page.locator('//*[@id="main_content"]/div[2]/div/div[3]/div[1]/div/div[5]/div[2]/a').click()
            time.sleep(20)
            page.locator('//*[@id="main_content"]/div[2]/div/div[4]/div/div/div[2]/div[1]/div/div/label/span').click()
            time.sleep(10)
            html = page.inner_html('#ui-datepicker-div')
            #html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            Children = soup.find('tbody')
            chilldren = Children.find_all('tr')
            print("g")
            for child in chilldren:
                td_list = child.find_all('td', {'class' : ''})
                if td_list:

                    a_href = td_list[0].find('a').get_text()
                    month = soup.find('span', {'class' : 'ui-datepicker-month'}).get_text()

                    print(f'es gibt freiprüfung Termine am {a_href}-{month}-2023 in {stadt}')
                    content += f"es gibt freiprüfung Termine am {a_href}-{month}-2023 in {stadt}"
            print("**************************************************************************************")
            content += "**************************************************************************************"
    except Exception as e:
            pass
content = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print(content)