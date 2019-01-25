# PAM authentication plugin for Radicale

[Radicale] is a CalDAV and CardDAV server, for storing calendars and
contacts.  This python module provides an authentication plugin for Radicale
to make use of the [Linux PAM] system library.

[Radicale]: https://radicale.org/
[Linux PAM]: http://www.linux-pam.org/


## Installation

```shell
pip3 install radicale-auth-PAM
```

## Configuration

```INI
[auth]
type = radicale_auth_PAM
```
