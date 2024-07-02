#################
Reasoning and Why
#################

Norms
*****

There are many different reasons, why you need bidirectional traceability.
E.g. in the automotive industry it is the ISO26262 or ASPICE.

As the ASPICE specification is public available let's what is requested:
https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf

Or within is documentation for Version Automotive-SPICE-PAM-v4.1 
:numref:`{name} <ASPICE-V31-Figure-D4—Bidirectional-traceability-and-consistency>`.

.. toctree::
   :caption: ASPICE
   :maxdepth: 1

   AutomotiveSPICE_PAM_31/AutomotiveSPICE_PAM_31
   AutomotiveSPICE_for_Cybersecurity/AutomotiveSPICE_for_Cybersecurity

Implemented with Sphinx-Needs
*****************************

With Sphinx-Needs we get one tool to cover all demands of ASPICE
(often you want to use a planning tool for change request management).
Everything should be reviewed with `github pull-requests <https://docs.github.com/en/pull-requests>`_ or 
`gitlab merge requests <https://docs.gitlab.com/ee/user/project/merge_requests/>`_ as a single point of review tool.
You can protect branches with rules, so you can enforce all content is reviewed.

If you want to use sphinx-needs even as your ticket management tool, here are some hints:

- You could use https://docs.github.com/en/actions/examples/using-the-github-cli-on-a-runner
  to create github issues automatically (peter-evans/create-issue-from-file),
- You could use https://sphinx-needs.readthedocs.io/en/latest/directives/needgantt.html
  and a need of a self defined type like ticket to manage work packages.


You can find a Example with all classical ASPICE artifacts in this open source repository:

- gitlab:

  - Repository: https://gitlab.com/PhilipPartsch/reconf2023-product-as-code
  - Hosted documentation: https://reconf2023-product-as-code-philippartsch-a4d4571b1b7e4136d3bdb6.gitlab.io/
  - Pipeline: https://gitlab.com/PhilipPartsch/reconf2023-product-as-code/-/pipelines

- github:

  - Repository: https://github.com/PhilipPartsch/ReConf2023-Product-As-Code
  - Hosted documentation: https://reconf2023-product-as-code.readthedocs.io
  - Pipeline: https://readthedocs.org/projects/reconf2023-product-as-code/builds/



