pyramid_letsencrypt
====================

``pyramid_letsencrypt`` provides an easy way to host Let's Encrypt domain
validation content in your Pyramid project, with just a config entry.

This plugin is needed for deployment scenarios where you do not have a
reverse proxy (think Nginx and the lot) in from of your Pyramid app to serve
static content. On of such scenarios is hosting your Pyramid app on Heroku.

Usage
-----



Testing & development
---------------------

If you have ``tox`` installed, run all tests with:

.. code-block:: bash

    $ tox

To run only a specific Python environment:

.. code-block:: bash

    $ tox -e py35

If you don't have ``tox`` installed, you can install the testing requirements,
then run the tests.

.. code-block:: bash

    $ python3 -m venv env
    $ env/bin/pip install -e ".[testing]"
    $ env/bin/nosetests
