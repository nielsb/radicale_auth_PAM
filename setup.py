#!/usr/bin/env python3

from distutils.core import setup

setup(
        name="radicale_auth_PAM",
        version="0.1",
        description="PAM authentication plugin for Radicale",
        author="Joseph Nahmias",
        author_email="joe@nahmias.net",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Programming Language :: Python :: 3",
            "Topic :: System :: Systems Administration :: Authentication/Directory",
            ],
        packages=["radicale_auth_PAM"],
        install_requires=["pam",],
)
