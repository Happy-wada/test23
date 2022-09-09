#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

class LocInfo():
    def __int__(self):
        self.loc_dict = rospy.get_param('/location')
        self.human_dict = {}
        self.loc_name_list = list(self.loc_dict.keys())

