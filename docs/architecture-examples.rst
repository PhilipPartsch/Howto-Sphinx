##########################################
How-To model Archiecture with Sphinx-Needs
##########################################

Pay attention: We do use ``:input:`` and ``:output:`` in the same datamodel.
This is only because to see the differences in the output of plantuml tooling.
Especially the ordering of links like ``A -> B`` vs ``B <- A``.

.. example:: Definiton of a super structure element

   .. lib:: My lib
      :id: LIB_MY_LIB

      .. needarch::
         :key: Component
         :debug:

         left to right direction
         'top to bottom direction

         'Define elements
         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().part_of_back %}
         '{{e}}
         {% if needs[e].type == "comp" %}{{uml(e, 'Component')}}{% endif %}
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
         :key: Component2
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

      .. needarch::
         :key: Component
         :debug:

         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().parent_needs_back %}
         '{{e}}
         {% if needs[e].parent_need == need().id and (needs[e].type == "outport" or needs[e].type == "inport") %}{{uml(e)}}{% endif %}
         {% endfor %}
         }


   .. comp:: Component B
      :id: C_B
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_B_OUT
         :output: IP_C_C_IN2

      .. needarch::
         :key: Component

         {{flow(need().id)}} {
         {% for e in need().parent_needs_back %}
         {% if needs[e].parent_need == need().id and (needs[e].type == "outport" or needs[e].type == "inport") %}{{uml(e)}}{% endif %}
         {% endfor %}
         }


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

      .. needarch::
         :key: Component

         {{flow(need().id)}} {
         {% for e in need().parent_needs_back %}
         {% if needs[e].parent_need == need().id and (needs[e].type == "outport" or needs[e].type == "inport") %}{{uml(e)}}{% endif %}
         {% endfor %}
         }


   .. comp:: Component D
      :id: C_D
      :part_of: LIB_MY_LIB

      .. inport:: in
         :id: IP_C_D_IN
         :input: OP_C_C_OUT

      .. needarch::
         :key: Component

         {{flow(need().id)}} {
         {% for e in need().parent_needs_back %}
         {% if needs[e].parent_need == need().id and (needs[e].type == "outport" or needs[e].type == "inport") %}{{uml(e)}}{% endif %}
         {% endfor %}
         }


.. example:: Visialize the dependencies - Input

   .. needflow::
      :filter: docname == "architecture-examples"
      :link_types: input, part_of
      :show_link_names:
      :debug:

   .. needflow::
      :filter: docname == "architecture-examples" and type != "lib"
      :link_types: input
      :show_link_names:
      :debug:

.. example:: Visialize the dependencies - Output

   .. needflow::
      :filter: docname == "architecture-examples"
      :link_types: output, part_of
      :show_link_names:
      :debug:

   .. needflow::
      :filter: docname == "architecture-examples" and type != "lib"
      :link_types: output
      :show_link_names:
      :debug:


.. example:: Visulize a sequence diagram

   .. needuml::
      :debug:

      {%- set components = ['C_A', 'C_B', 'C_C', 'C_D',] -%}
      {% for c in components %}
      'c = {{c}}
      {{sequence(needs, c)}} {{ref(c)}}
      {% endfor %}

      'group "{{ref('OP_C_A_OUT', option='title')}} {{ref('OP_C_C_IN', option='title')}}"
      group "{{ref('OP_C_A_OUT', option='title')}}"
      C_A -> C_C
      end
      C_A -> C_C
      C_B -> C_C
      C_C -> C_D

