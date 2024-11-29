# Configuration file for the Sphinx documentation builder.

import os
import sys

from sphinx import __version__ as sphinx_version
print ('sphinx version: ' + str(sphinx_version))

from sphinx_needs import __version__ as sphinx_needs_version
print ('sphinx-needs version: ' + str(sphinx_needs_version))

from sphinx_needs.api import add_dynamic_function

sys.path.append(os.path.abspath('.'))
import metamodel

sys.path.append(os.path.abspath('scripts'))

from gitlink import get_edit_url_from_folder, extent_url_with_file, get_githoster_edit_url_for_need

# For autodoc


# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'HowTo-Sphinx'
copyright = f'2023 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '1.0'
version = '1.0.0'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.test_reports',
    'sphinxcontrib.collections',
    'sphinxcontrib.jquery', # https://github.com/sphinx-contrib/jquery
    'sphinx_preview',
    #'sphinx_immaterial',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# to use numref see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig
numfig = True

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Sphinx-Preview

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case "div-mo-content" is the content area
    # and we handle all links there.
    #"selector": "div.md-content a",
    "selector": "div.main a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button",
    #"not_selector": "div.needs_head a, h1 a, h2 a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔎",
    #"icon": "icon:search",
    "width": 600,
    "height": 400,
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
#html_theme = 'sphinx_immaterial'

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- get edit url for git hoster
print('edit url to git hoster:')
import pathlib
current_folder = pathlib.Path().resolve()
git_hoster_edit_url = get_edit_url_from_folder(current_folder, with_docu_part = True, docu_part_default = 'docs')
print('git hoster edit url: ' + git_hoster_edit_url)

# sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

print('plantuml path: ' + str(plantuml))

plantuml_output_format = 'svg'

# sphinx_needs configuration

needs_role_need_max_title_length = -1

needs_build_json = True

needs_id_regex = metamodel.needs_id_regex

needs_types = metamodel.needs_types

needs_extra_options = metamodel.needs_extra_options

needs_extra_links = metamodel.needs_extra_links

needs_services = metamodel.needs_services

needs_layouts = metamodel.needs_layouts

needs_global_options = metamodel.needs_global_options

needs_render_context = metamodel.needs_render_context

needs_warnings = metamodel.needs_warnings

needs_string_links = metamodel.needs_string_links

needs_external_needs = metamodel.needs_external_needs

needs_diagram_template = metamodel.needs_diagram_template

suppress_warnings = ["config.cache"]

needs_render_context = metamodel.needs_render_context

needs_default_layout = 'clean_with_edit_link'

# -- custom extensions ---------------------------------------

from docutils import nodes  # noqa: E402
from sphinx.application import Sphinx  # noqa: E402
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.errors import ExtensionError


class NeedExampleDirective(SphinxDirective):
    """Directive to add example content to the documentation.

    It adds a container with a title, a code block, and a parsed content block.
    """

    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        count = self.env.temp_data.setdefault("needs-example-count", 0)
        count += 1
        self.env.temp_data["needs-example-count"] = count
        root = nodes.container(classes=["needs-example"])
        self.set_source_info(root)
        title = f"Example {count}"
        title_nodes, _ = (
            self.state.inline_text(f"{title}: {self.arguments[0]}", self.lineno)
            if self.arguments
            else ([nodes.Text(title)], [])
        )
        root += nodes.rubric("", "", *title_nodes)
        code = nodes.literal_block(
            "", "\n".join(self.content), language="rst", classes=["needs-example-raw"]
        )
        root += code
        parsed = nodes.container(classes=["needs-example-raw"])
        root += parsed
        self.state.nested_parse(self.content, self.content_offset, parsed)
        return [root]

from docutils.nodes import Node
from sphinx import version_info
from sphinx.util import logging
from sphinx.util.logging import SphinxLoggerAdapter


def get_logger(name: str) -> SphinxLoggerAdapter:
    return logging.getLogger(name)


def log_warning(
    logger: SphinxLoggerAdapter,
    message: str,
    subtype: str | None,
    /,
    location: str | tuple[str | None, int | None] | Node | None,
    *,
    color: str | None = None,
    once: bool = False,
) -> None:
    # Since sphinx in v7.3, sphinx will show warning types if `show_warning_types=True` is set,
    # and in v8.0 this was made the default.
    if version_info < (8,):
        if subtype:
            message += f" [needs.{subtype}]"
        else:
            message += " [needs]"

    logger.warning(
        message,
        type="needs",
        subtype=subtype,
        location=location,
        color=color,
        once=once,
    )

def get_mylogger(name: str) -> logging.LoggerAdapter:
    return logging.getLogger(name)

def log_error(
    logger: logging.LoggerAdapter,
    message: str,
    subtype: str | None,
    /,
    location: str | tuple[str | None, int | None] | Node | None,
    *,
    color: str | None = None,
    once: bool = False,
) -> None:
    # Since sphinx in v7.3, sphinx will show warning types if `show_warning_types=True` is set,
    # and in v8.0 this was made the default.
    if version_info < (8,):
        if subtype:
            message += f" [needs.{subtype}]"
        else:
            message += " [needs]"

    logger.error(
        message,
        type="needs",
        subtype=subtype,
        location=location,
        color=color,
        once=once,
    )

logger = get_logger(__name__)
mylogger = get_mylogger(__name__)

class HelloRole(SphinxRole):
    """A role to say hello!"""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.inline(text=f'Hello {self.text}!' + str(self.get_source_info()))
        if self.text == "Woorld2":
            #raise ExtensionError('my random error')
            log_warning(
                    logger,
                    f"my random error",
                    "hello",
                    location=self.get_source_info(),
                    color="red",
                )
            log_error(
                    mylogger,
                    f"my random error",
                    "hello",
                    location=self.get_source_info(),
                    color="red",
                )
        return [node], []

from sphinx.directives.code import CodeBlock
from docutils.parsers.rst import directives

class Code2Option(CodeBlock):

    has_content = CodeBlock.has_content
    required_arguments = CodeBlock.required_arguments
    optional_arguments = CodeBlock.optional_arguments
    final_argument_whitespace = CodeBlock.final_argument_whitespace
    option_spec = CodeBlock.option_spec
    option_spec['option2'] = directives.unchanged


    def run(self):
#        language = "rst"
#        code = nodes.literal_block(
#            "", "\n".join(self.content), language=language, classes=["code"]
#        )
#        self.set_source_info(code)
#        return [code]
        super_run = super().run()

        print(self.option2)

        return super_run



def setup(app):
    app.add_config_value(name = 'gitlink_edit_url_to_git_hoster', default = git_hoster_edit_url, rebuild = '', types = [str])

    app.add_directive("example", NeedExampleDirective)
    app.add_role('hello', HelloRole())

    add_dynamic_function(app, get_githoster_edit_url_for_need)

    for func in metamodel.needs_functions:
        add_dynamic_function(app, func)

    app.connect("build-finished", metamodel.my_process_warnings)

