.. _architecture-examples:

###########################################
How-To model Architecture with Sphinx-Needs
###########################################


Structure Model: Deployment-Diagram
***********************************

Sphinx-Needs offers a build in represenatation of elements with `needflow`_,
`needarch`_, and `needuml`_.

You can use `needs-flow-configs <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-flow-configs>`_
to change repesentation in needflow.
You can use `needs-render-context`_ to extend the data available in needarch and needuml.

Needflow expects to get `plantuml deployment-diagram`_ elements as representation.
With `flow() <https://sphinx-needs.readthedocs.io/en/latest/directives/needuml.html#flow-id>`_
you can get this repesentation even in needarch and needuml.


Visial representation of UML Ports in Sphinx-Needs
==================================================

Pay attention: We do use ``:input:`` and ``:output:`` in the same datamodel.
This is only because to see the differences in the output of plantuml tooling.
Especially the ordering of links like ``A -> B`` vs ``B <- A``.

.. example:: Definiton of a super structure element

   .. lib:: My lib
      :id: LIB_MY_LIB

      .. needarch::
         :key: Deployment
         :debug:

         left to right direction
         'top to bottom direction

         'Define elements
         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().part_of_back %}
         '{{e}}
         {% if needs[e].type == "comp" %}{{uml(e, 'Deployment')}}{% endif %}
         {% endfor %}
         }

         'Extra link to make diagramm nice looking
         C_A --[hidden] C_B

         'Link defined elements
         {% for e in need().part_of_back %}
         'e = {{e}}
         {%- if needs[e].type == "comp" -%}
         {% for f in needs[e].parent_needs_back %}
         'f = {{f}}
         {%- if (needs[f].type == "inport") -%}
         {% for g in needs[f].input %}
         'g = {{g}}
         {{g}} -[#000000]-> {{f}}
         {% endfor %}
         {%- endif -%}
         {% endfor %}
         {%- endif -%}
         {% endfor %}
         }

      .. needarch::
         :key: Deployment2
         :debug:

         'Define elements
         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().part_of_back %}
         '{{e}}
         {% if needs[e].type == "comp" %}{{flow(e)}}{% endif %}
         {% endfor %}
         }

         'Extra link to make diagramm nice looking
         C_A --[hidden] C_B

         'Link defined elements
         {% for e in need().part_of_back %}
         'e = {{e}}
         {%- if needs[e].type == "comp" -%}
         {% for f in needs[e].parent_needs_back %}
         'f = {{f}}
         {%- if (needs[f].type == "inport") -%}
         {% for g in needs[f].input %}
         'g = {{g}}
         {{needs[g].parent_need}} #-# {{e}}
         {% endfor %}
         {%- endif -%}
         {% endfor %}
         {%- endif -%}
         {% endfor %}
         }

.. example:: Definition of elements within the super structure

   .. comp:: Component A
      :id: C_A
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_A_OUT
         :output: IP_C_C_IN


   .. comp:: Component B
      :id: C_B
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_B_OUT
         :output: IP_C_C_IN2


   .. comp:: Component C
      :id: C_C
      :part_of: LIB_MY_LIB

      .. inport:: in
         :id: IP_C_C_IN
         :input: OP_C_A_OUT

      .. inport:: in
         :id: IP_C_C_IN2
         :input: OP_C_B_OUT

      .. outport:: out
         :id: OP_C_C_OUT
         :output: IP_C_D_IN


   .. comp:: Component D
      :id: C_D
      :part_of: LIB_MY_LIB

      .. inport:: in
         :id: IP_C_D_IN
         :input: OP_C_C_OUT


To show the different repesentations of ``A -> B`` (output) vs ``B <- A`` (input).

.. example:: Visualize the dependencies - Input

   .. needflow::
      :filter: is_need and docname == "architecture-examples" and section_name == "Visial representation of UML Ports in Sphinx-Needs"
      :link_types: input, part_of
      :show_link_names:
      :debug:

   .. needflow::
      :filter: is_need and docname == "architecture-examples" and section_name == "Visial representation of UML Ports in Sphinx-Needs" and type != "lib"
      :link_types: input
      :show_link_names:
      :debug:

