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

   .. code-block:: python
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
      :prepend: def setup(app):

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


Sphinx-Needs: Attribute Variants
================================

1. For sure you have to add the `sphinx-needs` extension to your extensions:

   .. code-block:: python
      :caption: How-to add `sphinx-needs` extension to the extensions

      extensions = [
         #...
         'sphinx_needs',
         #...
      ]

2. Configure :code:`needs_variants` and :code:`needs_variant_options` in :code:`conf.py`.

   .. literalinclude:: conf.py
      :caption: Example how-to incude source code from a file
      :language: py
      :linenos:
      :start-after: # sphinx-needs variants start
      :end-before: # sphinx-needs variants end

3. Use it in your rst files:

   .. example:: Sphinx-Needs: Attribute Variants

      .. need:: A need with variants
         :id: N_EXAMPLE_VARIANTS
         :status: var_MacOS: MacOS, var_Linux: Linux, not set
         :test_status: ['tag_MacOS' in tags]: set with sphinx-tag, not set

      .. need:: A need with variants (with different ordering)
         :id: N_EXAMPLE_VARIANTS_ORDERING
         :status: var_Linux: Linux, var_MacOS: MacOS, not set
         :test_status: [tag_Linux]: set with sphinx-tag, not set

Sphinx-Ifelse:
==============



References
==========

.. target-notes::

.. _`How to use only directive` : https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only

.. _`How to use tags` : https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags
