========
 Ophrys
========

Simple Association Web Content Management System
================================================

.. image:: https://travis-ci.org/Ophrys-Project/Ophrys.png?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Ophrys-Project/Ophrys


What is Ophrys?
---------------

Ophrys is a simple web content management system for small associations and
communities who want to communicate with each other inside and present the
group on a public website.

The project is still under development.


Information for developers
--------------------------

To get the development version of this project, run the following commands::

  $ git clone https://github.com/Ophrys-Project/Ophrys.git
  $ cd Ophrys
  $ virtualenv --python=python3 .virtualenv
  $ source .virtualenv/bin/activate
  $ pip install https://www.djangoproject.com/download/1.6b1/tarball/
  $ pip install -r requirements.txt
  $ python create_custom_directory.py

Now you can customize the settings file in the ``ophrys_custom/``
directory. After you have done this (or done nothing if you do not want to
customize the file), run the following command::

  $ python manage.py syncdb

To start Django's development server, run the following command::

  $ python manage.py runserver

To run the pep8 style guide checker and the tests, have a look at the
commands you find in the .travis.yml file.

Good luck.


Used Software
-------------

Ophrys uses:

* `Python Programming Language`_
* `Django`_
* `Pep8 (Python style guide checker)`_
* `Coverage (Code coverage measurement for Python)`_
* `Sphinx (Python Documentation Generator)`_

.. _Python Programming Language: http://python.org/
.. _Django: https://www.djangoproject.com/
.. _Pep8 (Python style guide checker):  http://pep8.readthedocs.org/
.. _Coverage (Code coverage measurement for Python): http://nedbatchelder.com/code/coverage/
.. _Sphinx (Python Documentation Generator): http://sphinx-doc.org/
