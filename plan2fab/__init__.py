from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)

    session_factory = SignedCookieSessionFactory(settings['session_secret'])
    config.set_session_factory(session_factory)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('create_project', '/create_project')

    config.scan()

    return config.make_wsgi_app()
