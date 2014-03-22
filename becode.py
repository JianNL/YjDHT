#!/usr/bin/env python
# coding=utf-8
#Author : yj 
#Created Time: 2014年03月22日 星期六 11时32分04秒
#File Name:becode.py
######################################################
'''
完成BENCODE的编码以及解码
'''


class bencode():
    '''
    bencode 的封装类
    '''
    def __init__(self):
        '''

        '''
        #解码操作
        self.decodeop={
            'i':self.decodeOpDig,
            '0':self.decodeOpStr,
            '1':self.decodeOpStr,
            '2':self.decodeOpStr,
            '3':self.decodeOpStr,
            '4':self.decodeOpStr,
            '5':self.decodeOpStr,
            '6':self.decodeOpStr,
            '7':self.decodeOpStr,
            '8':self.decodeOpStr,
            '9':self.decodeOpStr,
            'l':self.decodeOpLst,
            'd':self.decodeOpDic
        }
        #编码操作
        self.encodeop={
            "<type 'dict'>":self.encodeOpDic,
            "<type 'int'>":self.encodeOpDig,
            "<type 'str'>":self.encodeOpStr,
            "<type 'list'>":self.encodeOpLst
        }


    def encode(self,code):
        '''
        bencode编码
        '''
        pass

    def encodeOpDig(self,dig):
        '''
        对数字进行bencode编码,并返回
        '''
        return 'i%de'%dig

    def encodeOpStr(self,str):
        '''
        对字符串进行bencode编码，并返回
        '''
        return '%d:%s'%(len(str),str)


    def encodeOpLst(self,lst):
        '''
        对list进行编码
        '''
        re='l'
        for i in lst:
            re=re+self.encodeop.get(str(type(i)))(i)
        return re+'e'


    def encodeOpDic(self,dic):
        '''
        对dic进行编码
        '''
        re='d'
        for key in dic:
            re=re+self.encodeop.get(str(type(key)))(key)
            re=re+self.encodeop.get(str(type(dic[key])))(dic[key])
        return re+'e'

    def decode(self,code):
        '''
        bencode解码
        '''
        return self.decodeop.get(code[0])(code)

    def decodeOpDig(self,code):
        '''
        code头部是个数字，处理返回数字，并且返回下个头开始.
        '''
        i=1
        while code[i]!='e':
            i=i+1
        digit=int(code[1:i])
        return digit,code[i+1:]

    def decodeOpStr(self,code):
        '''
        code头部是个字符串,处理返回该字符串，并且返回下个头部
        '''
        i=0
        while code[i]!=':':
            i=i+1
        #i现在指示冒号的位置
        lenOfStr=int(code[:i])
        #i现在指示字符串第一个的位置.
        i=i+1
        return code[i:i+lenOfStr],code[i+lenOfStr:]

    def decodeOpLst(self,code):
        '''
        code头部是个list，处理返回该list，并且返回下个头部
        '''
        #用来存储该list
        l=[]
        code=code[1:]
        while code[0]!='e':
            re,code=self.decodeop.get(code[0])(code)
            l.append(re)
        return l,code[1:]


        

    def decodeOpDic(self,code):
        '''
        code头部是个dict，处理返回dict，并且返回下个头部
        '''
        #用来存储dict
        d={}
        code=code[1:]
        while code[0]!='e':
            #返回Key
            rekey,code=self.decodeop.get(code[0])(code)
            revalue,code=self.decodeop.get(code[0])(code)
            d[rekey]=revalue
        return d,code[1:]

    def getinfohash(self,torrentfilename):
        '''
        从torrent文件得到infohash
        '''
        pass
    
    def decodeFromTorrentFile(self,torrentfilename):
        '''
        对torrent文件进行bencode解码
        '''
        pass


if __name__=='__main__':
    code='d1:eli201e20:AGenericErrorOcurrede1:t2:aa1:y1:ee'
    b=bencode()
    print b.decode(code)
    print b.encodeOpDig(123)
    print b.encodeOpStr('helloworld')
    print b.encodeOpLst([1,'fdfdfdf'])
    print b.encodeOpDic({1:'fsdfasdf','abc':[1,'dfdfdf']})
