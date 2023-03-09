from typing import Dict, List
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH
from ...util import update_exc

_exc: Dict[str, List[Dict]] = {}

for orth in [
    "'d",
    "a.m.",
    "adm.",
    "bros.",
    "co.",
    "corp.",
    "d.c.",
    "dr.",
    "e.g.",
    "gen.",
    "gov.",
    "i.e.",
    "inc.",
    "jr.",
    "ltd.",
    "md.",
    "messrs.",
    "mo.",
    "mont.",
    "mr.",
    "mrs.",
    "ms.",
    "p.m.",
    "ph.d.",
    "prof.",
    "rep.",
    "rev.",
    "sen.",
    "st.",
    "vs.",
    "v.s.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)