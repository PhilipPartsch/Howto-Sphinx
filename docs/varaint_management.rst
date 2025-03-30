##################
Variant Management
##################


Sphinx: `only` Directive
========================

Documentation: `How to use only directive`_.

You can use a few mechanism to set tags, see `How to use tags`_.

In the pipeline, we currently set the tag via command line option :code:`--tag tag_Linux`.
See :download:`.gitlab-ci.yml <../.gitlab-ci.yml>`.

.. example:: `only` directive

   .. only:: tag_Windows

      We are building currently for `Windows`.

   .. only:: tag_MacOS

      We are building currently for `MacOS`.

   .. only:: tag_Linux

      We are building currently for `Linux`.

.. warning::

   Sphinx is always rendering the content inside the only directive,
   but is discarding the output if not needed.
   So if you create objects within the only directive, they are available to the datamodel.


Sphinx: `ifconfig` Directive
============================

:code:`--define my_ifconfig='ifconfig_MacOS'`

https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-D
https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html#module-sphinx.ext.ifconfig

add literal include conf.py

.. example:: `ifconfig` directive

   .. ifconfig:: my_ifconfig == ifconfig_Windows

      We are building currently for `Windows`.

   .. ifconfig:: my_ifconfig == ifconfig_MacOS

      We are building currently for `MacOS`.

   .. ifconfig:: my_ifconfig == ifconfig_Linux

      We are building currently for `Linux`.


useblocks Collections: `if_collection` Directive
================================================


Sphinx-Needs: Atttribute Variants
=================================


Sphinx-Ifelse:
==============



References
==========

.. target-notes::

.. _`How to use only directive` : https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only

.. _`How to use tags` : https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags
