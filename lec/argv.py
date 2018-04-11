import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("Usage: python arg1 arg2")
    sys.exit()

regionCode = sys.argv[1]
rssUrl = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    "stnId": regionCode
}

params = parse.urlencode(values)

url = rssUrl + "?" + params

print("URL:", url)

data = req.urlopen(url).read()
text = data.decode("UTF-8")

print(text)
