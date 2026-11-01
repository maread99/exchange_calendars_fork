import inspect

import pandas.testing as tm

_SUPPORTS_CHECK_FREQ = (
    "check_freq" in inspect.signature(tm.assert_index_equal).parameters
)


def assert_index_equal(left, right, **kwargs):
    """As `pandas.testing.assert_index_equal`, tolerant of pandas version.

    Drops the `check_freq` kwarg, if passed, on a pandas version that
    predates it, as determined by introspecting the function signature.
    """
    if not _SUPPORTS_CHECK_FREQ:
        kwargs.pop("check_freq", None)
    tm.assert_index_equal(left, right, **kwargs)
