from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.view import view_config, view_defaults
from jinja2 import FileSystemLoader, Environment
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship, aliased

from models.user import User

env = Environment(loader=FileSystemLoader('public_html/'))


@view_defaults(renderer='index.pt')
class RealAuto:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='Index', renderer='public_html/index.pt')
    def index_page(self):
        if self.request.cookies.get('login') is not None:
            log_in = True
            message = 'Здравствуйте, ' + self.request.cookies['login']
        else:
            log_in = False
            message = ''
        request = self.request
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            engine = create_engine('mysql+pymysql://root:@fix213p.dsmynas.com/real_auto')
            session = Session(bind=engine)
            base = declarative_base(bind=engine)
            if len(session.query(User.login, User.password).filter(User.login == login,
                                                                   User.password == password).all()) == 1:
                log_in = True
                message = 'Здравствуйте, ' + login
                self.request.response.set_cookie(name='login', value=login)
            else:
                message = 'Неверный логин или пароль'
        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/',
            login=login,
            password=password,
            log_in=log_in
        )


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('Index', '/')
    config.scan()

    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 80, app)
    server.serve_forever()
