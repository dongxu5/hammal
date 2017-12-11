#!/bin/env python
# coding:utf-8
import os
import json
import hashlib
from log import logger
from upload import uploadFileV2
from download import DownloadVideo
import sys

dir = os.path.dirname(os.getcwd()) + '/bilibili'

if __name__ == '__main__':
    uf = uploadFileV2()
    dv = DownloadVideo()
    names = ["youku.json","bilibili.json","iqiyi.json","qq.json"]
    for name in names:
        with open(dir+'/'+name, mode='r', encoding='utf-8') as f:
            for line in f:
                detail = json.loads(line.rstrip())
                name = hashlib.md5(detail['title'].encode()).hexdigest()
                try:
                    dv.download(name,detail['link'])
                    st1 = 0
                    logger.info(detail['link']+" download succ")
                except Exception as e:
                    st1 = 1
                    logger.info(detail['link']+" download failed")
                if st1 == 0:
                    try:
                        fid = uf.upload(name+".mp4")
                        st2 = 0
                        logger.info(detail['link']+" upload succ")
                        os.system( "rm -f *.mp4 *.xml")
                    except Exception as e:
                        st2 = 1
                        logger.info(detail['link']+" upload failed")
                    if st2 == 0:
                        try:
                            info = uf.transfer_data(fid,line.rstrip())
                            if info['code'] == 10000:
                                logger.info(detail['link']+" transfer succ")
                            else:
                                logger.info(detail['link']+" transfer failed")
                        except Exception as e:
                            logger.info(detail['link']+" transfer error")
                    else:
                        pass
                else:
                    pass
