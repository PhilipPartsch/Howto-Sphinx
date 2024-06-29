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

Advantages: Enhance Sphinx to support object like elements with attributes, links, content and porcess them with functions.

.. element:: Sphinx-Needs
   :id: E_SPHINX_NEEDS

   .. needarch::

      {{flow(need().id)}}
      {{uml("E_SPHINX")}}

      {{need().id}}  -> E_SPHINX : extends


Directive
*********

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


Role
****

A role is an inline annottaion to get an information or link destination from a script.
Here we use the ``math`` role to explain how it looks like. 

.. example:: Docutils Role

   :math:`(a + b)` multiplied with :math:`(a - b)` is equal to :math:`a^2 - b^2`.


How-to use Sphinx and Sphinx-Needs
**********************************

You call ``sphinx-build`` with ``input``and ``òutput`` folder.
All CLI paramters can be found here: https://www.sphinx-doc.org/en/master/man/sphinx-build.html

How it is been used with in this repo, you can see here:

.. literalinclude:: ../.gitlab-ci.yml
   :language: yml
   :emphasize-lines: 15-18
   :linenos:
