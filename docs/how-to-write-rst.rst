.. _reSTxt_style_guide:

############################
reStructuredText Style Guide
############################

*******************
General information
*******************

Purpose
=======

This document intends to define the reStructuredText style-guide.


.. _reSTxt_style_guide_Filenames:

Quick Reference
===============

For a `Quick Reference`_ have a look at https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html


*********
Filenames
*********

We define our filenames only with lowercase alphanumeric characters (a-z, 0-9) and ``-`` (minus) symbol.

We use the ``.rst`` extension to indicate we defining a reStructuredText file.


.. _reSTxt_style_guide_ReguTxt:

*************
Regular text
*************

.. example:: Regular text

   You can write any text, 
   but please keep in mind, 
   white       spaces      or new lines are ignored.

   If you want to define a new line you can to use line blocks ``|``.
   For more information about line blocks please check `How to write lists and line blocks`_.

   | ``|`` Here I have defined when a new line has to be printed,
   | ``|`` so it looks like how I have specified it. 

   Or you use a empty line to serpeate the text

   from each other.
   
The standard reST inline markup is quite simple, use:

.. example:: reST inline markup

   one asterisk: *text* for emphasis (italics),

   two asterisks: **text** for strong emphasis (boldface), and

   backquotes: ``text`` for code samples.

   subscript: H\ :sub:`2`\ O

   superscript: E = mc\ :sup:`2`

Alternatives for are subscript and superscript are often the ``math`` :ref:`role <reSTxt_style_guide_Math>` ( :math:`E = mc^2` )
or literal Unicode characters (H₂O).

For information about inline markup please check `How to use inline-markup`_.

.. _reSTxt_style_guide_Whitespaces:

***********
Whitespaces
***********

Indentation
===========

We indent with 3 spaces. We do not use tabs.


Blank lines
===========

Blank lines are often need, please think about the description in `Regular text`_.
For a better reading in rst, please write two blank lines before overlined sections,
i.e. before H1 and H2 and one blank line before other sections.
See `Headlines`_ for an example.


Comments
========

.. example:: Comments

   Text before the comment.
   
   .. You can comment with ``..``.

   Text after the comment.


.. _reSTxt_style_guide_Substitution:

***********************
Substitution Definition
***********************

With this you can substitute content see https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions.  

.. example:: Substitution

   .. |reST| replace:: reStructuredText

   Yes, |reST| is a long word, so I can't blame anyone for wanting to
   abbreviate it.

.. note::
   You can use 
   
   "image": can be used for block-level images as well as in a substitution definition for inline images.
   See even the :ref:`image example <reSTxt_style_guide_Pictures>`.

   "replace": allows simple macro substitution. It also provides a workaround for the still missing support of nested inline markup.

   "unicode": converts Unicode character codes to characters.

   "date": inserts the current local date.


.. _reSTxt_style_guide_Headlines:

*********
Headlines
*********

We use the following symbols for the headlines:

| Headline level 1. ``#`` with overline
| Headline level 2. ``*`` with overline
| Headline level 3. ``=``
| Headline level 4. ``-``
| Headline level 5. ``^``
| Headline level 6. ``"``

Please define only on H1 for a rst document.

As an example:

