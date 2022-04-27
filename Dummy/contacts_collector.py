#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   contacts_collector.py
@Time    :   2022/01/14 22:42:18
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

class ContactsCollector:
    def __init__(self, input_profile, input_config):
        self.profile = input_profile
        self.config = input_config
        pass

    def run(self):
        debugPrint('[START] Python Script: Save contacts')
        debugPrint('[Finished] Python Script: Save contacts')