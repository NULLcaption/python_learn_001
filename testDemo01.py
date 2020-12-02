from urllib.request import urlopen
from urllib.request import Request
import random

def getContent(url, headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    # req =Request(url)
    # req.add_header("User-Agent", random_header)
    # req.add_header("GET",url)
    # req.add_header("Host","blog.csdn.net")
    # req.add_header("Referer","http://www.csdn.net/")

    header = {"User-Agent": random_header, "GET": url, "Host": "localhost:8088", "Referer": "http://localhost:8088/bootdo/"}
    req = Request(url, None, header)
    content = urlopen(req).read().decode("utf-8")
    return content


url = "http://localhost:8088/bootdo/production/production/productXpp"
my_headers = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36"]
print(getContent(url, my_headers))
