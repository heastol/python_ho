import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=O26wyq4tzZwKro5mW5ZfS9ajcvuzTn3z&data=AP01'
res = requests.get(url).text
data = json.loads(res)
result = data[-1]['deal_bas_r']
result1 = result.replace(",","").replace(".","")
result2 = int(result1) / 10
print(f'오늘의 환율은 1달러에 {result2}원 입니다.')
