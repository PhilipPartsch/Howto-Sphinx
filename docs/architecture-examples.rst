##########################################
How-To model Archiecture with Sphinx-Needs
##########################################



.. example:: Definiton of a super structure element

   .. lib:: My lib
      :id: LIB_MY_LIB

      .. needarch::
         :key: Component
         :debug:

         '{{need()}}
         {{flow(need().id)}} {
         {% for e in need().part_of_back %}
         '{{e}}
         {% if e.type == "comp" %}{{uml(e, 'Component')}}{% endif %}
         {{uml(e, 'Component')}}
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
         {% if (e.type == "outport" or e.type == "inport") %}{{uml(e)}}{% endif %}
         {{uml(e)}}
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
         {% if e.parent_need == need().id and (e.type == "outport" or e.type == "inport") %}{{uml(e)}}{% endif %}
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
         {% if e.parent_need == need().id and (e.type == "outport" or e.type == "inport") %}{{uml(e)}}{% endif %}
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
         {% if e.parent_need == need().id and (e.type == "outport" or e.type == "inport") %}{{uml(e)}}{% endif %}
         {% endfor %}
         }


.. example:: Visialize the dependencies

   .. needflow::
      :filter: docname == "architecture-examples"
      :show_link_names:
