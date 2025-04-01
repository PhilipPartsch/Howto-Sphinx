##################
Variant Management
##################


Sphinx: only Directive
======================

Documentation: `How to use only directive`_.

You can use a few mechanism to set tags, see `How to use tags`_.

In the pipeline, we currently set the tag via command line option :code:`--tag tag_Linux`.
See :download:`.gitlab-ci.yml <../.gitlab-ci.yml>`.

.. example:: `only` directive

   .. only:: tag_Windows

      We are building currently for Windows via tag.

      .. need:: Need Tag Windows
         :id: N_VARIANT_TAG_WINDOWS

   .. only:: tag_MacOS

      We are building currently for MacOS via tag.

      .. need:: Need Tag MacOS
         :id: N_VARIANT_TAG_MACOS

   .. only:: tag_Linux

      We are building currently for Linux via tag.

      .. need:: Need Tag Linux
         :id: N_VARIANT_TAG_LINUX

.. warning::

   Sphinx is always processing the content inside of the only directive,
   but is discarding the output if not needed.
   So if you create objects within the only directive, they are available to the datamodel.
   See the following needtable for demonstration.

.. needtable::
   :filter: c.this_doc() and section_name == "Sphinx: only Directive"
   :style: table


Sphinx: ifconfig Directive
==========================

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
      :caption: How-to add a customer configuration value to sphinx
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

         We are building currently for Windows via ifconfig.

         .. need:: Need ifconfig Windows
            :id: N_VARIANT_IFCONFIG_WINDOWS

      .. ifconfig:: my_ifconfig == "ifconfig_MacOS"

         We are building currently for MacOS via ifconfig.

         .. need:: Need ifconfig MacOS
            :id: N_VARIANT_IFCONFIG_MACOS

      .. ifconfig:: my_ifconfig == "ifconfig_Linux"

         We are building currently for Linux via ifconfig.

         .. need:: Need ifconfig Linux
            :id: N_VARIANT_IFCONFIG_LINUX

.. warning::

   Sphinx is always processing the content inside of the ifconfig directive,
   but is discarding the output if not needed.
   So if you create objects within the ifconfig directive, they are available to the datamodel.
   See the following needtable for demonstration.

.. needtable::
   :filter: c.this_doc() and section_name == "Sphinx: ifconfig Directive"
   :style: table


Collections: if-collection Directive
====================================

1. For sure you have to add the `sphinxcontrib.collections` extension to your extensions:

   .. code-block:: python
      :caption: How-to add `sphinxcontrib.collections` extension to the extensions

      extensions = [
         #...
         'sphinxcontrib.collections',
         #...
      ]

2. Configure :code:`collections` in :code:`conf.py`.

   .. literalinclude:: conf.py
      :caption: How-to configure collections extension
      :language: py
      :lineno-match:
      :start-after: # -- extension configuration: collections
      :end-before: # -- extension configuration: collections end

3. Use it in your rst files:

   .. example:: useblocks Collections: if-collection Directive

      .. if-collection:: collection_Windows

         We are building currently for Windows via if-collection.

         .. need:: Need if-collection Windows
            :id: N_VARIANT_COLLECTION_WINDOWS

      .. if-collection:: collection_MacOS

         We are building currently for MacOS via if-collection.

         .. need:: Need if-collection MacOS
            :id: N_VARIANT_COLLECTION_MACOS

      .. if-collection:: collection_Linux

         We are building currently for Linux via if-collection.

         .. need:: Need if-collection Linux
            :id: N_VARIANT_COLLECTION_LINUX

   .. warning::

      You can write headlines / sections in the content of the if-collection directive.
      But you have to be careful with the correct ordering of sections in all
      possible output variants.

.. needtable::
   :filter: c.this_doc() and section_name == "Collections: if-collection Directive"
   :style: table


Sphinx-Ifelse:
==============

1. For sure you have to add the `sphinx-ifelse` extension to your extensions:

   .. code-block:: python
      :caption: How-to add `sphinx-ifelse` extension to the extensions

      extensions = [
         #...
         'sphinx_ifelse',
         #...
      ]

2. Configure :code:`ifelse_variants` in :code:`conf.py`.

   .. literalinclude:: conf.py
      :caption: How-to configure ifelse_variants
      :language: py
      :lineno-match:
      :start-after: # -- extension configuration: ifelse
      :end-before: # -- extension configuration: ifelse end

3. Use it in your rst files:

   .. example:: Sphinx-Ifelse:

      .. if:: ifelse_OS == "ifelse_Windows"

         We are building currently for Windows via ifelse.

         .. need:: Need ifelse Windows
            :id: N_VARIANT_IFELSE_WINDOWS

      .. elif:: ifelse_OS == "ifelse_MacOS"

         We are building currently for MacOS via ifelse.

         .. need:: Need ifelse MacOS
            :id: N_VARIANT_IFELSE_MACOS

      .. elif:: ifelse_OS == "ifelse_Linux"

         We are building currently for Linux via ifelse.

         .. need:: Need ifelse Linux
            :id: N_VARIANT_IFELSE_LINUX

      .. else::

         We are building currently for an unknown OS via ifelse.

         .. need:: Need ifelse OS Unknown
            :id: N_VARIANT_IFELSE_OS_UNKNOWN

   .. warning::

      You can write headlines / sections in the content of the ifelse directive.
      But you have to be careful with the correct ordering of sections in all
      possible output variants.

