import sae
from OJproject import wsgi
application = sae.create_wsgi_app(wsgi.application)