.. _sphinx_import_needs:

##########################
Sphinx-Needs: Import Needs
##########################


Import a Need with `needimport`
*******************************

Documentation: How-to import needs with
`needimport <https://sphinx-needs.readthedocs.io/en/latest/directives/needimport.html>`_.

.. example:: How-to import a Need.

   .. needimport:: example_needs9.json
      :id_prefix: imp_
      :tags: imported
      :template: extend_template

We do use here a template, to make the `reject_reason` availalbe to the content of the need.
The `reject_reason` is been set in the `needextend` in the next chapter.

In the template `extend_template` we access to the reject reason:

.. literalinclude:: needs_templates/extend_template.need
   :caption: file extend_template.need
   :language: jinja
   :linenos:

You can find the documenation of the option `template` for `needimport` in
`needimport customization <https://sphinx-needs.readthedocs.io/en/latest/directives/needimport.html#customization>`_.

You can find the documenation of the option `template` for `need` in
`need template <https://sphinx-needs.readthedocs.io/en/latest/directives/need.html#template>`_.

You can find the documentation of dynamic functions and the copy function especially in
`dynamic functions <https://sphinx-needs.readthedocs.io/en/latest/dynamic_functions.html#copy>`_.

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

Challanges
**********

The issue with `needextend` is, how to ensure the final output is correct.
Here it is often necassary to protect attributes for changes via `needextend` via `needs_warnings`.
See `Monitoring modifications <https://sphinx-needs.readthedocs.io/en/latest/directives/needextend.html#monitoring-modifications>`_.
