Django-rq-dashboard
-------------------

`RQ`_ is a simple task queue for queuing and processing jobs.
``django-rq-dashboard`` is a web frontend to monitor your RQ queues, jobs and
workers in realtime from the Django admin. It looks like this:

.. image:: http://cloud.github.com/downloads/brutasse/django-rq-dashboard/stats.png

See also screenshots of the `Worker`_, `Queue`_ and `Job`_ pages.

.. _Worker: http://cloud.github.com/downloads/brutasse/django-rq-dashboard/worker.png

.. _Queue: http://cloud.github.com/downloads/brutasse/django-rq-dashboard/queue.png

.. _Job: http://cloud.github.com/downloads/brutasse/django-rq-dashboard/job.png

It is very much inspired from the Flask-powered `rq-dashboard`_.

.. _RQ: http://python-rq.org/

.. _rq-dashboard: https://github.com/nvie/rq-dashboard

* Authors: Bruno Renié and `contributors`_

  .. _contributors: https://github.com/brutasse/django-rq-dashboard/contributors

* Licence: BSD

* Compatibility: Django 1.4 and greater, pytz and a recent RQ (>= 0.3)

* Code & docs: https://github.com/brutasse/django-rq-dashboard

Installation
------------

* ``pip install django-rq-dashboard``

* Add ``django_rq_dashboard`` to your ``INSTALLED_APPS``

* Add the URL patterns in you URLconf::

      urlpatterns = patterns('',
          (r'^admin/rq/', include('django_rq_dashboard.urls')),
          # your own patterns follow…
      )

* (optional if non-default values) configure Redis access in your settings.
  Just define a dictionnary that can be used to construct a ``Redis`` object.
  All key are optional and their default values are::

      RQ = {
          'host': 'localhost',
          'port': 6379,
          'db': 0,
          'password': None,
          'socket_timeout': None,
          'connection_pool': None,
          'charset': 'utf-8',
          'errors': 'strict',
          'decode_responses': False,
          'unix_socket_path': None,
      }

* Run the development server, queue some jobs, fire off some workers and go
  watch http://localhost:8000/admin/rq/
