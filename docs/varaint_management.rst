##################
Variant Management
##################


Sphinx: `only` Directive
========================

See `How to use only directive`_.

In the pipeline, we currently set the tag via command line option ``-t tag_Linux``.
See :download:`.gitlab-ci.yml <../.gitlab-ci.yml>`.
Or you could use https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags

.. example:: only directive

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

useblocks Collections: `if_collection` Directive
================================================

Sphinx-Needs: Atttribute Variants
=================================

Sphinx-Ifelse:
==============

.. comment

   **********
   References
   **********

   .. target-notes::

   .. _`How to use only directive` : https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only
