"""
Flask-Validate
----------------

Extension for validating the JSON payload of API requests using [JSON Schema](http://json-schema.org/)
"""
from setuptools import setup

setup(
    name='Flask-Validate',
    version='0.0.1',
    url='https://github.com/stockninja/flask_validate',
    license='MIT',
    author='Justin Moen',
    author_email='jamoen7@gmail.com',
    py_modules=['flask_validate'],
    description='API payload validation',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'jsonschema',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
