#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.handlers import ContextHandler
from thumbor.utils import logger


class BlacklistHandler(ContextHandler):

    def get(self):
        blacklist = self.get_blacklist_contents()
        self.write(blacklist)
        self.set_header('Content-Type', 'text/plain')
        self.set_status(200)

    def put(self):
        blacklist = self.get_blacklist_contents()
        blacklist +=  self.request.query + "\n"
        logger.debug('Adding to blacklist: %s' % self.request.query)
        self.context.modules.storage.put('blacklist.txt', blacklist)
        self.set_status(200)
