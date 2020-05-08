import pandas as pd

import requests

def get_optstk_history(inst,strike_price,opt_type,fromdate,todate):
    headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    }
    params = (('instrumentType', 'OPTIDX'),
    ('symbol', inst),
    ('expiryDate', 'select'),
    ('optionType', opt_type),
    ('strikePrice', strike_price),
    ('dateRange', 'day'),
    ('fromDate', fromdate),
    ('toDate', todate),
    ('segmentLink', '9'),
    ('symbolCount', ''),
    )
    response = requests.get('https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp', headers=headers, params=params)
    try:
        opthistdf = pd.read_html(response.text,flavor='lxml',skiprows=1,header=0)[0]
        print (type(opthistdf))
    except:
        opthistdf = pd.DataFrame()
    return opthistdf

strikePrices = [19500]
stock = 'BANKNIFTY'
startDate = '01-05-2020'
endDate = '07-05-2020'
optionType = 'CE'

for x in strikePrices:
    filename = str(x) + 'BN.csv'
    optdf = get_optstk_history(stock ,x, optionType, startDate, endDate)
    optdf.to_csv(filename, sep=',')




