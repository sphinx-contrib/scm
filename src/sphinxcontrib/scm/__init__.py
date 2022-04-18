from __future__ import annotations

from typing import Any

import sphinx.util
from sphinx.application import Sphinx

from .directives import ContribsDirective
from .roles import ContribsRole

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("sphinxcontrib-scm")
except metadata.PackageNotFoundError:
    pass

logger = sphinx.util.logging.getLogger(__name__)


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value(name="scm_contribs_email", default="true", rebuild="env")
    app.add_config_value(name="scm_contribs_limit_authors", default=None, rebuild="env")
    app.add_config_value(name="scm_contribs_min_commits", default=0, rebuild="env")
    app.add_config_value(name="scm_contribs_sort", default="name", rebuild="env")
    app.add_config_value(name="scm_contribs_type", default="author", rebuild="env")
    app.add_directive(name="scm-sectionauthor", cls=ContribsDirective)
    app.add_role(name="scm-contribs", role=ContribsRole())
    return {"version": ".".join(__version__.split(".")[:3])}
