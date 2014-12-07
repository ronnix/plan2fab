from pyramid import testing

from pyramid_mailer import get_mailer

from plan2fab.models import Project
from plan2fab.tests import BaseTestCase
from plan2fab.views.create_project import CreateProject


class TestCreateProject(BaseTestCase):

    def setUp(self):
        super(TestCreateProject, self).setUp()
        self.config.add_route('create_project', '/foo')

    def test_project_is_created_in_database(self):
        request = testing.DummyRequest({'name': 'An Ubber Project'})
        CreateProject(request).create_project()
        user = self.session.query(Project).filter_by(name='An Ubber Project').first()
        self.assertIsNotNone(project)

    def test_show_error_message_when_name_already_exist(self):
        project = Project('A Name')
        self.session.add(project)
        request = testing.DummyRequest({'name': 'A Name'})
        CreateProject(request).create_project()
        self.assertEqual([U'Name already taken'], request.session.peek_flash())

