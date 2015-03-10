#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.handlers import BaseHandler


class HealthcheckHandler(BaseHandler):
    def get(self):
        self.write('WORKING')

    def head(self, *args, **kwargs):
        self.set_status(200)
