from wsgiref.simple_server import make_server

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import remember
from pyramid.view import view_config, view_defaults
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('public_html/'))


@view_defaults(renderer='index.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='Index', renderer='public_html/index.pt')
    def index_page(self):
        request = self.request
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            if 1:
                headers = remember(request, login)
                return HTTPFound(headers=headers)
            message = 'Неверный логин или пароль'
        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/',
            login=login,
            password=password,
        )


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('Index', '/')
    config.scan()

    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 80, app)
    server.serve_forever()
