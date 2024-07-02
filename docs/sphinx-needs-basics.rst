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

Types
=====

Documentation: How-to configure `Sphinx-Needs Types`_.


Options
=======

Documentation: How-to configure `Sphinx-Needs Options`_.

The special option ``:id:``, has to be unique within the current project.
It is often the case, you write sel speacking id's which are even can be easly reviewed.
Additionally you can use auto generated ids via IDE extension or scripting or scripting see https://github.com/useblocks/sphinx-needs/issues/728.
A discussion how ID's could be generated accross organisations is currently ongoing in https://github.com/useblocks/sphinx-needs/discussions/1088#discussioncomment-8131189.


Links
=====

Documentation: How-to configure `Sphinx-Needs Links`_.

Reference to Needs
==================

Documentation: How-to use `Sphinx-Needs Reference to Needs`_.

.. example:: Reference to Needs

   :need:`R_EXAMPLE_REQUIREMENT` is here like a customer requirement,
   where the :need:`[[title]] ([[id]] [[status]]) <S_EXAMPLE_SPECIFICATION>` is our derived specification.

Embedded a Need in a Need
=========================

.. example:: Embedded a Need in a Need

   .. need:: Parent
      :id: N_PARENT

      .. need:: Child
         :id: N_CHILD

Filter
******

Documentation: How-to use `Sphinx-Needs Filters`_.

NeedPie
*******

Documentation: How-to use `Sphinx-Needs NeedPie`_.

.. example:: How-to use a NeedPie.

   .. needpie:: Ratio of requirement types
      :labels: Stakeholder Requirement, Software Requirement, Evaluation

      type == 'stake_req'
      type == 'sw_req'
      type == 'evaluation'

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

.. example:: How-to use a NeedFlow.

   .. needflow:: Requirement Linkage
      :filter: is_external == "True" and (type=='stake_req' or type=='sw_req')
      :show_link_names:
      :show_filters:
      :scale: 50


NeedUML
*******

Documentation: How-to use `Sphinx-Needs NeedUML`_.
The ``debug`` option is often useful here, see `Sphinx-Needs NeedUML & NeedArch debug option`_.
The code been expected and generated is for `plantuml`_.

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

.. Variants
   ********

   Currently out-of-scope

   Only directive
   ==============

   Currently out-of-scope

   Build in Variants
   =================

   Currently out-of-scope


.. _ide_vscode:

Visula Studio Code Extensions
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

.. _`Sphinx-Needs NeedUML & NeedArch debug option` : https://sphinx-needs.readthedocs.io/en/latest/directives/needuml.html#debug

.. _`plantuml` : https://plantuml.com

.. _`jinja`: https://jinja.palletsprojects.com
