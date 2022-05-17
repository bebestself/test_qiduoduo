import unittest,requests,re,time
from lxml import etree

class TestWeb(unittest.TestCase):
    '''
    爬取百度首页相关标签属性值
    '''
    def setUp(self):
        self.url = 'https://www.baidu.com/'
        self.expect = '//www.baidu.com/img/bd_logo1.png'

    def test_html(self):
        resp = requests.get(self.url)
        res_time = float(resp.elapsed.total_seconds())
        #获取请求的响应时间，单位为秒
        resp.encoding = 'utf8'
        # html = resp.text
        # res = re.findall("<div id=lg>(.*?)>",html)
        # resu= re.findall("src=(.*?) width",str(res))
        # print(resu)
        #通过正则提取属性值
        html = etree.HTML(resp.text)
        res = html.xpath('//div[@id="lg"]/img/@src')
        print(res)
        #通过lxml提取属性值
        self.assertGreater(1,res_time)
        #断言相应时间小于1s
        self.assertEqual(self.expect,*res)
        #断言返回值，上面返回为列表，需进行解包


if __name__ == '__main__':
    unittest.main()
