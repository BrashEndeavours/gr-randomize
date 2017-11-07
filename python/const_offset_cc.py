#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017 SLt Blake Mackey
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

from gnuradio import gr
from gnuradio.blocks import multiply_const_cc
from math import sqrt
from random import uniform

class const_offset_cc(gr.hier_block2):
    """
    docstring for block const_offset_cc
    """
    def __init__(self):
        gr.hier_block2.__init__(self,
            "const_offset_cc",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex))  # Output signature

        re = uniform(-1000,1000)
        im = uniform(-1000,1000)

        unit_re = re/sqrt(re**2 + im**2)
        unit_im = (im/sqrt(re**2 + im**2))


        # Define blocks and connect them
        self.multiply_const_cc_0 = multiply_const_cc(complex(unit_re, unit_im))

        self.connect(self, self.multiply_const_cc_0)
        self.connect(self.multiply_const_cc_0, self)
