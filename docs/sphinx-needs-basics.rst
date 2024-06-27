############################
Introduction to Sphinx-Needs
############################

Define a Need
*************

Documentation: How-to work with `Sphinx-Needs Need`_.

Types
=====

Documentation: How-to configure `Sphinx-Needs Types`_.

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


Options
=======

Documentation: How-to configure `Sphinx-Needs Options`_.

Links
=====

Documentation: How-to configure `Sphinx-Needs Links`_.

Reference to Needs
==================

Documentation: How-to use `Sphinx-Needs Reference to Needs`_.

:need:`R_EXAMPLE_REQUIREMENT` is here like a customer requirement,
where the :need:`S_EXAMPLE_SPECIFICATION` is our derivied specification.

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

.. needpie:: Ratio of requirement types
   :labels: Stakeholder Requirement, Software Requirement, Evaluation

   type == 'stake_req'
   type == 'sw_req'
   type == 'evaluation'

NeedBar
*******

Documentation: How-to use `Sphinx-Needs NeedBar`_.

.. needbar : : Requirements & Status Overview
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

.. needtable : : List of software requirements
   :types: sw_req
   :style: table
   :columns: id;title;docname as "document";lineno as "line no"
   :sort: lineno

NeedFlow
********

Documentation: How-to use `Sphinx-Needs NeedFlow`_.

.. needflow : : Requirement Linkage
   :types: stake_req, sw_req
   :show_link_names:
   :show_filters:

NeedArch
********

Documentation: How-to use `Sphinx-Needs NeedArch`_.

NeedUML
*******

Documentation: How-to use `Sphinx-Needs NeedUML`_.

.. needuml:: Architecture of Module Merge_Dicts

   {{flow("M_MERGE_DICTS")}}

Variants
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
-----------------------------

VsCode extension `Sphinx-Needs-VsCode <https://marketplace.visualstudio.com/items?itemName=useblocks.sphinx-needs-vscode>`_
provides support for Sphinx-Needs. See more details in the `Documentation <https://sphinx-needs-vscode.useblocks.com/>`_.

reStructuredText Extension: https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext


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
