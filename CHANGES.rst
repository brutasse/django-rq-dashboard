Changelog
=========

0.3.3 (2017-06-13)
------------------

* Redirect to admin login views when users aren't logged in or lack the proper
  permissions. Require users to have ``is_staff`` set to ``True``.

0.3.1 (2017-03-21)
------------------

* Fix an encoding error with RQ>=0.6.

0.3.0 (2016-03-11)
------------------

* Add support for Django 1.9. Drop support for Django < 1.5.

0.2.2 (2014-06-23)
------------------

* Use ``get_state()`` instead of deprecated ``state`` to get worker state.

0.2.1 (2014-04-02)
------------------

* Remove a print statement.

0.2 (2012-09-05)
----------------

* Fixed #1 -- added ``{% load url from future %}`` to templates.

0.1 (2012-09-04)
----------------

Initial release
