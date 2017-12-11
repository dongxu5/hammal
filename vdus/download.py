import sys
from you_get import common as you_get

class DownloadVideo:

    def download(self,name,link):
    	sys.argv=['you-get','-O',name,'--format=mp4sd',link]
    	you_get.main()

if __name__ == '__main__':
    dv=DownloadVideo()
    dv.download('http://v.youku.com/v_show/id_XMjg3OTc3NjAwNA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2')
