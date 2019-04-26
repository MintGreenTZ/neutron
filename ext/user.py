import json
import hashlib
import tornado.web
import tornado.gen

from base import BaseHandler
from forms import UpdateForm
from database import UserSystem


class ProfileHandler(BaseHandler):
    @tornado.gen.coroutine
    @tornado.web.authenticated
    def get(self):
        yield self.render('profile.html', title="profile", user=self.current_user,
                          info=UserSystem.queryById(self.current_user.decode()).fetchone())

    @tornado.gen.coroutine
    @tornado.web.authenticated
    def post(self):
        arg = self.request.arguments
        result = UserSystem.queryById(self.current_user.decode()).fetchone()

        diff = arg['username'][0].decode() != result[1]
        diff += arg['email'][0].decode() != result[3]
        diff += arg['phone'][0].decode() != result[4]

        if diff == 0:
            self.write(json.dumps({'errors': 'Nothing'}))
        else:
            arg['originUsername'] = [result[1]]
            arg['originEmail'] = [result[3]]
            arg['originPhone'] = [result[4]]

            form = UpdateForm(arg)

            errors = "Failed"
            if form.validate():
                yield UserSystem.update(result[0], arg['username'][0].decode(), arg['email'][0].decode(), arg['phone'][0].decode())
                errors = "Success"
            self.set_header("Content-Type", "application/json")

            retval = form.errors
            retval['errors'] = errors
            yield self.write(json.dumps(retval))


class SettingHandler(BaseHandler):
    @tornado.gen.coroutine
    @tornado.web.authenticated
    def get(self):
        self.render('setting.html', title="setting", user=self.current_user,
                    info=UserSystem.queryById(self.current_user.decode()).fetchone())

    @tornado.gen.coroutine
    @tornado.web.authenticated
    def post(self):
        form = self.request.arguments
        retval = {'errors': 'Failed'}

        if UserSystem.queryById(self.current_user.decode()).fetchone()[2] != hashlib.sha256(form['old'][0]).hexdigest():
            retval['old'] = 'Wrong Password'
        elif len(form['new'][0]) < 8:
            retval['new'] = 'Password too short'
        elif form['new'] != form['confirm']:
            retval['confirm'] = 'The two passwords you typed do not match'
        else:
            retval['errors'] = 'Success'
            UserSystem.changePassword(self.current_user.decode(), hashlib.sha256(form['new'][0]).hexdigest())

        self.set_header("Content-Type", "application/json")
        yield self.write(json.dumps(retval))

class AvatarHandler(BaseHandler):
    @tornado.gen.coroutine
    @tornado.web.authenticated
    def get(self):
        pass

class BookingHandler(BaseHandler):
    @tornado.gen.coroutine
    @tornado.web.authenticated
    def get(self):
        self.render('booking.html', title="my booking", user=self.current_user,
                    info=UserSystem.queryById(self.current_user.decode()).fetchone())
