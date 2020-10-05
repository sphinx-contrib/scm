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
    app.add_config_value("scm_contribs_email", "true", "env")
    app.add_config_value("scm_contribs_limit_authors", None, "env")
    app.add_config_value("scm_contribs_min_commits", 0, "env")
    app.add_config_value("scm_contribs_sort", "name", "env")
    app.add_config_value("scm_contribs_type", "author", "env")
    app.add_directive("scm-sectionauthor", ContribsDirective)
    app.add_role("scm-contribs", ContribsRole())
    return {"version": ".".join(__version__.split(".")[:3])}
