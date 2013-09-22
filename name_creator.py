# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 21:52:18 2013

@author: MaLin_win
"""

class Filename_Creator:
    prefix = ""
    name_format =""
    def __init__ (self, prefix_, name_format_):
        self.prefix = prefix_
        self.name_format = name_format_
    
    def compose_name (prefix_, idx_, name_format_):
        output_name = prefix_ + str(idx_) + name_format_
        return output_name
        
    def generate_name (self, idx_):
        output_name = self.prefix + str(idx_) + self.name_format
        return output_name
        

    

        
#import name_creator
#
#a=name_creator.Filename_Creator("sd",".s");
#name = a.generate_name(3);
#print (name)