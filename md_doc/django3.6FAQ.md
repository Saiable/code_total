### `runserver`

- `django-admin runserver [addrport]`

  

Starts a lightweight development Web server on the local machine. By default, the server runs on port 8000 on the IP address `127.0.0.1`. You can pass in an IP address and port number explicitly.

If you run this script as a user with normal privileges (recommended), you might not have access to start a port on a low port number. Low port numbers are reserved for the superuser (root).

This server uses the WSGI application object specified by the[`WSGI_APPLICATION`](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-WSGI_APPLICATION) setting.

DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)

The development server automatically reloads Python code for each request, as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

If you’re using Linux or MacOS and install both [pywatchman](https://pypi.org/project/pywatchman/) and the[Watchman](https://facebook.github.io/watchman/) service, kernel signals will be used to autoreload the server (rather than polling file modification timestamps each second). This offers better performance on large projects, reduced response time after code changes, more robust change detection, and a reduction in power usage. Django supports `pywatchman` 1.2.0 and higher.

### [`path()`](https://docs.djangoproject.com/en/3.2/ref/urls/#django.urls.path)

The [`path()`](https://docs.djangoproject.com/en/3.2/ref/urls/#django.urls.path) function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. 

