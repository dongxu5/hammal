import urllib.parse
import sys
class starturl:
    #明星对应的搬运号uid
    hammal_uids = {
        '鹿晗': '6336553953',
        "易洋千玺": "6341399232",
        "李易峰": "6336553963",
        "王俊凯": "6336553970",
        '张艺兴': '6341399271',
        "王源": "6336553989",
        "郑爽": "6336553996",
        "赵丽颖": "6336554005",
        "吴亦凡": "6341399316",
        "华晨宇": "6341399328",
        "杨洋": "6341399340",
        "刘诗诗": "6336554029",
        "薛之谦": "6341399372",
        "陈伟霆": "6341399382",
        "李宇春": "6341399394",
        "tfboys": "6336554047",
        "杨幂": "6336554052",
        "钟汉良": "6341399436",
        "林更新": "6341399452",
        "宋茜": "6341399464",
        "白敬亭": "6341399485",
        "王凯": "6336554087",
        "许魏洲": "6336554097",
        "马天宇": "6336554107",
        "王嘉尔": "6341399562",
        "张杰": "6341399579",
        "黄景瑜": "6341399603",
        "刘涛": "6336554148",
        "黄子韬": "6341399642",
        "刘亦菲": "6336554166",
        "邓紫棋": "6336554180",
        "唐嫣": "6336554195",
        "胡歌": "6336554207",
        "陈学冬": "6341399759",
        "靳东": "6336554217",
        "李艺彤": "6341399809",
        "大张伟": "6336554247",
        "刘昊然": "6341399827",
        "吴磊": "6341399844",
        "张翰": "6341399859",
        "陈乔恩": "6336554268",
        "潘玮柏": "6341399886",
        "罗志祥": "6336554282",
        "杨紫": "6336554289",
        "张一山": "6341399928",
        "周冬雨": "6336554310",
        "鞠婧祎": "6341399961",
        "黄婷婷": "6336554316",
        "Angelababy杨颖": "6341399993",
    }

    #组装搜索起始的url
    def assemblUrl(self, website):
        search_url = []
        if website == 'bili' :
            for name in self.hammal_uids.keys():
                url = "https://search.bilibili.com/video?keyword=" + urllib.parse.quote(name) + "&page=1&order=pubdate&duration=1"
                search_url.append(url)
        elif website == 'youku':
            for name in self.hammal_uids.keys():
                url = "http://www.soku.com/search_video/q_" + urllib.parse.quote(name) + "_orderby_2_limitdate_1?spm=a2h0k.8191407.0.0&site=14&_lg=10&lengthtype=1"
                search_url.append(url)
        elif website == 'iqiyi':
            for name in self.hammal_uids.keys():
                url = "http://so.iqiyi.com/so/q_" + urllib.parse.quote(name) + "_ctg__t_2_page_1_p_1_qc_0_rd_1_site__m_1_bitrate_?af=true"
                search_url.append(url)
        elif website == 'qq':
            for name in self.hammal_uids.keys():
                url = "https://v.qq.com/x/search/?ses=qid%3Dg1QK4t2UldEuFXzOd2q5Rn4ezBKY67cCUpyMyfH34t30wYAAXLnjgw%26last_query%3D" + urllib.parse.quote(name) + "%26tabid_list%3D0%7C12%7C3%7C7%7C2%7C1%7C5%7C17%26tabname_list%3D%E5%85%A8%E9%83%A8%7C%E5%A8%B1%E4%B9%90%7C%E7%BB%BC%E8%89%BA%7C%E5%85%B6%E4%BB%96%7C%E7%94%B5%E8%A7%86%E5%89%A7%7C%E7%94%B5%E5%BD%B1%7C%E9%9F%B3%E4%B9%90%7C%E6%B8%B8%E6%88%8F&q=" + urllib.parse.quote(name) + "&stag=4&filter=sort%3D2%26pubfilter%3D1%26duration%3D1%26tabid%3D0#!filtering=1"
                search_url.append(url)
        else:
            pass
        return search_url

    #解析url中的keyword
    def parseUrl(self, link, website):
        if website == "iqiyi":
            find_start_str = "/q_"
            find_end_str = "_ctg_"
        elif website == "bili":
            find_start_str = "keyword="
            find_end_str = "&page="
        elif website == "youku":
            find_start_str = "/q_"
            find_end_str = "_orderby_"
        elif website == "qq":
            find_start_str = "&q="
            find_end_str = "&stag="
        else:
            find_start_str = ""
            find_end_str = ""
        start = link.find(find_start_str)
        length = find_start_str.__len__()
        start_index = start + length
        #判断结束字符串有没有
        if find_end_str == "":
            end = ""
        else :
            end = link.find(find_end_str)
        if end == "":
            keyword = link[start_index]
        else:
            keyword = link[start_index:end]
        keyword = urllib.parse.unquote(keyword)
        return keyword

#测试使用
if __name__ == '__main__':
   surl = starturl()
   url = surl.assemblUrl('youku')
   print(url)
   url = surl.assemblUrl('iqiyi')
   print(url)
   url = surl.assemblUrl('bili')
   print(url)
   url = surl.assemblUrl('qq')
   print(url)
   sys.exit()