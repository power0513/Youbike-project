#下載youbike.csv資料
import requests, json
import pandas as pd

url='https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
fn = 'youbike.csv'
response= requests.get(url)
ybike = json.loads(response.text)
#下面是orient是資料方向，index是將字典鍵當索引
df = pd.DataFrame.from_dict(ybike['retVal'],orient='index')
df.to_csv(fn, index=False, encoding='utf-8')

