from pathlib import Path

from libboost_headers import get_include


def test_header():
    include_path: Path = get_include()
    assert (include_path / "boost/version.hpp").exists()
