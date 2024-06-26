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


Sphinx
******

Link: https://www.sphinx-doc.org

Description: Create intelligent and beautiful documentation ...

Advantages: Enhance Docutils to support multi file documentation build with commonly used directives.


Sphinx-Needs
************

Author: useblocks

Link: https://www.sphinx-needs.com

Description: Sphinx-Needs allows to create, manage and
analyze requirements, specifications, test cases and more inside Sphinx-based documentations.

Advantages: Enhance Sphinx to support object like elements with attributes, links, content and porcess them with functions.


Directive
*********

A directive gives the opportunity to structure information together.
Here we use the ``figure`` directive to explain how it looks like. 

| Directive Type: "figure"
| Directive Arguments: one, required (image URI)
| Directive Options: see documentation
| Directive Content: Interpreted as the figure caption and an optional legend.

.. example:: What is a Directive?

   .. figure:: pictures/avatar.png
      :scale: 150 %
      :alt: my avatar

      This is the caption of the figure (a simple paragraph).


Role
****

A role is an inline annottaion to get an information or link destination from a script.
Here we use the ``mat`` role to explain how it looks like. 

.. example:: Docutils Role

   :math:`(a + b)` multiplied with :math:`(a - b)` is equal to :math:`a^2 - b^2`.
