# -*- coding: utf-8 -*-
import os
import http.client
import time
import hashlib
import datetime
import hmac
import json
import base64
import urllib.request
import urllib.parse
from log import logger
import sys


class uploadFileV2:
    source = 3688815048
    verb = 'POST'

    def transfer_data(self, fid, exData=None):
        Data = json.loads(exData)
        Data['fid'] = fid
        exData = json.dumps(Data, ensure_ascii=False)
        args = {}
        args['source'] = Data['source']
        args['uid'] = Data['uid']
        args['info'] = exData
        encode_args = urllib.parse.urlencode(args)
        proxy_support = urllib.request.ProxyHandler({'http': '10.13.131.86:80'})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        url = "http://i.hammal.service.starvip.weibo.com/Huanlesong/Addvideo"
        req = urllib.request.Request(url, encode_args.encode())
        req.get_method = lambda: self.verb
        conn = urllib.request.urlopen(req)
        response = conn.read().decode()
        info = json.loads(response)
        return info

    def hmacSignature(self, tauth_token_secret, param_str):
        h = hmac.new(tauth_token_secret.encode(), param_str.encode(), hashlib.sha1)
        s = h.digest()
        return base64.b64encode(s).rstrip()

    def createAuthHeader(self, token, param, sign):
        m = {'token': token, 'param': param, 'sign': sign}
        arr = urllib.parse.urlencode(m).split('&')
        authorizationHeader = "TAuth2 "
        for value in arr:
            pair = value.split("=")
            authorizationHeader += pair[0] + "=\"" + pair[1] + "\","
        return authorizationHeader[0: len(authorizationHeader) - 1]

    def getToken(self):
        url = 'http://i.service.starvip.weibo.com/api/common/gettauthtoken?source=3688815048'
        res = json.loads(urllib.request.urlopen(url).read().decode())
        return res['data']

    def upload(self, filePath):
        body = ''
        with open(filePath, 'rb') as fp:
            body = fp.read()
        fp.close()
        fid = ''
        if body:
            md5 = hashlib.md5(body).hexdigest()
            fsize = os.path.getsize(filePath)
            params = {'source': self.source, 'name': os.path.basename(filePath), 'check': md5, 'length': fsize,
                      'type': 'video'}
            encode_params = urllib.parse.urlencode(params)
            token_data = json.loads(self.getToken())
            token = token_data['tauth_token']
        
            sign = self.hmacSignature(token_data['tauth_token_secret'], 'uid=6284677270')
            authorization = self.createAuthHeader(token, 'uid=6284677270', sign)
            headers = {'Authorization': authorization}
            req = urllib.request.Request('http://i.multimedia.api.weibo.com/2/multimedia/init.json',
                                         encode_params.encode(), headers=headers)
            f = urllib.request.urlopen(req)
            result = json.loads(f.read().decode())
            logger.info(result)

            if 'fileToken' in result:
                print('Initialize task successfully.')
                logger.info('Initialize task successfully.')
                filetoken = result['fileToken']
                # Upload content
                slice_size = (float)(result['length'] * 1024)
                slice_count = (int)(fsize / slice_size + 1)
                slice_left = fsize % slice_size
                fp = open(filePath, 'rb')
                for i in range(slice_count):
                    pointer = i * slice_size
                    read_size = 0
                    if i == slice_count - 1:
                        read_size = slice_left
                    else:
                        read_size = slice_size
                    content = fp.read((int)(read_size))
                    slice_md5 = hashlib.md5(content).hexdigest()
                    args = {'source': self.source, 'check': md5, 'filelength': fsize, 'sectioncheck': slice_md5,
                            'startloc': (int)(i * slice_size), 'filetoken': filetoken}
                    encode_args = urllib.parse.urlencode(args)
                    url = "http://i.multimedia.api.weibo.com/2/multimedia/upload.json?%s" % encode_args
                    req = urllib.request.Request(url, data=content, headers=headers)
                    req.get_method = lambda: self.verb

                    # Retry times:2
                    success = True
                    for j in range(2):
                        try:
                            conn = urllib.request.urlopen(req, timeout=15)
                            response = conn.read()
                            info = json.loads(response.decode())
                            if i == slice_count - 1:
                                if 'fid' in info:
                                    logger.info(info)
                                    fid = info['fid']
                                break
                            else:
                                if info['succ'] == True:
                                    success = True
                                    break
                                else:
                                    success = False
                                    print('Failed to upload content. Info=%s' % info)
                                    logger.info('Failed to upload content. Info=%s' % info)
                        except Exception as exec:
                            success = False
                            print("connection error(%s)" %
                            exec)

                            if not success:
                                print('Failed to upload video')
                                break
                        fp.close()

                return fid

        if __name__ == '__main__':
            uf = uploadFileV2()

