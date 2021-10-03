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

import logging
from radicale.auth import BaseAuth
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
        if configuration.get('auth', 'pam_service'):
            self._service = self.configuration.get('auth', 'pam_service')
        logger.info('Using PAM service "%s" for authentication.', self._service)

    def is_authenticated(self, user, password):
        if user is None or password is None:
            return False
        self.logger.debug("Login attempt by '%s'.", user)
        self._pam.authenticate(user, password, self._service)
        self.logger.debug("Pam returned %d - %s.",
                self._pam.code, self._pam.reason)
        if 0 == self._pam.code:
            self.logger.info("User '%s' authenticated successfully.", user)
            return True
        else:
            self.logger.warning("Authentication failed for user '%s': %s.",
                    user, self._pam.reason)
            return False
