# coding: utf8
from __future__ import unicode_literals

from ..punctuation import TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES, TOKENIZER_INFIXES
from ..char_classes import CONCAT_QUOTES, ALPHA_LOWER, ALPHA_UPPER, ALPHA
from ..char_classes import ALPHA


_xemxin = ["ċ", "d", "n", "r", "s", "t", "x", "ż", "z"]
_prep = ["bi", "da", "di", "fi", "ġo", "li", "ma", "mi", "sa", "ta", "bħa"]


_prefixes = (
    TOKENIZER_PREFIXES +
    ["{}-".format(cons) for cons in _xemxin + ["l"]] +  # definite article (dropped vowel)
    ["i{}-".format(cons) for cons in _xemxin + ["l"]] +  # definite article
    ["għa{}-".format(cons) for cons in _xemxin + ["l"]] +
    ["b'", "f'", "m'", "s'", "t'", "x'"] +
    ["{prep}{cons}-".format(
        prep=prep, cons=cons
    ) for prep in _prep for cons in _xemxin + ["l"]] +
    ["ta'", "ma'"] +
    ["fl-", "bl-"] +
    ["bħall-", "għall-", "lill-", "mill-"] +
    ["ħad-", "ħaż-", "san-"]
)

_suffixes = (
    TOKENIZER_SUFFIXES +
    [r"[{a}]+a'".format(a=ALPHA)] +
    ["-il"]
)

_infixes = (
    TOKENIZER_INFIXES +
    [r"[()]"]
)

TOKENIZER_PREFIXES = _prefixes
TOKENIZER_SUFFIXES = _suffixes
TOKENIZER_INFIXES = _infixes
