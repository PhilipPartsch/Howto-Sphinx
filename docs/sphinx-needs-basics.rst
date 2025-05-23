############################
Introduction to Sphinx-Needs
############################

Define a Need
*************

Documentation: How-to work with `Sphinx-Needs Need`_.

.. example:: How-to create a Need.

    .. req:: Example Requirement
       :id: R_EXAMPLE_REQUIREMENT
       :status: new

       This is our example requirement.


    .. spec:: Example Specification
       :id: S_EXAMPLE_SPECIFICATION
       :status: new
       :links: R_EXAMPLE_REQUIREMENT

       This is our example Specification.

Minimum need
============

With `needs_title_optional <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-title-optional>`_
it is even possible to skip the title.

.. example:: Minimum Need.

    .. need::
       :id: N_MINIMUM_NEED

So the bare minimum need only has a `:id:`.


Types
=====

Documentation: How-to configure `Sphinx-Needs Types`_.


Options
=======

Documentation: How-to configure `Sphinx-Needs Options`_.

The special option ``:id:``, has to be unique within the current project.
It is often useful, you write self speacking id's which even can be easly reviewed.
Additionally you can use auto generated ids via IDE extension or scripting see https://github.com/useblocks/sphinx-needs/issues/728.
A discussion how ID's could be generated accross organisations is currently ongoing in https://github.com/useblocks/sphinx-needs/discussions/1088#discussioncomment-8131189.


Links
=====

Documentation: How-to configure `Sphinx-Needs Links`_.

Reference to Needs
==================

Documentation: How-to use `Sphinx-Needs Reference to Needs`_.

.. example:: Reference to Needs

   :need:`R_EXAMPLE_REQUIREMENT` is here like a customer requirement,
   where the :need:`[[title]] in [[status]] ([[id]]) <S_EXAMPLE_SPECIFICATION>` is our derived specification.

Embedded a Need in a Need
=========================

.. example:: Embedded a Need in a Need

   .. need:: Parent
      :id: N_PARENT

      Here is some text before the embedded need. You could even write any other rst text.

      .. need:: Child
         :id: N_CHILD

         Here is some text inside of the embedded need. You could even write any other rst text.

      Here is some text after the embedded need. You could even write any other rst text.


NeedPart
========

.. example:: Need with needpart, linking to parts and filter

   .. need:: Test need with need parts
      :id: N_NEED_WITH_PARTS
      :tags: needpart_example

      :np:`(1) Part 1 of need`.

      :np:`(2) Part 2 of need`.

      Part :np:`(3)` of need.

   .. need:: Need links to part 1
      :id: N_LINK_TO_PART1
      :tags: needpart_example
      :links: N_NEED_WITH_PARTS.1

   .. need:: Need links to part 2 and 3
      :id: N_LINK_TO_PART2
      :tags: needpart_example
      :links: N_NEED_WITH_PARTS.2, N_NEED_WITH_PARTS.3

      We link to :need:`N_NEED_WITH_PARTS.2` and :need:`N_NEED_WITH_PARTS.3`.

   .. needtable::
      :tags: needpart_example
      :filter: is_need
      :show_parts:
      :columns: id;title;outgoing;incoming
      :style: table


External Projects
*****************

needs_external_needs
====================

We have add an external project already here:

.. literalinclude:: /metamodel.py
   :caption: How-to add a external project
   :language: py
   :lineno-match:
   :start-at: needs_external_needs = [
   :end-at: ]

Needs are imported from the project, marked as `external`, and can be used as created
in this project. You can find filters, which use the imported needs in all following
reports.

needimport
==========

An example of the usage of needimport can be found under
:ref:`Sphinx-Needs: Import Needs <sphinx_import_needs>`.


Filter
******

Documentation: How-to use `Sphinx-Needs Filters`_.

We use these filters in different exampls within this document in the following
reports.


NeedPie
*******

Documentation: How-to use `Sphinx-Needs NeedPie`_.

.. example:: How-to use a NeedPie.

   .. needpie:: Ratio of requirement types
      :labels: Stakeholder Requirement, Software Requirement, Evaluation

      type == 'stake_req' and is_external == True
      type == 'sw_req' and is_external == True
      type == 'evaluation' and is_external == True

NeedBar
*******

Documentation: How-to use `Sphinx-Needs NeedBar`_.

