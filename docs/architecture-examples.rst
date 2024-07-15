##########################################
How-To model Archiecture with Sphinx-Needs
##########################################



.. example:: Definiton of a super structure element

   .. lib:: My lib
      :id: LIB_MY_LIB

.. example:: Definiton of elements within the super structure

   .. comp:: Component A
      :id: C_A
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_A_OUT

   .. comp:: Component B
      :id: C_B
      :part_of: LIB_MY_LIB

      .. outport:: out
         :id: OP_C_B_OUT

   .. comp:: Component C
      :id: C_C
      :part_of: LIB_MY_LIB

      .. inport:: in
         :id: OP_C_C_IN
         :input: OP_C_A_OUT
         :output: OP_C_A_OUT

      .. outport:: out
         :id: OP_C_C_OUT

   .. comp:: Component D
      :id: C_D
      :part_of: LIB_MY_LIB

      .. inport:: in
         :id: OP_C_D_IN
         :input: OP_C_C_OUT
         :output: OP_C_C_OUT


.. example::

   .. needflow::
      :filter: docname == "architecture-examples"
      :show_link_names:
