import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
        'pyramid<1.4.99',
        'pyramid_debugtoolbar',
        'SQLAlchemy',
        'transaction',
        'pyramid_tm',
        'pyramid_mailer',
        'zope.sqlalchemy',
        'waitress',
        'docutils',
        'WebTest',
        'passlib',
    ]


setup(name='plan2fab',
      version='0.0',
      description='plan2fab',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="plan2fab",
      entry_points="""\
      [paste.app_factory]
      main = plan2fab:main
      initialize_plan2fab_db = plan2fab.initialize_db:main
      """,
      )