.. code:: rst

  ##################
  H1: document title
  ##################

  Introduction text.


  *********
  Sample H2
  *********

  Sample content.


  **********
  Another H2
  **********

  Sample H3
  =========

  Sample H4
  ---------

  Sample H5
  ^^^^^^^^^

  Sample H6
  """""""""

  And some more content.


.. _reSTxt_style_guide_Tables:

******
Tables
******

The information about tables are wonderful provided in `How to write a table`_,
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#tables 
and https://docutils.sourceforge.io/docs/ref/rst/directives.html#tables .


Grid table syntax
=================

Especially the handling of bars ``|`` within tables has to be acknowledge.
They do have to be of sifted to the alligment.
So pay attention, a table with mailformed middel bares will not reported.

.. example:: Grid table syntax

   +------------------------+------------+----------+-----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4  |
   | (header rows optional) |            |          |           |
   +========================+============+==========+===========+
   | body row 1, column 1   | column 2   | column 3 | column 4  |
   +------------------------+------------+----------+-----------+
   | body row 2             | Cells may span columns.           |
   |                        | And with an bar ``|`` in the text |
   +------------------------+------------+----------------------+
   | body row 3             | Cells may  | - Table cells        |
   +------------------------+ span rows. | - contain            |
   | body row 4             |            | - body elements.     |
   +------------------------+------------+----------------------+


Simple tables
=============

Especially the handling to join adjacent columns has to be acknowledge.

.. example:: Simple tables

   =====  =====
      Inputs
   ------------
     A      B
   =====  =====
   1      Second column of row 1.
   2      Second column of row 2.
          Second line of paragraph.
   3      - Second column of row 3.

          - Second item in bullet
            list (row 3, column 2).
   \      Row 4; column 1 will be empty.
   =====  =====


Table directive
===============

.. example:: Table directive

   .. table:: Truth table for "not"
      :widths: auto
      :align: center

      =====  =====
        A    not A
      =====  =====
      False  True
      True   False
      =====  =====


CSV Table directive
===================

We want to highlight the directive options ``file``, ``header`` and ``header-rows``.

.. example:: csv-table directive

   .. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out,
      it wouldn't be crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"


List Table directive
====================

.. example:: list-table directive

   .. list-table:: Frozen Delights!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
        - Quantity
        - Description
      * - Albatross
        - 2.99
        - On a stick!
      * - Crunchy Frog
        - 1.49
        - If we took the bones out, it wouldn't be
          crunchy, now would it?
      * - Gannet Ripple
        - 1.99
        - On a stick!


.. _reSTxt_style_guide_Pictures:

********
Pictures
********

Image
=====

.. example:: Image directive

   .. image:: pictures/avatar.png
      :alt: my avatar
      :align: center

.. example:: Image directive inline

   |my avatar| greats you.

   .. |my avatar| image:: pictures/avatar.png
      :align: top
      :scale: 10%

Figure
======

.. example:: Figure directive

   .. figure:: pictures/avatar.png
      :scale: 100 %
      :alt: my avatar

      This is the caption of the figure (a simple paragraph).

      A legend consists of all elements after the caption.


.. _reSTxt_style_guide_Lists:

*****
Lists
*****

The information about lists are wonderful provided in `How to write lists and line blocks`_.

.. example:: Lists and Quote-like blocks

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

Nested lists are even possible, but be aware that they must be separated from the parent list items by blank lines:

.. example:: Nested lists

   * this is
   * a list

   * with a nested list
   * and some subitems

   * and here the parent list continues


.. _reSTxt_style_guide_Math:

****
Math
****

The information about mathematical expression are wonderful provided in `How to write math`_.

You can use a directive:

.. example:: math directive

   .. math::

      (a + b)^2 = a^2 + 2ab + b^2

      (a - b)^2 = a^2 - 2ab + b^2

You can even use inline ``math`` role:

.. example:: inline math role

   :math:`(a + b)` multiplied with :math:`(a - b)` is equal to :math:`a^2 - b^2`.


.. _reSTxt_style_guide_src_code:

********************************
Source code in the documentation
********************************

We use the ``code`` directive. It is good style to specify the programming language.

.. Here we do not use the example directive, as we want to document the code directive itself.

.. example:: code directive

   .. code:: rst
      :number-lines:

      ##################
      H1: document title
      ##################


.. _reSTxt_style_guide_links:

*****
Links
*****

Links between parts of the documentation
========================================

Here you can find an example how you link to a reference label (here a headline) in your documentation.
The ref is working across rst files. You can find more examples for picture and tables under `How to link within a rst documentation`_. 

From this chapter:

.. code:: rst

   .. _reSTxt_style_guide_links:

   *****
   Links
   *****

.. example:: reference to a reference label

   If you want to reference to the reference-label, see :ref:`reSTxt_style_guide_links`.
   If you want to customize your link text use :ref:`custom text <reSTxt_style_guide_links>`.

.. Note:: It is recommended to shorten the link mark as most as possible and use the customized link text way most of the time.

If you only want to link to a headline within a document you can use the headline text itself.

.. example:: Link to headline in the current document

   | ... content ...
   | I want to link to `References`_.
   | ... content ...


.. _reSTxt_style_guide_download_file:

Links to download files
=======================

It is possible to reference to non-rst files, so they can be "downloaded".
For more details please see `How to reference to downloadable files`_.

.. example::

   Download file to this :download:`file itself <how-to-write-rst.rst>`.


Reference to document
=====================

It is even possible to refernce to a document with ``:doc:``.

.. example:: Link to headline in the current document
   
   Reference to this :doc:`file itself <how-to-write-rst>`.


.. _reSTxt_style_guide_include_file:

Include a file into current document
====================================

It is possible to ``include`` in the current document another document.
Please be aware, that it is useful to have another file extension for included files,
standard pattern is ``.rst.inc``.
Even files with extension ``.inc`` shall **not** be fetched by the conf.py.

Example of ``include`` directive.

.. code:: rst
   
   .. include:: inclusion.rst.inc

Docutils documentation: `How to include file in document`_.


.. _reSTxt_style_guide_references:

References to external sites
============================

We use target-notes to mark links to external sites. The approach is used in this file, too.
The opportunity is you even get a back link, where in the document this link is been used. 

.. code:: rst

   ... content ...
   If you want to have an example see `How to link within a rst documentation`_.
   You can even customize the link `text<How to link within a rst documentation>`_.
   ... content ...

   **********
   References
   **********

   .. target-notes::

   _`How to link within a rst documentation`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks

It is even possible to reference directly to an external webside:

..  example:: direct external links

    - https://www.sphinx-needs.com
    - `sphinx-needs <https://www.sphinx-needs.com>`_


.. _reSTxt_style_guide_table_of_contents:

*****************
Table of Contents
*****************

It is possible to explicit create a table of contents over a complete documentation (overall documents) with ``.. toctree::``.
For detailed information see `How to create table of contents with toctree`_ or check ``index.rst``.

With `.. contents::` it is possible to create a "table of contents" for the current document.

.. it is not possible to include ``contents`` directive within another directive. So we cannot use ``example`` directive here.

.. code:: rst
   
   .. contents:: table of contents

This will be printed like:

.. contents:: table of contents


.. _reSTxt_style_guide_glossary:

********
Glossary
********

We use glossaries to define often used terms in a documentation. To get more information how to 
setup a glossary and how to link to, see `How to use a glossary`_. If you want to reference to a
glossary entry please use role ``term``.

.. example:: Glossary

   .. glossary::

      rst
         Apprivation of :term:`reStructuredText`.

      reStructuredText
         Markdown language we currently use.


.. _reSTxt_style_guide_variants:

********
Variants
********

See https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only

In the pipeline, we currently set the project_b tag via command line option ``-t project_b``.
See :download:`.gitlab-ci.yml <../.gitlab-ci.yml>`.
Or you could use https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags

.. example:: only directive

   .. only:: project_a

      We are building currently for Project A.

   .. only:: project_b
      
      We are building currently for Project B.

.. warning::

   Sphinx is always reandering the content inside the only directive,
   but is dicsarding the output if not needed.
   So if you create objects within the only directive, they are available to the datamodel. 

.. _reSTxt_style_guide_notes_and_warnings:

************************
Notes, warnings and tips
************************

We use sphinx build possibility to indicate notes and warnings to user of the documentation.
Please keep in mind, that we only use notes and warnings for really important things.

.. example:: note

   .. note::

      Note to the user of the documentation.

.. example:: warning

   .. warning::

      Warning to the user of the documentation.

.. example:: tip

   .. tip::

      Tip to the user of the documentation.


.. _reSTxt_style_guide_open_point:

**********
Open point
**********

As the complete methodology of Doc-As-Code and the changes we foresee during the transition phase,
it is needed to indicate open points in the same way across the work.
For this please use ``todo:`` in the documentation the start of an open point.


**********
References
**********

.. target-notes::

.. _`How to write lists and line blocks` : https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks

.. _`How to write a table`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables

.. _`How to use inline-markup`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#inline-markup

.. _`How to link within a rst documentation`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks

.. _`How to use a glossary`: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/glossary.html

.. _`How to reference to downloadable files`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#referencing-downloadable-files

.. _`How to create table of contents with toctree`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents

.. _`How to write math`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#math

.. _`Quick Reference`: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html

.. _`How to include file in document`: https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment
