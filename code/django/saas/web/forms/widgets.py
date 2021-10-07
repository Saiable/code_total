#!/usr/bin/env python
# encoding: utf-8
'''
@author: huihui
@time: 2021-10-07 13:18
@func:

'''

from django.forms import RadioSelect

class ColorRadioSelect(RadioSelect):
    input_type = 'radio'
    template_name = 'web/widgets/color_radio/radio.html'
    option_template_name = 'web/widgets/color_radio/radio_option.html'