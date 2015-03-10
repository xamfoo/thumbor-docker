#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):

    @filter_method()
    def grayscale(self):
        engine = self.context.modules.engine
        engine.convert_to_grayscale()
