import os
import sys
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('scripts')) # for gitlink
from gitlink import get_githoster_edit_url_for_need

from sphinx_needs.config import NeedsSphinxConfig
from sphinx_needs.filter_common import filter_needs


# sphinx_needs configuration
needs_id_regex = '^[A-Za-z0-9_-]{3,}'

# Define project specific needs directives

needs_types = [
               # Process-As-Code
               # Role
               dict(directive="prole", title="Role", prefix="ROLE_", color="#ffffff", style="actor"),

               # Strategy
               dict(directive="strategy", title="Strategy", prefix="STGY_", color="#ffffff", style="hexagon"),

               # Process
               dict(directive="process", title="Process", prefix="PROC_", color="#ffffff", style="package"),
               dict(directive="activity", title="Activity", prefix="ACT_", color="#ffffff", style="card"),
               dict(directive="artifact", title="Artifact", prefix="ART_", color="#ffffff", style="artifact"),
               dict(directive="pstatus", title="Status", prefix="STATUS_", color="#ffffff", style="artifact"), # Child of Artifact

               # Instruction
               dict(directive="template", title="Template", prefix="TEMP_", color="#ffffff", style="frame"),
               dict(directive="instruction", title="Work Instruction", prefix="INST_", color="#ffffff", style="frame"),

               # Storage
               dict(directive="repo", title="Repository", prefix="REPO_", color="#ffffff", style="database"),

               # Timeline
               dict(directive="lifecycle", title="Lifecycle", prefix="CYCLE_", color="#ffffff", style="card"),
               dict(directive="phase", title="Phase", prefix="PHASE_", color="#ffffff", style="rectangle"),
               dict(directive="milestone", title="Milestone", prefix="MILE_", color="#ffffff", style="hexagon"),

               # Product-As-Code

               # Requirements
               dict(directive="stake_req", title="Stakeholder Requirement", prefix="CSTRQ_", color="#abcdef", style="artifact"),
               dict(directive="sys_req", title="System Requirement", prefix="SYSRQ_", color="#abcdef", style="artifact"),
               dict(directive="sw_req", title="Software Requirement", prefix="SWRQ_", color="#abcdef", style="artifact"),

               # Architecture & Design
               dict(directive="bin", title="Binary", prefix="BIN_", color="#abcdef", style="rectangle"),
               dict(directive="lib", title="Library ", prefix="LIB_", color="#abcdef", style="rectangle"),
               dict(directive="package", title="Package", prefix="P_", color="#abcdef", style="package"),
               dict(directive="arch_module", title="Module", prefix="M_", color="#abcdef", style="package"),
               dict(directive="comp", title="Component", prefix="C_", color="#abcdef", style="component"),
               dict(directive="unit", title="Unit", prefix="U_", color="#abcdef", style="rectangle"),
               dict(directive="interface", title="Interface", prefix="IF_", color="#abcdef", style="card"),
               dict(directive="decision", title="Decision", prefix="D_", color="#efff9c", style="artifact"),
               dict(directive="inport", title="InPort", prefix="IP_", color="#abcdef", style="portin", sequence_style="control"),
               dict(directive="outport", title="OutPort", prefix="OP_", color="#abcdef", style="portout", sequence_style="control"),

               # Test
               dict(directive="test_spec", title="Test Specification", prefix="TS_", color="#abcdef", style="artifact"),
               dict(directive="test_coverage", title="Test Coverage", prefix="TCOVER_", color="#abcdef", style="artifact"),
               dict(directive="sys_test", title="System Test", prefix="SYSTST_", color="#abcdef", style="artifact"),
               dict(directive="sw_test", title="Software Test", prefix="SWTST_", color="#abcdef", style="artifact"),

               # Generic
               dict(directive="evaluation", title="Evaluation", prefix="EVAL_", color="#abcdef", style="artifact"),
               dict(directive="verify", title="Verification Information", prefix="VERIFY_", color="#abcdef", style="artifact"),

               # From Sphinx-needs Standards:
               dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node"),

               # For documentation
               dict(directive="element", title="Element", prefix="E_", color="#BFD8D2", style="component"),

              ]

