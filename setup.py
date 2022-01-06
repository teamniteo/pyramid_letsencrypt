import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGELOG = open(os.path.join(here, 'CHANGELOG.rst')).read()
except IOError:
    README = CHANGELOG = ''

install_requires = [
    'pyramid>=1.4',
    ]

testing_extras = [
    'WebTest',
    'nose',
    'coverage',
    ]


setup(name='pyramid_letsencrypt',
      version='0.1',
      description=('A package which provides an easy way to host Let\'s '
        'Encrypt domain validation content in your Pyramid project.'),
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: OSI Approved :: BSD License",
        ],
      keywords='wsgi pylons pyramid ssl letsencrypt',
      author="Niteo",
      author_email="info@niteo.co",
      url="https://github.com/teamniteo/pyramid_letsencrypt",
      license="BSD",
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require = {
          'testing':testing_extras,
          },
      test_suite="tests",
      entry_points='',
      )
