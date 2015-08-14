import re
from scripts.handlers import handler

from scripts.models.user import User


USER_RE   = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE   = re.compile(r"^.{3,20}$")
EMAIL_RE  = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_user_name(user_name):
    return user_name and USER_RE.match(user_name)
def valid_password(password):
    return password and PASS_RE.match(password)
def valid_email(email):
    return email and EMAIL_RE.match(email)

def valid_signup(self, email, password, verify, user_name):
    if not valid_email(email):
        return "That's not a valid email."
    if not valid_password(password):
        return "That's a valid password."
    if password != verify:
        return "Your passwords didn't match."
    if not valid_user_name(user_name):
        return "That's not a valid username."
    if User.get_by_name(user_name):
        return "This user already exists."
    if User.get_by_email(email):
        return "This email already registered."

class Signup(handler.Handler):

    def get(self):
        if not self.get_current_user():
            self.render("signup.html")
        else:
            self.redirect('/')

    def post(self):
        
        user_name = self.request.get('user_name')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        error_login = valid_signup(self, email, password, verify, user_name)
        
        if error_login:
            self.render('signup.html', error_login=error_login, email=email, password=password, verify=verify, user_name=user_name)
        else:
            user = User(name=user_name, password=password, email=email)
            user.put()
            self.set_current_user(user)
            self.redirect('/')

class Signin(handler.Handler):

    def get(self):
        user_name = self.request.cookies.get('user_name')
        if not user_name:
            self.render('signin.html')
        else:
            self.redirect('/')

    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        user = User.get_by_email(email)
        if (not user) or (password != user.password):
            self.render('signin.html', error_login = "Invalid mail or password.", email=email, password=password)
        else:
            self.set_current_user(user)
            self.redirect('/')

class Signout(handler.Handler):

    def get(self):
        self.reset_user()
        self.redirect('/')