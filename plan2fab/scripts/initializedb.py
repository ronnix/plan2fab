import sys

from passlib.hash import sha256_crypt
import argparse

from sqlalchemy import engine_from_config
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Project,
    Base,
    )


def parse_command_line(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="configuration file (e.g. production.ini)")
    return parser.parse_args(args)


def main(argv=sys.argv):
    args = parse_command_line(argv[1:])
    setup_logging(args.config)
    settings = get_appsettings(args.config)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

