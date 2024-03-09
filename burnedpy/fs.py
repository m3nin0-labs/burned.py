#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Filesystem utilities."""


import csv
import os
from pathlib import Path
from typing import Generator, Union


def fs_get_user_cache_dir(app_name: str) -> Path:
    """Get the user-specific application cache directory.

    This function finds the user-specific application
    cache directory. Typically, the user cache directories
    are:
        MacOS:   ~/Library/Caches/<AppName>
        Unix:    ~/.cache/<AppName> (XDG default)
        Windows: C:\\Users\\<username>\\AppData\\Local\<AppName>\\Cache

    Args:
        app_name (str): Application name.

    Returns:
        Path: Path to the application cache directory.

    Note:
        This function was adapted from the ``python-poetry`` source code. Currently,
        we only support the Linux implementation.

    See:
        See the original implementation of this function in the ``python-poetry``
        repository: <https://github.com/python-poetry/poetry/blob/f6022eade7485a3b017ef0c8060dffed12e3cdb2/src/poetry/utils/appdirs.py#L32>
    """
    return Path(
        os.path.join(
            os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share")), app_name
        )
    )


def fs_read_csv(file: Union[str, Path]) -> Generator:
    """Read CSV file.

    Args:
        file (Union[str, Path]): Path to file.
    """
    file = Path(file)

    with file.open("r") as ifile:
        yield from csv.DictReader(ifile)
