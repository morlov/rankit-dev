import webapp2
import os
import jinja2

from scripts.utils import secutils

from scripts.models.user import User
from scripts.utils.secutils import check_secure_val

template_dir = os.path.join(os.path.dirname(__file__), '../../html')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_string(self, template, **params):
        return jinja_env.get_template(template).render(params)

    def render(self, template, **kw):
        self.write(self.render_string(template, **kw))

    def get_current_user(self):
        user_name = self.request.cookies.get('user_name')
        user_name = check_secure_val(user_name)
        if not user_name:
            return None
        return User.get_by_name(user_name.split('|')[0])

    
    def set_current_user(self, user):
        user_name = user.name
        h = secutils.make_secure_val(user_name)
        self.response.headers.add_header('Set-Cookie', 'user_name=%s; Path=/' % str(h))

    def reset_user(self):
        self.response.headers.add_header('Set-Cookie', 'user_name=; Path=/')

