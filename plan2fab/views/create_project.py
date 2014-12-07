from uuid import uuid4

from mako.template import Template

from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render
from pyramid.security import authenticated_userid
from pyramid.view import (
    view_config,
    view_defaults
)

from plan2fab.models import (DBSession, Project)


@view_defaults(route_name='create_project', renderer='create_project.mako')
class CreateProject:

    def __init__(self, request):
        self.request = request
        self.create_project_url = request.route_url('create_project')

    @view_config(request_method='GET')
    def create_project_form(self):
        return {
            'submit_project_url': self.create_project_url
        }

    @view_config(request_method='POST')
    def create_project(self):
        email = None
        website = None
        try:
            email = self.request.POST['email']
            website = self.request.POST['website']
        except KeyError:
            pass
            # Error 400 (Bad Request)

        if email is None:
            self.request.session.flash(u'Email is mandatory')
            return HTTPFound(location=self.create_project_url)

        if website is None:
            self.request.session.flash(u'WebSite is mandatory')
            return HTTPFound(location=self.create_project_url)

        #user = User(email)
        #user.website = website
        #user.token = self.generate_random_token()
        #DBSession.add(user)

        #self.send_setpassword_email(user)

        #users = DBSession.query(User).all()

        return {
            'submit_projects_url': self.create_projects_url,
            'projects': projects,
        }

