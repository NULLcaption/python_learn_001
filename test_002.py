from suds.client import Client


def test():
    try:
        # qingqing
        str1 = 'https://qinqing.hangzhou.gov.cn/qqzx-centre/services/callback?wsdl'
        # fujian
        str2 = 'http://60.205.206.111:805/WebServiceCC.asmx?wsdl'
        client = Client(str1)
        print(client)
    except Exception as e:
        print('SenderClass running cyle: {:s}'.format(str(e)))


if __name__ == '__main__':

    try:
        test()
    except Exception as e:
        print('SenderClass running cyle: {:s}'.format(str(e)))