.. example:: How-to use a NeedBar.

   .. needbar:: Requirements & Status Overview
      :legend:
      :colors: black, yellow, orange, green
      :xlabels: FROM_DATA
      :ylabels: FROM_DATA

                 ,        Stakeholder Requirement             ,           Software Requirement
            empty, type=='stake_req' and status==''           ,    type=='sw_req' and status==''
         accepted, type=='stake_req' and status=='accepted'   ,    type=='sw_req' and status=='accepted'
      implemented, type=='stake_req' and status=='implemented',    type=='sw_req' and status=='implemented'
         verified, type=='stake_req' and status=='verified'   ,    type=='sw_req' and status=='verified'

NeedTable
*********

Documentation: How-to use `Sphinx-Needs NeedTable`_.

.. example:: How-to use a NeedTable.

   .. needtable:: List of software requirements
      :types: sw_req
      :style: table
      :columns: id; title; status

.. example:: How-to use a NeedTable II.

   .. needtable:: List of stakeholder requirements
      :types: stake_req
      :style: datatables
      :columns: id; title; status; is_external as "External"

NeedFlow
********

Documentation: How-to use `Sphinx-Needs NeedFlow`_.
The code been expected and generated is for `plantuml`_.
You can configure the visiual repsentation of needs elements in  needflow with `needs-types <Sphinx-Needs Types>`_.
Needflow expects to get `plantuml deployment-diagram`_ elements as representation.

.. example:: How-to use a NeedFlow.

   .. needflow:: Requirement Linkage
      :filter: is_external == True and (type=='stake_req' or type=='sw_req')
      :show_link_names:
      :debug:
      :scale: 30


Structured Sphinx-Needs reports in tables
*****************************************

Often you have the use case to structure reports of Sphinx-Needs in table view.
You can do this with e.g. a `list-table` to structure the visiual representation.

.. example:: Reports structured with tables

   .. list-table:: Reports
         :header-rows: 1

         * - Report
           - Representation
         * - NeedPie
           - .. needpie:: Ratio of requirement types
                :labels: Stakeholder Requirement, Software Requirement, Evaluation

                type == 'stake_req' and is_external == True
                type == 'sw_req' and is_external == True
                type == 'evaluation' and is_external == True

         * - NeedBar
           - .. needbar:: Requirements & Status Overview
                :legend:
                :colors: black, yellow, orange, green
                :xlabels: FROM_DATA
                :ylabels: FROM_DATA

                           ,        Stakeholder Requirement             ,           Software Requirement
                      empty, type=='stake_req' and status==''           ,    type=='sw_req' and status==''
                   accepted, type=='stake_req' and status=='accepted'   ,    type=='sw_req' and status=='accepted'
                implemented, type=='stake_req' and status=='implemented',    type=='sw_req' and status=='implemented'
                   verified, type=='stake_req' and status=='verified'   ,    type=='sw_req' and status=='verified'

         * - NeedTable
           - .. needtable:: List of software requirements
                :types: sw_req
                :style: table
                :columns: id; title; status

         * - NeedFlow
           - .. needflow:: Requirement Linkage
                :filter: is_external == True and (type=='stake_req' or type=='sw_req')
                :show_link_names:
                :show_filters:
                :scale: 30


NeedUML
*******

Documentation: How-to use `Sphinx-Needs NeedUML`_.
The ``debug`` option is often useful here, see `Sphinx-Needs NeedUML & NeedArch debug option`_.
The code been expected and generated is for `plantuml`_.
You can use `needs-render-context` to extend the data available in needarch and needuml.

.. example:: How-to use a NeedUML.

   .. needuml::
      :debug:

      {{flow("M_MERGE_DICTS")}}

      note right of [M_MERGE_DICTS]
         We use M_MERGE_DICTS to
         merge python dictionaries.
      end note


NeedArch
********

NeedArch is extending the functionality of NeedUML, to access local data of a Need.
Documentation: How-to use `Sphinx-Needs NeedArch`_.
The code been expected and generated is for `plantuml`_ and
you can use `jinja`_ to template your planuml code.

You can find detailed description in
:ref:`How-To model Architecture <architecture-examples>`.


Templating
**********

With templates you can template the content for needs.
It is even possible to add text before and after a need.
Documentation: the documentation is part of needs docu under How-to use `Sphinx-Needs Templates`_.

We use it here finally in `conf.py`:

.. literalinclude:: /metamodel.py
   :caption: How-to assign the templates to needs via global options
   :language: py
   :lineno-match:
   :start-at: needs_global_options = {
   :end-at: }

The templates are defined available in `/needs_templates` e.g. `arch_template.need`
used in `docname == "architecture-examples"`:

