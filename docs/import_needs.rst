.. _sphinx_import_needs:

#########################
Sphinx-Needs Import Needs
#########################


Import a Need with `needimport`
*******************************

Documentation: How-to import needs with
`needimport <https://sphinx-needs.readthedocs.io/en/latest/directives/needimport.html>`_.

.. example:: How-to import a Need.

   .. needimport:: example_needs.json
      :id_prefix: imp_
      :tags: imported
      :template: extend_template

We do use here a template, to make the `reject reason`` avaialbe to the content of the need.
The `reject reason` is been set in the `needextend` in the next chapter.

In the template `extend_template` we access to the reject reason:

.. literalinclude:: needs_templates/extend_template.need
   :language: rst
   :linenos:


How-to change a imported need with `needextend`
***********************************************

Documentation: How-to extend needs with
`needextend <https://sphinx-needs.readthedocs.io/en/latest/directives/needextend.html>`_.

.. example:: How-to extend a Need.

   .. needextend:: imp_test_item
      :status: implemented
      :reject_reason: 
         | Here I add a multi line reject reason.
         | First line
         | Second line
