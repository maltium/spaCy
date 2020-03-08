# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, TAG, NORM, PRON_LEMMA

_exc = {}

for orth in [
    "a.m.",
    "bros.",
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
    "eċċ.",
    "eż.",
    "vol.",
    "Vol.",
    "p.",
    "2d", "2D",
    "3d", "3D",
    "3g", "3G",
    "4g", "4G",
    "5g", "5G",
    "mp3", "MP3",
    "mp4", "MP4",
    "U2",
    "x86", "x64",
    "TVM2",
    "r&b", "R&B",
    "r&d", "R&D",
    "E.coli"
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = _exc