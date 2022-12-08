from bs4 import BeautifulSoup
import requests
import pandas as pd

# JAKARTA BARAT
url = 'https://id.wikipedia.org/wiki/Daftar_rumah_sakit_di_Kota_Jakarta_Barat'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',attrs={'class':"wikitable sortable"})

df = pd.read_html(str(rows))[0]

jakbar = df.drop('No.', axis=1)

jakbar.to_csv(r'./dataset/'+'JakartaBarat.csv')

# JAKARTA PUSAT
url = 'https://id.wikipedia.org/wiki/Daftar_rumah_sakit_di_Kota_Jakarta_Pusat'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',attrs={'class':"wikitable sortable"})

df = pd.read_html(str(rows))[0]

jakpus = df.drop('No.', axis=1)

jakpus.to_csv(r'./dataset/'+'JakartaPusat.csv')

# JAKARTA SELATAN
url = 'https://id.wikipedia.org/wiki/Daftar_rumah_sakit_di_Kota_Jakarta_Selatan'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',attrs={'class':"wikitable sortable"})

df = pd.read_html(str(rows))[0]

jaksel = df.drop('No.', axis=1)

jaksel.to_csv(r'./dataset/'+'JakartaSelatan.csv')

# JAKARTA TIMUR
url = 'https://id.wikipedia.org/wiki/Daftar_rumah_sakit_di_Kota_Jakarta_Timur'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',attrs={'class':"wikitable sortable"})

df = pd.read_html(str(rows))[0]

jaktim = df.drop('No.', axis=1)

jaktim.to_csv(r'./dataset/'+'JakartaTimur.csv')

# JAKARTA UTARA
url = 'https://id.wikipedia.org/wiki/Daftar_rumah_sakit_di_Kota_Jakarta_Utara'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',attrs={'class':"wikitable sortable"})

df = pd.read_html(str(rows))[0]

jakut = df.drop('No.', axis=1)

jakut.to_csv(r'./dataset/'+'JakartaUtara.csv')