# Define extra options for needs object
needs_extra_options = [
   'author', # to store the author of a stakeholder requirement
   'safety_level',
   'security_level',
   'reject_reason',
   'coverage', # to store test coverage in %
   'pathfile', # file path in needs e.g. for test coverage
   'interface_definition', # to store in machine readable code interface definition
   'test_status',

   'github_edit_url',
]

needs_services = {}

needs_extra_links = [
   # generic links
   {
      "option": "links",
      "incoming": "links incoming",
      "outgoing": "links outgoing",
      "style": "#000000",
      "style_start": "-",
      "style_end": "-",
   },
   #Used to indicate a generic description is been specialized
   {
      "option": "derived",
      "incoming": "Detailed in",
      "outgoing": "Derived from",
      "style": "#000000",
      "style_start": "-",
      "style_end": "-<>",
   },
   # Process to Process link
   {
      "option": "successor",
      "incoming": "Predecessor",
      "outgoing": "Successor",
      "style": "#000000",
      "style_start": "-",
      "style_end": "right->",
   },
   # Process to Activity link
   {
      "option": "activities",
      "incoming": "Process",
      "outgoing": "Activities",
      "style": "#000000",
   },
   # Activity to Phase link
   {
      "option": "when",
      "incoming": "contains",
      "outgoing": "executed in",
   },
   # Activity to Work Instruction link
   {
      "option": "instruction",
      "incoming": "Activity",
      "outgoing": "Instruction",
      "style": "#000000",
   },
   # links from Activity to Artifacts
   {
      "option": "input",
      "incoming": "consumed by",
      "outgoing": "input",
      "style": "#000000",
      "style_start": "<-",
      "style_end": "-",
   },
   {
      "option": "output",
      "incoming": "generated by",
      "outgoing": "output",
      "style": "#000000",
   },
   # links to roles
   {# responsible:
      "option": "responsible",
      "incoming": "Responsible for",
      "outgoing": "Responsible",
      "style": "#000000",
      "style_start": ".",
      "style_end": "up.",
   },
   { # part of - to indicate that this role is a part of another role
      "option": "part_of",
      "incoming": "Includes",
      "outgoing": "Part of",
      "style": "#000000",
      "style_start": "-down",
      "style_end": "->",
   },
   # links to repos and artifacts (an artifact can be stored in another artifact)
   {
      "option": "stored_in",
      "incoming": "to be stored",
      "outgoing": "stored in",
      "style": "#000000",
   },
   # link to a artifact from a template
   {
      "option": "blue_print",
      "incoming": "Template",
      "outgoing": "Template for",
      "style": "#000000",
   },
   # link to a process justification
   {
      "option": "why",
      "incoming": "Resolved with",
      "outgoing": "Justification",
      "style": "#000000",
   },
   # link from a software requirement to stakeholder requirement
   {
      "option": "satisfies",
      "incoming": "is satisfied by",
      "outgoing": "satisfies",
      "style_start": "-up",
      "style_end": "->",
   },
   # link from a requirement or archiecture element to a test specifiction
      {
      "option": "tests",
      "incoming": "tested by",
      "outgoing": "tests",
      "style_start": "-up",
      "style_end": "->"
   },
   {
      "option": "verified_by",
      "incoming": "verifies",
      "outgoing": "verified by",
      "style_start": "<-up",
      "style_end": "-"
   },
   # link from a requirement to an archiecture element
   {
      "option": "implemented_by",
      "incoming": "implemented by",
      "outgoing": "implements"
   },
   # from evaluation report to artifact under evalaution
   {
      "option": "evaluated",
      "incoming": "evaluated by",
      "outgoing": "evaluated",
      "style_start": "-up",
      "style_end": "->",
   },
   # links from Activity to Artifacts
   {
      "option": "uses",
      "incoming": "consumed by",
      "outgoing": "uses",
      "style": "#000000",
      "style_start": "<-right",
      "style_end": "-",
   },
   {
      "option": "implements",
      "incoming": "implemented by",
      "outgoing": "implements",
      "style_start": "-up",
      "style_end": "->"
   },
]

