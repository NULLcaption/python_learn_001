import json
import re
import scrapy
from scrapy import Request


class BraSpider(scrapy.Spider):
    name = 'bra'

    headers = {
        ":authority": "sclub.jd.com",
        ":method": "GET",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language:": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "cookie": "__jdu=1532074141621235407991; shshshfpa=30d0ea4e-dfe5-9ec6-35e3-852573050d5a-1532399778; "
                  "shshshfpb=0ab39c304f61a336e0540239a14c94d24a079d919c9c598305b5198a0b; "
                  "3AB9D23F7A4B3C9B"
                  "=GG3YPOONOR5XPLOIVVP7N27ZJDXCXULS2UDPYO7O6A5XRZE274NXQEATHIXZP5EZV4RQKBRE5FDKTMXRWSDQNK326A; "
                  "_jrda=1; shshshfp=9ed19b6b00b641b920767cc4d13bd8e9; user-key=e6eeb195-aaab-4242-9cd1-c1b0e6fa7441; "
                  "cn=0; __jda=122270672.1532074141621235407991.1532074142.1539585275.1539676870.7; __jdc=122270672; "
                  "__jdv=122270672|baidu|-|organic|not set|1539676869852; "
                  "cid=NWFNNjkyNmJGMTk0N2xBODcyOGNNOTc0MXRBNzcwMndZODcwM3dHMzcyNGdDODU0; "
                  "wlfstk_smdl=pswusyq5mzpsddnmc8iyupfbvpdkia97; "
                  "TrackID=17UdPK9O5vzzJpg65dXbqHy4EFc_aQhrJ8Qeysh8NmLXDNrtrMusiFod"
                  "-TdpKhOOtsp05prZ9HqsbiUTiqkArX7EFb_lsCu17V7YdAmNux5E; pinId=fCaG1mIQHB91jW13U2S7SQ; "
                  "pin=wduheoQGxRraeI; unick=CheneyMaster; ceshi3.com=000; _tp=gkXfB57TrZJ1eQ6DHJTJ4w%3D%3D; "
                  "_pst=wduheoQGxRraeI; areaId=15; ipLoc-djd=15-1158-1224-0; "
                  "shshshsID=daf206df37ef85060fdc0144cbe0ceec_1_1539677029193; juinfo=56%7C1990%7C0; "
                  "__jdb=122270672.10.1532074141621235407991|7.1539676870; "
                  "thor"
                  "=C2B9A3852F9608AFB6EDEF7336B8237E76AF39597A0957EA8CDCA723D86AF9305218D0AA24DBA93E44314DDA49CFF1A2CBBCE2786E936F353F44A3404F1396CA2A0A0345F4A172C766AA92447DE35C4D8266CFCC9D8AE81D8E0CD06999D08CB81E8F6F9FC10F92FE607B48C7E3E7C521546672D0BD62FE185FE017D5FB17035F470C3A901365462D02AA386A84E406E7",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.33 Safari/537.36",
    }

    base_url = "https://sclub.jd.com/comment/productPageComments.action?" \
               "callback=fetchJSON_comment98vv218" \
               "&productId=5973709" \
               "&score=0" \
               "&sortType=5" \
               "&page=0" \
               "&pageSize=10" \
               "&isShadowSku=0" \
               "&fold=1 "

    def start_requests(self):
        for page in range(1, 100):
            url = self.base_url % page
            print(url)
            self.headers[':path'] = url
            yield Request(url, self.parse, headers=self.headers)
            # time.sleep(2)

    def parse(self, response):
        content = json.loads(response.text)
        comments = content['comments']
        for comment in comments:
            item = {}
            item['content'] = comment['content']  # 评论正文
            item['guid'] = comment['guid']  # 用户id
            item['id'] = comment['id']  # 评论id
            item['time'] = comment['referenceTime']  # 评论时间
            item['color'] = self.parse_kuohao(comment['productColor'])  # 商品颜色
            item['size'] = self.parse_kuohao(comment['productSize'])  # 商品尺码
            item['userClientShow'] = comment['userClientShow']  # 购物渠道
            print(item)
            yield item

    # 干掉括号
    def parse_kuohao(self, text):
        new_text = text
        searchObj1 = re.search(r'（.+）', text, re.M | re.I)
        searchObj2 = re.search(r'\(.+\)', text, re.M | re.I)
        if searchObj1:
            text = searchObj1.group().strip()
            new_text = text.replace(text, '').strip()

        if searchObj2:
            text = searchObj2.group().strip()
            new_text = text.replace(text, '').strip()

        return new_text
