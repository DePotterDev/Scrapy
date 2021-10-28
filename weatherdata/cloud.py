from requests_html import HTMLSession

s = HTMLSession()

query = 'são paulo'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0'})

temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(query, temp, unit, desc)