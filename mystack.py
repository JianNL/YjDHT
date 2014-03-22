#!/usr/bin/env python
# coding=utf-8
#Author : yj 
#Created Time: 2014年03月21日 星期五 22时10分32秒
#File Name:mystack.py
######################################################
class mystack():
    '''
    自定义堆栈  
    '''
    def __init__(self):
        '''
        构造器
        '''
        self.array=[]

    def push(self,data):
        '''
        压栈
        '''
        self.array.append(data)
        
    def len(self):
        '''
        得到栈的大小
        '''
        return len(self.array)

    def isempty(self):
        '''
        栈是否为空
        '''
        if self.array==[]:
            return True
        return False

    def top(self):
        '''
        返回栈顶的值
        '''
        if not self.isempty():
            return self.array[-1]
        return None

    def pop(self):
        '''
        出栈
        '''
        if not self.isempty():
            return self.array.pop(-1)
        return None

    def list(self):
        '''
        输出
        '''
        print self.array

if __name__=='__main__':
    s=mystack()
    s.push(1)
    for i in range(10):
        s.push(i)
    s.list()
    print '####################'
    print s.pop()
    print s.top()
    print s.pop()
    s.list()

