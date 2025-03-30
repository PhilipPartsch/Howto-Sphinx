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

1. Add the `ifconfig` directive to the extensions:

   .. code-block:: rst
      :caption: How-to add `ifconfig` directive to the extensions

      extensions = [
         #...
         'sphinx.ext.ifconfig',
         #...
      ]

2. Add your configuration parameter to :code:`conf.py`

   .. literalinclude:: conf.py
      :caption: Example how-to incude source code from a file
      :language: py
      :linenos:
      :start-after: # -- sphinx ifconfig
      :end-before: # -- sphinx ifconfig end

3. Overwrite the configuration parameter in your sphinx-build
   :code:`sphinx-build [options] --define my_ifconfig='ifconfig_MacOS' <sourcedir> <outputdir>`

   https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-D
   https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html#module-sphinx.ext.ifconfig

4. Use the `ifconfig` directive in your rst files

   .. example:: `ifconfig` directive

      .. ifconfig:: my_ifconfig == "ifconfig_Windows"

         We are building currently for `Windows`.

      .. ifconfig:: my_ifconfig == "ifconfig_MacOS"

         We are building currently for `MacOS`.

      .. ifconfig:: my_ifconfig == "ifconfig_Linux"

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
