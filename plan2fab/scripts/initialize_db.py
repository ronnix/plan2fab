import sys

from passlib.hash import sha256_crypt
import argparse

from sqlalchemy import engine_from_config
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from plan2fab.models import (
    DBSession,
    Project,
    Base,
    )

def main(argv=sys.argv):
    print "innnnnn3"
    config = argv[1]
    setup_logging(config)
    settings = get_appsettings(config)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

