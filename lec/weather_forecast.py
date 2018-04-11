import urllib.request
import urllib.parse

rssUrl = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#stnId -> 108: 전국, 109: 서울/경기, 105: 강원, 131: 충북
#           133: 충남, 146: 전북, 156: 전남, 143: 경북
#           159: 경남, 184: 제주
values = {
    "stnId": "146"
}

params = urllib.parse.urlencode(values)

url = rssUrl + "?" + params

print("URL:", url)

data = urllib.request.urlopen(url).read()
text = data.decode("UTF-8")

print(text)
