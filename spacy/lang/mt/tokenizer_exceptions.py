# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, TAG, NORM, PRON_LEMMA

_exc = {}

for orth in [
    "a.m.",
    "bros.",
    "co.",
    "co.",
    "corp.",
    "dr.",
    "e.g.",
    "fr.",
    "i.e.",
    "inc.",
    "jr.",
    "ltd.",
    "mr.",
    "mrs.",
    "ms.",
    "onor."
    "p.m.",
    "ph.d.",
    "rep.",
    "rev.",
    "sen.",
    "st.",
    "vs.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = _exc