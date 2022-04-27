#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   media_collector.py
@Time    :   2022/01/14 22:42:54
@Author  :   Benno Krause 
@Contact :   bk@freezingdata.de
@License :   (C)Copyright 2020-2021, Freezingdata GmbH
@Desc    :   None
'''

from Dummy.module_tools import *
from Dummy.urls import *
from Dummy.debug import *

from snhwalker_utils import snhwalker, snh_major_version
import snhwalker_utils  


class MediaCollector:
    def __init__(self, profile, config):
        self.profile = profile
        self.config = config
        pass

    def run(self):
        print('[START] Python Script: Save media')
        print('[Finished] Python Script: Save medias')   


