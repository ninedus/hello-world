from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">네이버</a></li>
        <li><a href="http://www.daum.com">다음</a></li>
    </ul>
</body>
</html>
"""

#html 분석하기
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links:
    text = a.string
    print(text, a.attrs['href'], type(a.attrs))

