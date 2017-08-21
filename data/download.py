import wget

URL = 'http://www.properati.com.ar/data/static/data/AR/properati-AR-{0}-{1}-01-properties-sell.csv'

def get_csv(year, month):
  while year < 2018:
    while month <= 12:
      wget.download(URL.format(str(year), str(month).zfill(2)))
      month += 1
    year += 1
    month = 1

if __name__ == '__main__':
  get_csv(2013, 6)

