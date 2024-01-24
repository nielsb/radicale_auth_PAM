# This file is a plugin for the Radicale Calendar Server
# Copyright © 2019 Joseph Nahmias
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this plugin.  If not, see <http://www.gnu.org/licenses/>.

"""
Authentication plugin for the Radicale Calendar Server

Allows Radicale to use PAM as the authentication backend.
The PAM service used is configurable, default = login.
"""

from radicale.auth import BaseAuth
from radicale.log import logger
from importlib import import_module

class Auth(BaseAuth):
    def __init__(self, configuration):
        super().__init__(configuration)
        logger = logging.getLogger("radicale")
        try:
            logger.debug("Attempting to load module pam.")
            self._pam = import_module('pam').pam()
        except Exception as e:
            raise RuntimeError("Failed to load pam python module: %s." % e) from e
        logger.debug("Loaded module pam successfully.")
        self._service = 'login'     # default
        with contextlib.suppress(KeyError):
            self._service = configuration.get('auth', 'pam_service')
            logger.info('Using PAM service "%s" for authentication.', self._service)

    def login(self, login, password):
        if login is None or password is None:
            return ''
        logger.debug("Login attempt by '%s'.", login)
        self._pam.authenticate(login, password, self._service)
        logger.debug("Pam returned %d - %s.",
                self._pam.code, self._pam.reason)
        if 0 == self._pam.code:
            logger.info("User '%s' authenticated successfully.", user)
            return login
        else:
            logger.warning("Authentication failed for user '%s': %s.",
                    login, self._pam.reason)
            return ''