#needs_default_layout
needs_layouts = {
    "clean_with_edit_link": {
        "grid": "simple",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>>   '
                '<<link(url="github_edit_url", image_url="icon:edit", image_height="17", image_width="17", is_dynamic=True)>>'
            ],
            "meta": [
                '<<meta_all(no_links=True, exclude=["layout", "post_template", "style", "delete", "jinja_content", "github_edit_url"])>>',
                '<<meta_links_all()>>'
            ],
        },
    },
}

def check_verified(app, need, needs, *args, **kwargs):
    """
    :param app: sphinx app
    :param need: current need
    :param needs: dictionary of all needs. Key is the need id
    :return: str,int,float or list of elements of type str,int,float
    """

    if need['status'] == 'verified':
        # At time dynamic function is been executed incoming links are not resolved.
        # We have to search back by ourself.
        tests_back_list = []
        for n in needs.values():
            if need['id'] in n['tests']:
                tests_back_list.append(n['id'])
        if len(tests_back_list) > 0:
            result_passed = True
            for test_by in tests_back_list:
                if needs[test_by]['type'] == 'test_spec' and needs[test_by]['status'] == 'verified':
                    if len(needs[test_by]['verified_by']) > 0:
                        for current_verified_by in needs[test_by]['verified_by']:
                            result_passed = result_passed and needs[current_verified_by]['cases'].isdigit() and (int(needs[current_verified_by]['cases']) > 0)
                            result_passed = result_passed and (needs[current_verified_by]['cases'] == needs[current_verified_by]['passed'])
                            if not result_passed:
                                return 'failed test cases => failed'
                                break
                        if not result_passed:
                                break
                    else:
                        # no test result linked => failed
                        # print('no test result linked => failed')
                        result_passed = False
                        return 'no test result linked => failed'
                        break
                else:
                    # a not verified test spec linked => failed
                    # print('a not verified test spec linked => failed')
                    result_passed = False
                    return 'a not verified test spec linked => failed'
                    break

            if result_passed:
                return 'verified_passed'
            else:
                return 'verified_failed'

        else:
            return ''
    else:
        return ''

def fetch_elements(app, need, needs, *args, **kwargs):
    """
    :param app: sphinx app
    :param need: current need
    :param needs: dictionary of all needs. Key is the need id
    :param filter: str | None = None
    :return: str,int,float or list of elements of type str,int,float
    """
    linked = []
    if 'filter' in kwargs:
        filter = kwargs['filter']
        import inspect
        filter_needs_signature = inspect.signature(filter_needs)
        if 'location' in filter_needs_signature.parameters:
            linked_needs = filter_needs(
                needs.values(),
                NeedsSphinxConfig(app.config),
                filter,
                need,
                location=(need["docname"], need["lineno"]) if need["docname"] else None,
            )
        else:
            linked_needs = filter_needs(
                needs.values(),
                NeedsSphinxConfig(app.config),
                filter,
                need
            )

        linked = [nd['id'] for nd in linked_needs]
    else:
        import warnings
        warnings.warn("fetch_elements function called without a filter parameter")

    return linked

needs_functions = [check_verified, fetch_elements]

needs_global_options = {
    'test_status': {'predicates': [('type=="sw_req"', '[[check_verified()]]')]},
    'post_template': {'predicates': [('type=="evaluation"', 'evaluation_post_template')]},
    'template': {'predicates': [('type=="comp" and docname == "architecture-examples"', 'arch_template')]},
    'github_edit_url': {'default': '[[get_githoster_edit_url_for_need("id")]]'}
}

needs_render_context = {
}

needs_warnings = {
    'artifact_without_stored_in_link': "type == 'artifact' and len(stored_in) == 0",
    # currently disabled, as norms do not set the author
    # 'stakeholder_requirement_without_author': "type == 'stake_req' and not author",
    'author_only_allowed_for_stakeholder_requirement': "type != 'stake_req' and author != ''",
    'evaluation_output_and_evaluated_needed': "type == 'evaluation' and (len(output) == 0 or len(evaluated) == 0)",
    'invalid_status' : "type not in ['req', 'spec', 'need', 'element'] and status is not None and status not in ['new', 'changed', 'accepted', 'implemented', 'verified']",
}


