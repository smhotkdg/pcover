"""
input data

save yaml file

"""

import yaml
import codecs
import os
import sys

class cover :
    def __init__(self,name,width,height,font):
        self.name = name
        self.width = width
        self.height = height
        self.font = font

def print_Cover(cover) :
    """
    print "Nmae", ":",cover["nmae"]
    print "width",":",cover["width"]
    print "height",":",cover["height"]
    print "font",":",cover["font"]
"""

    data =dict(Name = cover.name,width = cover.width, height = cover.height,font = cover.font)
    return data
"""
a = cover("test1",20,10,33,0)
cover_list = list()
cover_list.append(a)
doc = yaml.load(codecs.open("cover.yaml","w","euc-kr"))


if cover_list :
    for cover in cover_list :
        print_Cover(cover)
"""
data_list = dict()
a = cover("test1",20,10,"$ddd")
b = cover("test2",26,15,"%dafd")
c = cover("test3",25,15,"123F")
d = cover("test4",10,12,"adf#")

cover_list = list()

data = print_Cover(a)
cover_list.append(data)

data = print_Cover(b)
cover_list.append(data)


data = print_Cover(c)
cover_list.append(data)

data = print_Cover(d)

data_list.update(data)
cover_list.append(data)
with open('config.yaml','w') as outfile:
    outfile.write(yaml.dump_all(cover_list,default_flow_style=False))

