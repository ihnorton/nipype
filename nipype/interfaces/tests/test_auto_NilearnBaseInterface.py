# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..nilearn import NilearnBaseInterface


def test_NilearnBaseInterface_inputs():
    input_map = dict()
    inputs = NilearnBaseInterface.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