# _not_following_naming_convention
for type in needs_types:

    if type['directive'] == 'stake_req':
        # We cannot enforce ID's of stakeholder requirements.
        continue

    warn_text = type['directive'] + '_not_following_naming_convention'
    if warn_text not in needs_warnings:
        warn_test = "type == '" + type['directive'] + "' and not id.startswith('" + type['prefix'] + "')"
        needs_warnings[warn_text] = warn_test
    else:
        # todo: add warning
        pass

needs_string_links = {
    # Links to the related github user
    'github_user': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://github.com/{{value}}',
        'link_name': 'GitHub User {{value}}',
        'options': ['author'],
    },
}

needs_external_needs = [
    {
        'base_url': 'https://reconf2023-product-as-code-philippartsch-a4d4571b1b7e4136d3bdb6.gitlab.io',
        'json_url':  'https://reconf2023-product-as-code-philippartsch-a4d4571b1b7e4136d3bdb6.gitlab.io/needs.json',
        'css_class': 'external_link',
    },
]

needs_diagram_template = """{%- if is_need and ( type == 'inport' or type == 'outport') -%}
**{{title|wordwrap(15, wrapstring='**\\\\n**')}}**
{%- elif is_need -%}
<size:12>{{type_name}}</size>\\n**{{title|wordwrap(15, wrapstring='**\\\\n**')}}**\\n<size:10>{{id}}</size>
{%- else -%}
<size:12>{{type_name}} (part)</size>\\n**{{content|wordwrap(15, wrapstring='**\\\\n**')}}**\\n<size:10>{{id_parent}}.**{{id}}**</size>
{%- endif -%}"""



dict_needs_types = {}
for nt in needs_types:
    dict_needs_types[nt['directive']] = nt

# you do have to import "JinjaFunctions" from "sphinx-needs/sphinx_needs/directives/needuml.py"
# and extend functions. Not done here, is only a fast hack :)

def sequence(needs, id):

    # check that id is part of needs and raise excpetion if not.

    need_id = id
    node_text = needs[id]["title"]
    need_type = needs[id]["type"]
    if "sequence_style" in dict_needs_types[need_type]:
        style = dict_needs_types[need_type]["sequence_style"]
    else:
        style = "participant"

    need_uml = '{style} "{node_text}" as {id}'.format(
        id=need_id,
        node_text=node_text,
        style=style,
    )

    return need_uml

# sequence def end
# above comment, is for automatically extracting code to the documentation

from sphinx_needs.directives.needuml import JinjaFunctions

def class_sequence(self, need_id: str) -> str:

    needs = self.needs

    return sequence(needs, need_id)

JinjaFunctions.class_sequence = class_sequence

from sphinx_needs.directives.needuml import NeedumlException
from sphinx_needs.utils import split_need_id
from sphinx_needs.diagrams_common import calculate_link
import copy

def ref_new(
        self, need_id: str, option: str = "", text: str = ""
    ) -> str:

    need_id_main, need_id_part = split_need_id(need_id)

    if need_id_main not in self.needs:
        raise NeedumlException(
            f"Jinja function ref is called with undefined need_id: '{need_id}'."
        )

    if (option != "" and text != ""):
        raise NeedumlException(
            "Jinja function ref requires 'option' or 'text', not both"
        )

    if need_id_part:
        # We are changing the needinfo, so we need a deepcopy, to not change the original data.
        need_info = copy.deepcopy(self.needs[need_id_main])

        if need_id_part not in need_info["parts"]:
            raise NeedumlException(
                f"Jinja function ref is called with undefined need_id part: '{need_id}'."
            )

        # This algorithm is following the implmentation of needref
        need_info["id"] = need_id_part
        need_info["title"] = need_info["parts"][need_id_part]["content"]
        need_info["is_part"] = True
        need_info["is_need"] = False

    else:
        need_info = self.needs[need_id_main]

    if (option != "" and option not in need_info):
        raise NeedumlException(
            f"Jinja function ref is called with undefined option '{option}' for need '{need_id}'."
        )

    link = calculate_link(self.app, need_info, self.fromdocname)
    content: str = need_info.get(option, "") if option != "" else text
    content = content.strip(' \t\n\r')

    need_uml = "[[{link}{seperator}{content}]]".format(
        link=link,
        seperator=" " if content != "" else "",
        content=content,
    )

    return need_uml

