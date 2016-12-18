from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults
from jinja2 import FileSystemLoader, Environment
from sqlalchemy import create_engine, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from car import Car
from car_advert import CarAdvert
from models.user import User

env = Environment(loader=FileSystemLoader('public_html/'))


@view_defaults(renderer='index.pt')
class RealAuto:
    def __init__(self, request):
        self.request = request
        self.engine = create_engine('mysql+pymysql://root:@fix213p.dsmynas.com/real_auto?charset=utf8')
        self.session = Session(bind=self.engine)
        self.base = declarative_base(bind=self.engine)
        self.car_adverts = \
            self.session. \
                query(CarAdvert.text, CarAdvert.cost, User.login, Car.model, Car.concern) \
                .join(User, User.id == CarAdvert.user_id) \
                .join(Car, Car.id == CarAdvert.car_id) \
                .all()

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
            if len(self.session.query(User.login, User.password).filter(User.login == login,
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
            log_in=log_in,
            car_adverts=self.car_adverts
        )

    @view_config(route_name='Reg', renderer='public_html/reg.pt')
    def reg_page(self):
        if self.request.cookies.get('login') is not None:
            log_in = True
            message = 'Здравствуйте, ' + self.request.cookies['login']
        else:
            log_in = False
            message = ''
        request = self.request
        login = ''
        password = ''
        password_conf = ''
        phone = null
        first_name = null
        surname = null
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            password_conf = request.params['password_conf']
            phone = request.params['phone']
            first_name = request.params['first_name']
            surname = request.params['surname']
            if len(self.session.query(User.login).filter(
                            User.login == login).all()) == 0 and password == password_conf and len(
                password) != 0 and len(login) != 0:
                log_in = True
                message = 'Здравствуйте, ' + login
                self.request.response.set_cookie(name='login', value=login, path='/', domain=None)
                self.session.add(User(login=login, password=password, phone=phone, name=first_name, surname=surname))
                self.session.commit()
            else:
                message = 'Логин не должен быть пустым и должен быть уникальным,' \
                          ' пароль не должен быть пустым и должен совпадать с подтверждением пароля.'
        return dict(
            name='Reg',
            message=message,
            url=request.application_url + '/reg',
            login=login,
            password=password,
            log_in=log_in,
            password_conf=password_conf,
            phone=phone,
            first_name=first_name,
            surname=surname
        )

    @view_config(route_name='Logout')
    def logout_page(self):
        url = self.request.route_url('Index')
        self.request.response = HTTPFound(location=url)
        self.request.response.delete_cookie(name='login', path='/', domain=None)
        return self.request.response


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('Index', '/')
    config.add_route('Reg', '/reg')
    config.add_route('Logout', '/logout')
    config.scan()

    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 80, app)
    server.serve_forever()