.. needtable::
   :filter: c.this_doc() and section_name == "Sphinx-Ifelse:"
   :style: table


Sphinx-Needs: Attribute Variants
================================

todo:
https://sphinx-needs.readthedocs.io/en/latest/directives/need.html#variants-for-options-support

https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-variants
https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-variant-options

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
      :caption: How-to configure needs_variants and needs_variant_options
      :language: py
      :linenos:
      :start-after: # sphinx-needs variants start
      :end-before: # sphinx-needs variants end

3. Use it in your rst files:

   .. example:: Sphinx-Needs: Attribute Variants

      .. need:: A need with variants
         :id: N_EXAMPLE_VARIANTS
         :status: var_MacOS:MacOS, var_Linux:Linux,not set
         :test_status: var_MacOS:set with variant,not set
         :satisfies: var_MacOS:N_EXAMPLE_VARIANTS_ORDERING

      .. need:: A need with variants (with different ordering)
         :id: N_EXAMPLE_VARIANTS_ORDERING
         :status: var_Linux:Linux, var_MacOS:MacOS,not set
         :test_status: [tag_Linux]:set with sphinx-tag,not set

   .. warning::

      If your are using sphinx tags, these are not always set,
      you will get a warning:

      .. code-block:: python

         .. need:: A need with variants which creates a warning
            :id: N_EXAMPLE_VARIANTS_WARNING
            :status: var_MacOS: MacOS, var_Linux: Linux, not set
            :test_status: [tag_MacOS]: set with sphinx-tag, not set

      In the example, we will get :code:`WARNING: Error in filter
      'tag_MacOS': name 'tag_MacOS' is not defined [needs.variant]`.

.. needtable::
   :filter: c.this_doc() and section_name == "Sphinx-Needs: Attribute Variants"
   :style: table


Jinja2 templates
================

todo:
how-to integrate jinja2 in rst: https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/

1. Define :code:`jinja_context` and :code:`jinja2rst` with variant information
   in :code:`conf.py`.

   .. literalinclude:: conf.py
      :caption: How-to configure jinja_context and jinja2rst
      :language: py
      :linenos:
      :start-after: # -- extension configuration: Jinja2
      :end-before: # -- extension configuration: Jinja2 end

2. Connect :code:`jinja2rst` in Sphinx to source-read event.

   .. literalinclude:: conf.py
      :caption: How-to connect jinja2rst to source-read event
      :language: py
      :linenos:
      :start-after: # -- use jinja2rst in setup
      :end-before: # -- use jinja2rst in setup end
      :prepend: def setup(app):

3. Use it in your rst files:

   .. example:: Jinja2:

{%if os%}
         We are building currently for {{os}} via jinja2 template.

         .. need:: Need Jinja2 {{os}}
            :id: N_VARIANT_JINJA2_{{os}}
            :status: {%if os == 'QNX'%}set by template{%else%}not set{%endif%}
            {%if realtime%}:satisfies: N_ALWAYS_JINJA2_REALTIME{%endif%}
{%else%}
         We are building currently for an unknown OS via jinja2 template.

         .. need:: Need Jinja2 OS Unknown
            :id: N_VARIANT_JINJA2_OS_UNKNOWN
{%endif%}

         .. need:: Need Jinja2 realtime
            :id: N_ALWAYS_JINJA2_REALTIME

.. needtable::
   :filter: c.this_doc() and section_name == "Jinja2 templates"
   :style: table


Comparision of the different mechanisms:
========================================

.. note::

   The table below is a summary of the different mechanisms.
   It is not complete and does not cover all use cases.
   Please check the documentation of the different mechanisms for more details.


   The rating is from:

   * `--` = not supported
   * `-` = possible, but not recommended
   * `+` = possible, but drawbacks
   * `++` = possible and recommended

.. list-table:: Jinja
   :header-rows: 1
   :widths: 10 30 30 10 10

   *  - Name
      - Advantages
      - Disadvantages
      - Manage Need Variants
      - Manage Need Attributes / Links
   *  - `only`
      -  - Can change complete parts of the documentation
         - Build-in sphinx directive
      -  - Always add the elements to the datamodel
         - Does not support else or elif
      - +
      - --
   *  - `ifconfig`
      -  - Can change complete parts of the documentation
         - Build-in sphinx directive
      -  - Always add the elements to the datamodel
         - Does not support else or elif
      - +
      - --
   *  - `if-collection`
      -  - Can change complete parts of the documentation
         - Wonderfull to be combined with content from collections
      -  - Has to be installed and configured
         - Does not support else or elif
      - +
      - --
   *  - `ifelse`
      -  - Can change complete parts of the documentation easly
         - Support else or elif
      -  - Has to be installed and configured
      - ++
      - --
   *  - `Sphinx-Needs Attribute Variants`
      -  - Build-in sphinx-needs directive
         - Support else or elif
         - Can change attributes and links of needs elements
      -  - Can only change attributes of needs
         - Attention with combintion of tags
      - --
      - ++
   *  - `jinja2`
      -  - Can change everything depending on the context
      -  - Is difficult to debug
         - Neasting of jinja2 templates is difficult, but often requested e.g.
           with use of needuml or needs templates
      - +
      - +

References
==========

.. target-notes::

.. _`How to use only directive` : https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only

.. _`How to use tags` : https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags
