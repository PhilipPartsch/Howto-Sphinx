##########################################
How-To model Archiecture with Sphinx-Needs
##########################################



.. example:: Definiton of a super structure element

   .. lib:: My lib
      :id: LIB_MY_LIB

      .. needarch::
         :key: Component
         :debug:

         'Define elements
         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().part_of_back %}
         '{{e}}
         {% if needs[e].type == "comp" %}{{uml(e, 'Component')}}{% endif %}
         {% endfor %}
         }

         'Link defined elements
         {% for e in need().part_of_back %}
         'e = {{e}}
         {%- if needs[e].type == "comp" -%}
         {% for f in needs[e].parent_needs_back %}
         'f = {{f}}
         {%- if (needs[f].type == "inport") -%}
         {% for g in needs[f].input %}
         'g = {{g}}
         {{g}} -> {{f}}
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

.. example:: Definiton of elements within the super structure

   .. comp:: Component A
      :id: C_A
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_A_OUT

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


.. example:: Visialize the dependencies

   .. needflow::
      :filter: docname == "architecture-examples"
      :show_link_names:
