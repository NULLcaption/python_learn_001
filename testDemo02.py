import urllib.request

url = "http://localhost:8088/bootdo"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer': 'localhost:8088' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

print(data)