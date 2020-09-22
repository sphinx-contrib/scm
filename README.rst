sphinxcontrib-scm
=================

|badge:pypi-version| |badge:py-versions|
|badge:pre-commit| |badge:black| |badge:prettier|

.. |badge:pypi-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-scm.svg
   :target: https://pypi.org/project/sphinxcontrib-scm
   :alt: [Latest PyPI version]
.. |badge:py-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-scm.svg
   :target: https://pypi.org/project/sphinxcontrib-scm
   :alt: [Supported Python versions]
.. |badge:pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: [pre-commit: enabled]
.. |badge:black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: [Code style: black]
.. |badge:prettier| image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
   :target: https://github.com/prettier/prettier
   :alt: [Code style: prettier]


This package provides ``sphinxcontrib.scm``, a simple SCM interface for Sphinx-based
documentation.


Installation
------------

1. ``pip install sphinxcontrib-scm``


Configuration
-------------

1. Add ``'sphinxcontrib.scm'`` to the ``extensions`` list in ``conf.py``.

   .. code::

      extensions = [ 'sphinxcontrib.scm' ]


2. Configure in ``conf.py``

   .. code::

      scm_contribs_email = ["true"|"false"]          # Show email. Default: "true"
      scm_contribs_limit_contributors" = [None|int]  # Limit number of contributors. Use None
                                                     # to deactivate. Default: None
      scm_contribs_min_commits" = int                # Filter by number of commits. Default: 0
      scm_contribs_sort" = ["name"|"num"]            # Sort by name or number of commits.
                                                     # Default: "name"
      scm_contribs_type" = ["author"|"committer"]    # Show info of author or committer.
                                                     # Default: "author"


Usage
-----

Directive
^^^^^^^^^

.. code::

   .. scm-sectionauthor::
      :email: [true|false]
      :limit_contributors: [<int>]
      :min_commits: [<int>]
      :sort: [name|num]
      :type: [author|committer]

Populates ``sectionauthor`` directive with a list of SCM contributors. All options are
optional and override the config settings in ``conf.py``.


Role
^^^^

.. code::

   :scm-contribs:`.`

Can be used inline (eg as content for the ``sectionauthor`` directive. Currenlty, email
addresses are not converted into mailto links.
