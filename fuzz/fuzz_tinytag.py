# SPDX-FileCopyrightText: 2026 tinytag Contributors
# SPDX-License-Identifier: MIT

# pylint: disable=import-error,missing-function-docstring
# pylint: disable=missing-module-docstring
# pyright: reportAttributeAccessIssue=false,reportMissingModuleSource=false
# pyright: reportUnknownMemberType=false

import io
import sys

import atheris

from tinytag import TinyTag, TinyTagException


def test_one_input(data: bytes) -> None:
    try:
        tag = TinyTag.get(
            file_obj=io.BytesIO(data), tags=True, duration=True, image=True
        )
    except TinyTagException:
        return

    tag.as_dict()


atheris.instrument_all()
atheris.Setup(sys.argv, test_one_input)
atheris.Fuzz()
