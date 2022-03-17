#!/usr/bin/env python
""" Removes Harakat from Arabic Text""" 

import pynini

from pynini.lib import pynutil
from pynini.lib import rewrite

geminates = pynini.union("bb", "cc", "dd", "ff", "gg", "hh", "jj", "kk", "ll", "mm", "nn", "pp", "qq", "rr", "ss", "tt", "yy", "vv", "ww", "zz") #list of Arabizi consonants geminated 
a_consonants = pynini.union( "إ","أ","ئ", "ؤ","ي", "ب" ,"ت", "ث","ج", "ح","خ","د", "ذ","ر", "ز","س", "ش","ص","ض","ط","ظ","ع","غ","ف", "ق","ك","ل", "م","ن", "ه", "و") #list of Arabic consonants
a_long_vowels = pynini.union("ا", "و", "ي")
harakat = pynini.union("َ", "ِ", "ُ", "ْ", "ّ")
e_consonants = pynini.union("D", "T","b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",)
e_vowels = pynini.union("a", "e", "i", "o", "u","è")


SIGMA_STAR = (
    pynini.union(
        "ee",
        "ei",
        "ai",
        "aa",
        "ie"
        "ii",
        "uu",
        "oo",
        "é",
        "th",
        "dj",
        "dh" 
        "kh",
        "gh",
        "ou",
        "uo",
        # number letters.
        "7",
        "3'",
        "2",
        "5",
        "7'",
        "6",
        "9",
        "9'",
        "6'",
        "3'",
        "8",
       
        "ا‎",
        "ء",
        "آ",
        "ئ",
        "إ",
        "ؤ",
        "أ",
        "ى",
       
        "$",
        geminates,
        harakat,
        a_consonants,
        a_long_vowels,
        e_consonants,
        e_vowels

    )
    .closure()
    .optimize()
)

Deletion = (pynini.cdrewrite(pynini.cross(pynini.union("َ", "ِ", "ُ", "ْ", "ّ"), " "), " ", " ", SIGMA_STAR).optimize())

def removal(istring: str) -> str:
    """Deletes diacritics from Arabic text.

    Args:
      istring: The diacriticized text.

    Returns:
      The undiacriticized version of the Arabic text.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, Deletion)

print(removal("حَبِيبِي"))



