.. _tickets_example:

####################
Examples for Tickets
####################

Here I collect examples to feedbacks of sphinx-needs tickets.

Coloring of needs depending of incoming links
=============================================

**Question:**

I would like to set the style of a need, if an incoming link is available.
I've tried it by using needs_global_options

.. code:: py

   needs_global_options = {
      "style": {
         "predicates":  [
               ("len(links_back)==0", "red_bar"),
               ("len(links_back)>0", "green_bar"),
            ]
      }
   }

With this option all requirements have the red bar, even there is an incoming link.

Another idea was to use dynamic functions,
but the incmoing links are not available as written in the documentation:
https://sphinx-needs.readthedocs.io/en/latest/dynamic_functions.html#incoming-links

I have imported system requirements and I would like to see very fast,
which requirement is already linked by a color bar.
Any ideas or suggestions how to realize this?

**Answer:**

Here is an implmentation of the feature.

It is not covering the needs_global_options, but to do so, is straight forward.
So I focused to set it manually in the following needs.

.. example::

   .. need:: need red if linked
      :id: N_NEED_RED_IF_LINKED
      :style: red_bar
      :tags: [[check_need_back_linked()]]

   .. need:: link to need
      :id: N_LINK_TO_RED_NEED
      :links: N_NEED_RED_IF_LINKED

