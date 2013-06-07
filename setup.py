#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from itertools import chain
from glob import glob

import cookielaw


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Session',
]

package_data_globs = (
    'cookielaw/templates/cookielaw/*.html',
    'cookielaw/static/cookielaw/*/*',
    'cookielaw/locale/*/*/*'
)

package_data = []
for f in chain(*map(glob, package_data_globs)):
    package_data.append(f.split('/', 1)[1])
import pdb; pdb.set_trace();
setup(
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    name='django-cookie-law',
    version='.'.join(str(v) for v in cookielaw.VERSION),
    description='Helps your Django project comply with EU cookie law regulations',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/TyMaszWeb/django-cookie-law',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.2',
        'django-classy-tags>=0.3.0',
    ],
    test_require=[
        'selenium>=2.32.0',
    ],
    packages=find_packages(),
    package_data={'cookielaw': package_data},
    include_package_data=False,
    zip_safe = False,
    test_suite = 'runtests.main',
)
