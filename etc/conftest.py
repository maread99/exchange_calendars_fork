import pytest


@pytest.fixture(autouse=True)
def _pytest_benchmark_nodeid_compat(request):
    """Shim for pytest-benchmark<=5.3.0 reading the private ``_nodeid``.

    pytest>=9.2 no longer sets the private ``Function._nodeid`` attribute
    that ``pytest-benchmark``'s ``benchmark`` fixture reads directly (fixed
    upstream in pytest-benchmark 5.3.1, not yet resolvable here due to the
    project's `exclude-newer` lock policy). Set it from the public
    ``nodeid`` so the ``benchmark`` fixture keeps working meanwhile.
    """
    node = request.node
    if not hasattr(node, "_nodeid"):
        node._nodeid = node.nodeid  # noqa: SLF001