.. example:: Visualize the dependencies - Output

   .. needflow::
      :filter: is_need and docname == "architecture-examples" and section_name == "Visial representation of UML Ports in Sphinx-Needs"
      :link_types: output, part_of
      :show_link_names:
      :debug:

   .. needflow::
      :filter: is_need and docname == "architecture-examples" and section_name == "Visial representation of UML Ports in Sphinx-Needs" and type != "lib"
      :link_types: output
      :show_link_names:
      :debug:


Visiual repesentation of many Elements
======================================

Following the link to the elements defined.

.. toctree::
   :maxdepth: 1

   architecture-many-components

.. example:: Visualize many elements with needflow

   .. needflow::
      :filter: is_need and docname == "architecture-many-components"
      :show_link_names:
      :debug:


.. example:: Visualize many elements with needuml I

   .. needuml::
      :debug:

      {%- set components = filter("docname == 'architecture-many-components'") -%}
      '{{components}}
      {% for need in filter("docname == 'architecture-many-components'") %}
      {{flow(need.id)}}
      {% endfor %}


.. example:: Visualize many elements with needuml II

   .. needuml::
      :debug:

      'the packages are project specific and defined in needs_render_context in conf.py
      {% for p in packages %}
      package {{p["name"]}} {
      ' import elements
      {% for e in p["elements"] %}
      {{flow(e)}}
      {% endfor %}
      ' connect elements
      {% for e in p["elements"] %}
      {%- if loop.previtem is defined -%}
      {{loop.previtem}} #-# {{e}}
      {# here it is important to use #-#, as - has a left / right alignment and -- has up / down alignment #}
      {% endif %}
      {% endfor %}
      }
      {% if loop.previtem is defined %}
      ' connect packages with hidden link to nice align elements
      {{loop.previtem["name"]}} --[hidden] {{p["name"]}}
      {% endif %}
      {% endfor %}


Behaviour Model: Sequence-Diagram
*********************************

Configuration
=============

Here we use monkey patching to get in functions in class `JinjaFunctions`
from sphinx-needs. Currently used functions:

- sequence
- sequence2
- sequence3

The patching is been done in `metamodel.py`.

Example with sequence
=====================

.. example:: Visualize a sequence diagram I

   .. needuml::
      :debug:

      'add your needed sphinx-needs elements to the list "components"
      {%- set components = ['C_A', 'C_B', 'C_C', 'C_D',] -%}
      {% for c in components %}
      'c = {{c}}
      {{sequence(needs, c)}} {{ref(c)}}
      {% endfor %}

      'here you can add your plantuml sequence diagramm code.
      'documentation can be found here: https://plantuml.com/en/sequence-diagram

      activate C_C

      'If you want to higlight a group of interactions are part of "port's",
      'you can use "group" as with the following example:
      group "{{ref('OP_C_A_OUT', option='title')}} {{ref('IP_C_C_IN', option='title')}}"
      C_A <- C_C : subscribe for service
      activate C_A
      C_A -> C_C : agree on subscribtion
      C_A -> C_C : send data
      deactivate C_A
      end

      group "{{ref('OP_C_B_OUT', option='title')}} {{ref('IP_C_C_IN2', option='title')}}"
      C_B <- C_C : subscribe for service
      activate C_B
      C_B -> C_C : agree on subscribtion
      C_B -> C_C : send data
      deactivate C_B
      end

      group "{{ref('OP_C_C_OUT', option='title')}} {{ref('IP_C_D_IN', option='title')}}"
      C_C -> C_D : send data
      end

      deactivate C_C

Example with sequence2
======================

.. example:: Visualize a sequence diagram II

   .. needuml::
      :debug:

      'add your needed sphinx-needs elements to the list "components"
      {%- set components = ['C_A', 'C_B', 'C_C', 'C_D',] -%}
      {% for c in components %}
      'c = {{c}}
      {{sequence2(context, c)}} {{ref(c)}}
      {% endfor %}

      'If you want to higlight a group of interactions are part of "port's",
      'you can use "group" as with the following example:
      group "{{ref('OP_C_A_OUT', option='title')}} {{ref('IP_C_C_IN', option='title')}}"
      C_A <- C_C : subscribe for service
      activate C_A
      C_A -> C_C : agree on subscribtion
      C_A -> C_C : send data
      deactivate C_A
      end

Example with sequence3
======================

.. example:: Visualize a sequence diagram III

   .. needuml::
      :debug:

      'add your needed sphinx-needs elements to the list "components"
      {%- set components = ['C_A', 'C_B', 'C_C', 'C_D',] -%}
      {% for c in components %}
      'c = {{c}}
      {{sequence3(c)}} {{ref(c)}}
      {% endfor %}

      'If you want to higlight a group of interactions are part of "port's",
      'you can use "group" as with the following example:
      group "{{ref('OP_C_A_OUT', option='title')}} {{ref('IP_C_C_IN', option='title')}}"
      C_A <- C_C : subscribe for service
      activate C_A
      C_A -> C_C : agree on subscribtion
      C_A -> C_C : send data
      deactivate C_A
      end


How-to referring to Diagrams within a Need
******************************************

It is not directly possible to refernce to a needarch (diagram).
So we introduce here a `needpart <https://sphinx-needs.readthedocs.io/en/stable/roles.html#need-part-np>`_ in the need,
so we can reference to these.

.. example:: How-to referring to Diagrams within a Need

   .. comp:: Component with Diagrams
      :id: C_DIAGRAMS

      .. needarch::
         :debug:

         {{flow(need().id)}}

      :np:`(Sequence)` Diagram

      .. needarch::
         :key: Sequence
         :debug:

         participant {{need().id}} {{ref(need().id)}} [
         {{need().title}}
         ----
         Here is a bug in safari, it is been rendered correct in firefox.
         With explicite link text:
         {{ref(need().id + '.Deployment', text="Deployment Diagram")}}
         {{ref(need().id + '.Sequence', text="Sequence Diagram")}}
         With link text from needpart id:
         {{ref(need().id + '.Deployment', option="id")}} Diagram
         {{ref(need().id + '.Sequence', option="id")}} Diagram
         ]

   .. comp:: Component linking to Diagrams within another Need
      :id: C_LINK2DIAGRAMS
      :links: C_DIAGRAMS.Deployment, C_DIAGRAMS.Sequence

      Link to the Deployment Diagram of Component :need:`C_DIAGRAMS`: :need:`C_DIAGRAMS.Deployment`

      Link to the Sequence Diagram of Component :need:`C_DIAGRAMS`: :need:`C_DIAGRAMS.Sequence`

      .. needarch::
         :debug:

         {{flow(need().id)}}

      :np:`(Internal)` Diagram

      .. needarch::
         :key: Internal
         :debug:

         {{flow(need().id)}}
         {{uml('C_DIAGRAMS', 'Deployment')}}
         {{need().id}} -> C_DIAGRAMS : uses Deployment Diagram

      :np:`(Sequence)` Diagram

      .. needarch::
         :key: Sequence
         :debug:

         {{sequence3(need().id)}} {{ref(need().id)}}
         {{uml('C_DIAGRAMS', 'Sequence')}}

         {{need().id}} -> C_DIAGRAMS : uses Sequence Diagram

   **How it is been in the native datamodel**

   Finally a `needflow` to show the datamodel represenatation:

   .. needflow::
      :filter: docname == "architecture-examples" and section_name == "How-to referring to Diagrams within a Need"
      :show_link_names:
      :debug:


Template needarch to needs
**************************

It is possible to use `needarch`_ and `needuml`_ in Sphinx-Needs `template`_.
You can set the template explicite in the need element itself or over `needs_global_options`_.

Within this file we currently set generic views on needs elements of type comp.
This is been done with a `needs_global_options`_ configuration within `metamodel.py`.

As `template`_ are jinja templates, even like `needarch`_ and `needuml`_,
we have to `escape <https://jinja.palletsprojects.com/en/3.0.x/templates/#escaping>`_ the jinja templates
in the needs_template with ```{% raw %} ... {% endraw %}```.

You can find an example in the `needs_templates/arch_template.need`:

.. literalinclude:: needs_templates/arch_template.need
   :language: rst
   :linenos:

.. target-notes::

.. _`needflow` : https://sphinx-needs.readthedocs.io/en/latest/directives/needflow.html

.. _`needarch` : https://sphinx-needs.readthedocs.io/en/latest/directives/needarch.html

.. _`needuml` : https://sphinx-needs.readthedocs.io/en/latest/directives/needuml.html

.. _`needs-render-context` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-render-context

.. _`plantuml deployment-diagram` : http://plantuml.com/deployment-diagram

.. _`template` : https://sphinx-needs.readthedocs.io/en/latest/directives/need.html#template

.. _`needs_global_options` : https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-global-options

