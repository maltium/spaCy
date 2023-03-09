from ...language import Language
from ..tokenizer_exceptions import BASE_EXCEPTIONS

from .punctuation import TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES, TOKENIZER_INFIXES
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS

from ...util import update_exc
from ...attrs import LANG


def _return_mt(_):
    return "mt"


class MalteseDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = _return_mt

    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)

    prefixes = TOKENIZER_PREFIXES
    suffixes = TOKENIZER_SUFFIXES
    infixes = TOKENIZER_INFIXES


class Maltese(Language):
    lang = "mt"
    Defaults = MalteseDefaults


__all__ = ["Maltese"]
