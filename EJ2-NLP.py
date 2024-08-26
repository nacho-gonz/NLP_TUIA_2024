import requests
from bs4 import BeautifulSoup

url = 'https://tableros.yvera.tur.ar/tablero_ODS/'

response = requests.get(url, verify=False).text

cont_html = BeautifulSoup(response, 'html.parser')

primeros_div = cont_html.find_all('div', {'class':'row'})
cant_divs = 0
cant_s_divs = 0

for div_p in primeros_div:
    if cant_divs == 2:
        segundos_div = div_p.find_all('div', {'class':'col-sm-4'})
        for div_s in segundos_div:
            texto = div_s.find('div', {'class':'small-box bg-navy'}).find('div',{'class':'inner'}).find('p',{'style':'font-size: 140%;'}).text
            numero = div_s.find('div', {'class':'small-box bg-navy'}).find('div',{'class':'inner'}).find('h3').find('p').text
            print(texto + numero)
    if cant_divs == 4:
        segundos_div = div_p.find_all('div', {'class':'col-sm-4'})
        cant_s_divs += 1
        for div_s in segundos_div:
            if cant_s_divs == 0:
                texto = div_s.find('div', {'class':'small-box bg-red'}).find('div',{'class':'inner'}).find('p',{'style':'font-size: 110%;'}).text
                numero = div_s.find('div', {'class':'small-box bg-red'}).find('div',{'class':'inner'}).find('h3').find('p').text
            elif cant_s_divs == 1:
                terceros_divs = div_s.find('div').find_all('div')
            else:
                texto = div_s.find('div', {'class':'small-box bg-aqua'}).find('div',{'class':'inner'}).find('p',{'style':'font-size: 120%;'}).text
                numero = div_s.find('div', {'class':'small-box bg-aqua'}).find('div',{'class':'inner'}).find('h3').find('p').text
            print(texto + numero)
    
    cant_divs += 1