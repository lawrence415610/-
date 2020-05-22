import requests
import operator
from functools import reduce

searchTerm = "黑丝"

query = "?query={}&limit=60".format(searchTerm)
url = "https://rabtman.com/api/v2/acgclub/pictures" + query

response = requests.get(url).json()
newArr = []
for ele in response['data']:
    newArr.append(ele['imgUrls'])
newArr = reduce(operator.add, newArr)

for index,ele in enumerate(newArr):
    downloadImg = requests.get(ele)
    with open('./img-{}.jpg'.format(index), 'wb') as f:
        f.write(downloadImg.content)



