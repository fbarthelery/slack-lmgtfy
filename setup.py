#!/usr/bin/env python

from setuptools import setup
# from distutils.core import setup

setup(name='slack-lmgtfy',
      version='1.0',
      description='Slack custom command to lmgtfy.com',
      author='Da Risk',
      author_email='da_risk@geekorum.com',
      package_dir={"": "src"},
      packages=['slack-lmgtfy'],
      scripts=["src/slack-lmgtfy-run-server.py", "src/slack-lmgtfy-run-wsgi.py"],
      test_suite="test",
      include_package_data=True,
      zip_safe=False,
      install_requires=['Flask', "requests"])
