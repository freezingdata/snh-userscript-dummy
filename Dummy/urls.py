#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   urls.py
@Time    :   2021/12/28 14:33:30
@Author  :   Benno Krause 
@Contact :   bk@freezingdata.de
@License :   (C)Copyright 2020-2021, Freezingdata GmbH
@Desc    :   None
'''


def GetURL_Timeline(UserID, UserIDNumber = ''):
    return f'http://url.com/timeline/{UserID}'

def GetURL_Profile(UserID, UserIDNumber = ''):
    return f'http://url.com/{UserID}'

def GetURL_Friends(UserID, UserIDNumber = ''):
    return f'http://url.com/friends/{UserID}'


def GetURL_Fotos(UserID, UserIDNumber = ''):
    return f'http://url.com/fotos/{UserID}'

def GetURL_Group(UserID, UserIDNumber = ''):
    return f'http://url.com/group/{UserID}'

def GetURL_OwnProfile(UserID, UserIDNumber = ''):
    return f'http://url.com/self/{UserID}'