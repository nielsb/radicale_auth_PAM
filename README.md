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
# Authentication method
type = radicale_auth_PAM
# PAM Service used for authentication
#pam_service = login
```

By default, we use the login PAM service to do authentication.  However, you
can create a custom PAM service if want.  For example, if you have `pam_service=radicale` and then have the following contents in `/etc/pam.d/radicale`:

```
#%PAM-1.0
# /etc/pam.d/radicale

auth required pam_succeed_if.so quiet_success user ingroup radicale-users
@include common-auth
```

Then users will need to be a member of the `radicale-users` group before being
granted access.
