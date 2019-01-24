#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
        name="radicale_auth_PAM",
        version="0.1",
        description="PAM authentication plugin for Radicale",
        author="Joseph Nahmias",
        author_email="joe@nahmias.net",
        url="https://gitlab.com/jello/radicale_auth_PAM",
        install_requires=["pam",],
        packages=find_packages(),
        include_package_data=True,
        license="GPL3+",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Topic :: System :: Systems Administration :: Authentication/Directory",
            ],
)
