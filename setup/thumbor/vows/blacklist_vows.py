#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from pyvows import Vows, expect
from tornado_pyvows.context import TornadoHTTPContext

from thumbor.app import ThumborServiceApp
from thumbor.importer import Importer
from thumbor.config import Config
from thumbor.context import Context, ServerParameters

from os.path import abspath, join, dirname, exists
from shutil import rmtree


class BaseContext(TornadoHTTPContext):
    def get_app(self):
        file_storage_root_path = '/tmp/thumbor-vows/storage'
        if exists(file_storage_root_path):
            rmtree(file_storage_root_path)

        cfg = Config()
        cfg.USE_BLACKLIST = True
        cfg.LOADER = "thumbor.loaders.file_loader"
        cfg.FILE_LOADER_ROOT_PATH = abspath(join(dirname(__file__), 'fixtures/'))
        cfg.STORAGE = 'thumbor.storages.file_storage'
        cfg.FILE_STORAGE_ROOT_PATH = file_storage_root_path

        importer = Importer(cfg)
        importer.import_modules()

        server = ServerParameters(8889, 'localhost', 'thumbor.conf', None, 'debug', None)
        ctx = Context(server, cfg, importer)
        application = ThumborServiceApp(ctx)
        return application

@Vows.batch
class Blacklist(BaseContext):

    class BaseBlacklist(TornadoHTTPContext):
        def topic(self):
            response = self.get('/blacklist')
            return (response.code, response.body)

        def should_return_blank(self, topic):
            expect(topic[1]).to_equal("")

        def should_return_200(self, topic):
            expect(topic[0]).to_equal(200)

        class AddingToBlacklist(TornadoHTTPContext):
            def topic(self):
                response = self.fetch('/blacklist?blocked.jpg', method='PUT', body='')
                return (response.code, response.body)

            def should_return_200(self, topic):
                expect(topic[0]).to_equal(200)

            class ReadingUpdatedBlacklist(TornadoHTTPContext):
                def topic(self):
                    response = self.get('/blacklist')
                    return (response.code, response.body)

                def should_return_200(self, topic):
                    expect(topic[0]).to_equal(200)

                def should_contain_blacklisted_file(self, topic):
                    expect("blocked.jpg\n" in topic[1] ).to_equal(True)

@Vows.batch
class BlacklistIntegration(BaseContext):

    class NormalGetImage(TornadoHTTPContext):
        def topic(self):
            response = self.get('/unsafe/image.jpg')
            return response.code

        def should_return_200(self, topic):
            expect(topic).to_equal(200)

        class BlacklistedGetImage(TornadoHTTPContext):

            def topic(self):
                self.fetch('/blacklist?image.jpg', method='PUT', body='')
                response = self.get('/unsafe/image.jpg')
                return response.code

            def should_return_200(self, topic):
                expect(topic).to_equal(404)
