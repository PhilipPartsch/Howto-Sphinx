##################################################
How is Docutils, Sphinx and Sphinx-Needs organized
##################################################

Docutils
********

Author: David Goodger

Link: https://docutils.sourceforge.io

Description: Docutils is an open-source text processing system for processing plaintext documentation into useful formats,
such as HTML, LaTeX, man-pages, OpenDocument, or XML.
It includes `reStructuredText <https://docutils.sourceforge.io/rst.html>`_, the easy to read, easy to use,
what-you-see-is-what-you-get plaintext markup language.

Advantages: It is possible to extend rst with own directives.

Restriction: Can only process one page.

.. element:: Docutils
   :id: E_DOCUTILS

   .. needarch::

      {{flow(need().id)}}



Sphinx
******

Link: https://www.sphinx-doc.org

Description: Create intelligent and beautiful documentation ...

Advantages: Enhance Docutils to support multi file documentation build with commonly used directives.

.. element:: Sphinx
   :id: E_SPHINX

   .. needarch::

      {{flow(need().id)}} {
         {{uml("E_DOCUTILS")}}
      }


Sphinx-Needs
************

Author: useblocks

Link: https://www.sphinx-needs.com

Description: Sphinx-Needs allows to create, manage and
analyze requirements, specifications, test cases and more inside Sphinx-based documentations.

Advantages: Enhance Sphinx to support object like elements with attributes, links, content and process them with functions.

.. element:: Sphinx-Needs
   :id: E_SPHINX_NEEDS

   .. needarch::

      {{flow(need().id)}}
      {{uml("E_SPHINX")}}

      {{need().id}}  -> E_SPHINX : extends


How-to use Sphinx and Sphinx-Needs
**********************************

You call ``sphinx-build`` with ``input`` and ``output`` folder.
All CLI parameters can be found here: https://www.sphinx-doc.org/en/master/man/sphinx-build.html

In the ``input`` folder Sphinx expects a ``index.rst`` file and normally a ``conf.py`` file for the configuration.
You can change the path to the configuration even with a ``sphinx-build`` parameter ``-c``.

Other useful parameter are:

- ``-v``, --verbose
- ``-W``, --fail-on-warning
- ``-E``, --fresh-env #discard previous build results
- ``-a``, --write-all #If given, always write all output files


How it is been used with in this repo, you can see here:

.. literalinclude:: ../.gitlab-ci.yml
   :language: yaml
   :emphasize-lines: 43
   :linenos:


Definition of a Directive
*************************

A directive gives the opportunity to structure information together.
Here we use the ``figure`` directive to explain how it looks like.

- Directive Type: "figure"

  .. code-block:: rst
     :emphasize-lines: 1
     :linenos:

     .. figure:: pictures/avatar.png
        :scale: 150 %
        :alt: my avatar

        This is the caption of the figure (a simple paragraph).

- Directive Arguments: "pictures/avatar.png"

  .. code-block:: rst
     :emphasize-lines: 1
     :linenos:

     .. figure:: pictures/avatar.png
        :scale: 150 %
        :alt: my avatar

        This is the caption of the figure (a simple paragraph).

- Directive Options: ":scale: 150 %" and ":alt: my avatar"

  .. code-block:: rst
     :emphasize-lines: 2, 3
     :linenos:

     .. figure:: pictures/avatar.png
        :scale: 150 %
        :alt: my avatar

        This is the caption of the figure (a simple paragraph).

- Directive Content: "This is the caption of the figure (a simple paragraph)."

  .. code-block:: rst
     :emphasize-lines: 5
     :linenos:

     .. figure:: pictures/avatar.png
        :scale: 150 %
        :alt: my avatar

        This is the caption of the figure (a simple paragraph).

.. example:: What is a Directive?

   .. figure:: pictures/avatar.png
      :scale: 150 %
      :alt: my avatar

      This is the caption of the figure (a simple paragraph).


Definition of a Role
********************

A role is an inline annotation to get an information or link destination from a script.
Here we use the ``math`` role to explain how it looks like.

.. example:: Docutils Role

   :math:`(a + b)` multiplied with :math:`(a - b)` is equal to :math:`a^2 - b^2`.

- Role Type: "math"

  .. code-block:: rst
     :emphasize-lines: 1
     :linenos:

     :math:`(a + b)`

- Role Argument: "(a + b)"

  .. code-block:: rst
     :emphasize-lines: 1
     :linenos:

     :math:`(a + b)`