.. literalinclude:: /needs_templates/arch_template.need
   :caption: How-to assign the templates to needs via global options
   :language: rst
   :lineno-match:

An example need which uses such template is :need:`C_DIAGRAMS`.


Dynamic functions
*****************

Documentation: How-to use `Sphinx-Needs Dynamic functions`_.

You can even define your own dynamic functions in `conf.py` and use them in your needs.
See `Sphinx-Needs develop-own-functions <https://sphinx-needs.readthedocs.io/en/latest/dynamic_functions.html#develop-own-functions>`_.

.. example:: How-to use dynamic functions.

   .. need:: Test Dynamic Functions 1
      :id: N_DF_1
      :status: open

      This need has id :ndf:`copy("id")` and status :ndf:`copy("status")`.

   .. need:: Test Dynamic Functions 2
      :id: N_DF_2
      :status: [[copy("status", "N_DF_1")]]
      :links: N_DF_1

      Copies status of :need:`N_DF_1` to own status.

   .. need:: Test Dynamic Functions 3
      :id: N_DF_3
      :links: N_DF_2, [[copy('links', 'N_DF_2')]]

      Set own link to :need:`N_DF_1` and also copies all links from it.


Layouts
*******

Documentation: with an dedicated chapter under How-to use `Sphinx-Needs Layouts & Styles`_.

You can define your own layouts finally in `conf.py` with `needs_layouts` and
use them for your needs:

.. literalinclude:: /metamodel.py
   :caption: How-to define the layouts
   :language: py
   :lineno-match:
   :start-at: needs_layouts = {
   :end-at: }

It is been used here, to get the edit button on all needs.

You can set the default layout like we do in `conf.py`

.. literalinclude:: /conf.py
   :caption: How-to set default layout of a need
   :language: py
   :lineno-match:
   :start-at: needs_default_layout =
   :end-at: needs_default_layout =

You could set the `layout` even via
`needs_global_options <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#global-option-filters>`_.


Variant Management
******************

You can find detailed description in
:ref:`How-To use variant management <variant_management>`.


.. ide_vscode

   Rework to ubcode

   Visual Studio Code Extensions
   *****************************

   VsCode extension for `Sphinx-Needs-VsCode <https://marketplace.visualstudio.com/items?itemName=useblocks.sphinx-needs-vscode>`_
   provides support for Sphinx-Needs. See more details in the `Documentation <https://sphinx-needs-vscode.useblocks.com/>`_.

   VsCode extension for `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_.


References
**********

.. target-notes::

.. _`Sphinx-Needs Need` : https://sphinx-needs.readthedocs.io/en/latest/directives/need.html

.. _`Sphinx-Needs Types` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-types

.. _`Sphinx-Needs Options` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-options

.. _`Sphinx-Needs Links` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links

.. _`Sphinx-Needs Reference to Needs` : https://sphinx-needs.readthedocs.io/en/latest/roles.html#need

.. _`Sphinx-Needs Filters` : https://sphinx-needs.readthedocs.io/en/latest/filter.html

.. _`Sphinx-Needs NeedPie` : https://sphinx-needs.readthedocs.io/en/latest/directives/needpie.html

.. _`Sphinx-Needs NeedBar` : https://sphinx-needs.readthedocs.io/en/latest/directives/needbar.html

.. _`Sphinx-Needs NeedTable` : https://sphinx-needs.readthedocs.io/en/latest/directives/needtable.html

.. _`Sphinx-Needs NeedFlow` : https://sphinx-needs.readthedocs.io/en/latest/directives/needflow.html

.. _`Sphinx-Needs NeedArch` : https://sphinx-needs.readthedocs.io/en/latest/directives/needarch.html

.. _`Sphinx-Needs NeedUML` : https://sphinx-needs.readthedocs.io/en/latest/directives/needuml.html

.. _`needs-render-context` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-render-context

.. _`plantuml deployment-diagram` : http://plantuml.com/deployment-diagram

.. _`Sphinx-Needs NeedUML & NeedArch debug option` : https://sphinx-needs.readthedocs.io/en/latest/directives/needuml.html#debug

.. _`plantuml` : https://plantuml.com

.. _`jinja`: https://jinja.palletsprojects.com

.. _`Sphinx-Needs Templates` : https://sphinx-needs.readthedocs.io/en/latest/directives/need.html#template

.. _`Sphinx-Needs Dynamic functions` : https://sphinx-needs.readthedocs.io/en/latest/dynamic_functions.html

.. _`Sphinx-Needs Layouts & Styles` : https://sphinx-needs.readthedocs.io/en/latest/layout_styles.html