JinjaFunctions.ref_new = ref_new

from sphinx_needs.directives.needuml import jinja2uml

from sphinx.application import Sphinx
from sphinx_needs.directives.needuml import ProcessedNeedsType
from jinja2 import BaseLoader, Environment, Template
from typing import TYPE_CHECKING, Any, Dict, List, Sequence, TypedDict

def jinja2uml_new(
    app: Sphinx,
    fromdocname: None | str,
    uml_content: str,
    parent_need_id: None | str,
    key: None | str,
    processed_need_ids: ProcessedNeedsType,
    kwargs: dict[str, Any],
) -> tuple[str, ProcessedNeedsType]:
    # Let's render jinja templates with uml content template to 'plantuml syntax' uml
    # 1. Remove @startuml and @enduml
    uml_content = uml_content.replace("@startuml", "").replace("@enduml", "")

    # 2. Prepare jinja template
    mem_template = Environment(loader=BaseLoader()).from_string(uml_content)

    # 3. Get a new instance of Jinja Helper Functions
    jinja_utils = JinjaFunctions(app, fromdocname, parent_need_id, processed_need_ids)

    # 4. Append need_id to processed_need_ids, so it will not been processed again
    if parent_need_id:
        jinja_utils.append_need_to_processed_needs(
            need_id=parent_need_id, art="uml", key=key, kwargs=kwargs
        )

    # 5. Get data for the jinja processing
    data: dict[str, Any] = {}
    # 5.1 Set default config to data
    data.update(**NeedsSphinxConfig(app.config).render_context)
    # 5.2 Set uml() kwargs to data and maybe overwrite default settings
    data.update(kwargs)
    # 5.3 Make the helpers available during rendering and overwrite maybe wrongly default and uml() kwargs settings
    data.update(
        {
            "needs": jinja_utils.needs,
            "need": jinja_utils.need,
            "uml": jinja_utils.uml_from_need,
            "flow": jinja_utils.flow,
            "filter": jinja_utils.filter,
            "import": jinja_utils.imports,
            "ref": jinja_utils.ref_new,
            "sequence3": jinja_utils.class_sequence,
            "context": jinja_utils,
        }
    )

    # 6. Render the uml content with the fetched data
    uml = mem_template.render(**data)

    # 7. Get processed need ids
    processed_need_ids_return = jinja_utils.get_processed_need_ids()

    return (uml, processed_need_ids_return)

# def jinja2uml_new end

import sphinx_needs
sphinx_needs.directives.needuml.jinja2uml = jinja2uml_new

# See https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-render-context
needs_render_context = {
    "needs_types": dict_needs_types,
    "sequence": sequence,
    "sequence2": JinjaFunctions.class_sequence,
    "packages": [
        {"name" : "P1", "elements" : ["C_MANY_A", "C_MANY_B", "C_MANY_C", "C_MANY_D"],},
        {"name" : "P2", "elements" : ["C_MANY_E", "C_MANY_F", "C_MANY_G"],},
        {"name" : "P3", "elements" : ["C_MANY_H", "C_MANY_I", "C_MANY_J", "C_MANY_K", "C_MANY_L"],},
        {"name" : "P4", "elements" : ["C_MANY_M", "C_MANY_N", "C_MANY_O", "C_MANY_P"],},
    ],
}
# needs_render_context end

def my_custom_warning(need, log):
    # some checks
    return False


def my_custom_warning2(need, log, needs):
    # some checks
    return False


my_needs_warnings = {
    'artifact_without_stored_in_link2': "type == 'artifact' and len(stored_in) == 0",
    'my_warning_no_inc_build': my_custom_warning,
    'my_warning_no_inc_build2': my_custom_warning2,
}

# test warnings with needs

"""
Cares about handling and execution warnings.

"""

from sphinx.application import Sphinx
from sphinx.util import logging

