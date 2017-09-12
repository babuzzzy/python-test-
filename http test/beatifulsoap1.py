html_doc = """
<html><head><title>The Dormouse's story </title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
