from cookielib import CookieJar

from tempfile import mkdtemp

import unittest

from passlib.hash import sha256_crypt
from pyramid import testing
from sqlalchemy import create_engine
from webtest import TestApp


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        from plan2fab import make_app, configure_db
        from plan2fab.models import Base, DBSession

        self.tmpdir = mkdtemp()

        settings = {
            'sqlalchemy.url': 'postgresql://',
            'mako.directories': 'plan2fab:templates',
            'app.reports_directory': self.tmpdir
        }

        engine = create_engine('postgresql://')
        configure_db(engine)
        Base.metadata.create_all(engine)
        self.session = DBSession

        self.config = testing.setUp(settings=settings)
        self.config.include('pyramid_tm')

        app = make_app({}, **settings)
        self.testapp = TestApp(app, cookiejar=CookieJar())

    def tearDown(self):
        del self.testapp
        from plan2fab.models import DBSession
        DBSession.remove()