from sphinx_needs.config import NeedsSphinxConfig
from sphinx_needs.data import NeedsInfoType, SphinxNeedsData
from sphinx_needs.filter_common import filter_needs
from sphinx_needs.logging import get_logger

logger = get_logger(__name__)


def my_process_warnings(app: Sphinx, exception: Exception | None) -> None:
    """
    Checks the configured warnings.

    This func gets called by the latest sphinx-event, so that really everything is already done.

    :param app: application
    :param exception: raised exceptions
    :return:
    """

    print ("added my process warnings")

    logger.info(
                    f"added my process warnings [needs]",
                    type="needs",
                )

    # We get called also if an exception occured during build
    # In this case the build is already broken and we do not need to check anything.
    if exception:
        return

    env = app.env
    needs = SphinxNeedsData(env).get_needs_view()
    # If no needs were defined, we do not need to do anything
    if not needs:
        return

    # Check if warnings already got executed.
    # Needed because the used event gets executed multiple times, but warnings need to be checked only
    # on first execution
    if hasattr(env, "my_needs_warnings_executed") and env.my_needs_warnings_executed:
        return

    env.my_needs_warnings_executed = True  # type: ignore[attr-defined]

    # Exclude external needs for warnings check
    checked_needs: dict[str, NeedsInfoType] = {}
    for need_id, need in needs.items():
        if not need["is_external"]:
            checked_needs[need_id] = need

    needs_config = NeedsSphinxConfig(app.config)
    warnings_always_warn = needs_config.warnings_always_warn

    with logging.pending_logging():
        logger.info("\nChecking sphinx-needs warnings2")
        warning_raised = False
        for warning_name, warning_filter in my_needs_warnings.items():
            if isinstance(warning_filter, str):
                # filter string used
                result = filter_needs(
                    checked_needs.values(),
                    needs_config,
                    warning_filter,
                    append_warning=f"(from warning filter {warning_name!r})",
                )
            elif callable(warning_filter):
                # custom defined filter code used from conf.py
                result = []
                for need in checked_needs.values():
                    from inspect import signature
                    sig = signature(warning_filter)
                    if 3 <= len(sig.parameters):
                        if warning_filter(need, logger, needs):
                            result.append(need)
                    else:
                        if warning_filter(need, logger):
                            result.append(need)
            else:
                logger.warning(
                    f"Unknown needs warnings filter {warning_filter}! [needs]",
                    type="needs",
                )

            if len(result) == 0:
                logger.info(f"{warning_name}: passed")
            else:
                need_ids = [x["id"] for x in result]

                # Set Sphinx statuscode to 1, only if -W is used with sphinx-build
                # Because Sphinx statuscode got calculated in very early build phase and based on warning_count
                # Sphinx-needs warnings check hasn't happened yet
                # see deatils in https://github.com/sphinx-doc/sphinx/blob/81a4fd973d4cfcb25d01a7b0be62cdb28f82406d/sphinx/application.py#L345
                # To be clear, app.keep_going = -W and --keep-going, and will overrite -W after
                # see details in https://github.com/sphinx-doc/sphinx/blob/4.x/sphinx/application.py#L182
                if app.statuscode == 0 and (app.keep_going or app.warningiserror):
                    app.statuscode = 1

                # get the text for used filter, either from filter string or function name
                if callable(warning_filter):
                    warning_text = warning_filter.__name__
                elif isinstance(warning_filter, str):
                    warning_text = warning_filter

                if warnings_always_warn:
                    logger.warning(
                        "{}: failed\n\t\tfailed needs: {} ({})\n\t\tused filter: {} [needs]".format(
                            warning_name,
                            len(need_ids),
                            ", ".join(need_ids),
                            warning_text,
                        ),
                        type="needs",
                    )
                else:
                    logger.info(
                        "{}: failed\n\t\tfailed needs: {} ({})\n\t\tused filter: {}".format(
                            warning_name,
                            len(need_ids),
                            ", ".join(need_ids),
                            warning_text,
                        )
                    )
                    warning_raised = True

        if warning_raised:
            logger.warning(
                "warnings were raised. See console / log output for details. [needs]",
                type="needs",
            )

