Releasing ``pyramid_letsencrypt``
================================

Prepare master for a new release
--------------------------------

- Do platform test via tox:

  $ tox -r

  Make sure statement coverage is at 100% (the test run will fail if not).

- Ensure all features of the release are documented (audit CHANGELOG.rst or
  communicate with contributors).

- Change CHANGELOG.rst heading to reflect the new version number.

- Change setup.py version to the release version number.

- Make sure PyPI long description renders (requires ``collective.dist``
  installed into your Python)::

  $ python setup.py check -r

- Create a release tag::

  $ git tag vX.Y

- Make sure your Python has ``setuptools-git``, ``twine``, and ``wheel``
  installed and release to PyPI::

  $ python setup.py sdist bdist_wheel
  $ twine upload dist/pyramid_letsencrypt-X.Y-*
