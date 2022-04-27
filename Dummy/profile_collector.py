#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   profile_collector.py
@Time    :   2022/01/14 22:42:29
@Author  :   Benno Krause 
@Contact :   bk@freezingdata.de
@License :   (C)Copyright 2020-2021, Freezingdata GmbH
@Desc    :   None
'''

from Dummy.module_tools import *
from Dummy.urls import *
from Dummy.debug import *

import time

from snhwalker_utils import snhwalker, snh_major_version
import snhwalker_utils    

class ProfileCollector:
    def __init__(self):
        pass

    def handle_current_profile(self):
        pass

    def handle_current_group(self):
        pass    

    def current_is_user(self):
        return True

    def current_is_page(self):
        return False

    def current_is_group(self):
        return False        

    def save_profile(self, profileUrl):
        debugPrint('[START] Python Script: Save profile')        
        debugPrint('[Finished] Python Script: Save profile')
        
    def save_profile_details(self, profile):
        debugPrint('[START] Python Script: SaveProfileDetails')
        debugPrint('[Finished] Python Script: SaveProfileDetails')