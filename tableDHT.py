#!/usr/bin/env python
# coding=utf-8
#Author : yj 
#Created Time: 2014年03月22日 星期六 20时43分44秒
#File Name:tableDHT.py
######################################################

class Node(object):
    '''
    Table中bucket的node结构
    '''
    __slot__=('nodeid','ip','port')

    def __init__(self,nodeid,ip,port):
        '''
        构造函数
        '''
        self.nodeid=nodeid
        self.ip=ip
        self.port=port

    def __eq__(self,other):
        '''
        判断两节点信息是否相同
        '''
        return self.nodeid==other.nodeid


class Bucket(object):
    '''
    K桶数据结构,桶中最大节点数量为k
    id的分布范围从0~2^160
    所以桶有一个范围
    初始桶的范围就是0~2^160
    但如果桶中数量超过k，桶会根据情况分裂
    '''
    __slot__=['min','max','nodes']
    def __init__(self,min,max):
        '''
        构造函数
        '''
        self.min=min
        self.max=max
        self.nodes=[]

    def append(self,node):
        '''
        向桶中添加一个Node
        '''
        if node in self.nodes:
            #如果已经存在,则更新
            self.nodes.remove(node)
            self.nodes.append(node)
        else:
            #如果桶已经满了
            if len(self.nodes)>=8:
                pass
                #待处理
            else:
                self.nodes.append(node)
                
    def remove(self,node):
        '''
        从桶中删除一个节点
        '''
        if len(self.nodes)>0:
            self.nodes.remove(node)
        else:
            pass

    def __len__(self):
        return len(self.nodes)

    def __contains__(self,node):
        return node in self.nodes

    def __iter__(self):
        for i in self.nodes:
            yield i

    def __lt__(self,other):
        return self.max<=other.max
    


class Table(object):
    '''
    每个节点都维护了一个Table的结构,这个结构是由很多桶组成的。
    初始化时只有一个桶
    '''
    def __init__(self,id):
        '''
        id是每个要加入DHT网络中必须要有的
        buckets是所有bucket的集合
        '''
        self.id=id
        #初始化时只有一个桶
        self.buckets=[Bucket(0,2**160)]
