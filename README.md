PAM authentication plugin for Radicale
######################################

Radicale_ is a CalDAV and CardDAV server, for storing calendars and
contacts.  This python module provides an authentication plugin for Radicale
to make use of the `Linux PAM`_ system library.

.. _Radicale: https://radicale.org/
.. _`Linux PAM`: http://www.linux-pam.org/


Installation
============

.. code::

	pip3 install radicale-auth-PAM

Configuration
=============

.. code::

	[auth]
	type = radicale_auth_PAM

