#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    desc = fh.read()

setuptools.setup(
        name="radicale_auth_PAM",
        version="0.1",
        description="PAM authentication plugin for Radicale",
        long_description=desc,
        author="Joseph Nahmias",
        author_email="joe@nahmias.net",
        url="https://gitlab.com/jello/radicale_auth_PAM",
        install_requires=["python-pam",],
        packages=setuptools.find_packages(),
        include_package_data=True,
        license="GPL3+",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Plugins ",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Topic :: Security",
            "Topic :: System :: Systems Administration :: Authentication/Directory",
            ],
)
