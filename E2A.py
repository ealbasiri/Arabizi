"""Arabizi conversion rules."""

import pynini

from pynini.lib import pynutil
from pynini.lib import rewrite

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
        # arabic alphabet
        "ا‎",
        "ء",
        "آ",
        "ئ",
        "إ",
        "ؤ",
        "أ",
        "ى",
        # dollar signs etc 
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
# ta marbuta and haa 
# shams and qamar rules  

geminates = pynini.union("bb", "cc", "dd", "ff", "gg", "hh", "jj", "kk", "ll", "mm", "nn", "pp", "qq", "rr", "ss", "tt", "yy", "vv", "ww", "zz") #list of Arabizi consonants geminated 
a_consonants = pynini.union( "إ","أ","ئ", "ؤ","ي", "ب" ,"ت", "ث","ج", "ح","خ","د", "ذ","ر", "ز","س", "ش","ص","ض","ط","ظ","ع","غ","ف", "ق","ك","ل", "م","ن", "ه", "و") #list of Arabic consonants
a_long_vowels = pynini.union("ا", "و", "ي")
harakat= pynini.union("َ", "ِ", "ُ", "ْ", "ّ")
e_consonants = pynini.union("D", "T","b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",)
e_vowels = pynini.union("a", "e", "i", "o", "u","è")
E2A = (
    #Rule 1: Shadda
    @ pynini.cdrewrite(pynini.concat(""), geminates , "", SIGMA_STAR) #ADD SHADDA SYMBOL
    
    #Rule 2: Consonants: 
    @ pynini.cdrewrite(pynini.cross("2", "ؤ"), pynini.union("o", "u"), " ", SIGMA_STAR) 
    @ pynini.cdrewrite(pynini.cross("2", "ئ" ), pynini.union("y", "e", "i"), " ", SIGMA_STAR) 
    @ pynini.cdrewrite(pynini.cross("2", "أ" ), "a", " ", SIGMA_STAR) #middle of the word
    @ pynini.cdrewrite(pynini.cross(pynini.union("a", "o", "u"), "أ" ), "[BOS]", " ", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("e", "i"), "إ" ), "[BOS]", " ", SIGMA_STAR) 
    @ pynini.cdrewrite(pynini.cross(pynini.union("b", "p", "bb", "pp"), "ب"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("t", "tt"), "ت"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("th", "ث"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("j", "dj", "jj"), "ج"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("7", "ح"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("kh", "7'", "5"), "خ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("d", "dd"), "د"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("th", "dh"), "ذ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("r", "rr" ),"ر"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("z", "zz"), "ز"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("s", "ss"), "س"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("sh", "ch", "$"), "ش"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("9", "ص"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("dh", "9'", "D"), "ض‎"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("6", "T"), "ط"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("dh", "6'"), "ظ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("3", "ع"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("gh", "3'", "8"), "غ‎"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("f", "v", "ff", "vv"), "ف"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("g", "gg", "8", "9"), "ق"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("k", "q", "qq", "kk"), "ك"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("l", "ll"), "ل"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("m", "mm"), "م"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("n", "nn"), "ن"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("h", "hh"), "ه"), "", "", SIGMA_STAR) 
    @ pynini.cdrewrite(pynini.cross(pynini.union("w","ww"), "و"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("y", "yy"), "ي"), "", "", SIGMA_STAR)

    #Rule 3: Sukoon
    @ pynini.cdrewrite(pynini.concat("ْ"), a_consonants , a_consonants, SIGMA_STAR)

    #Rule(s) 4: Long Vowels
    @ pynini.cdrewrite(pynini.cross("aa", "ا"), "" , "", SIGMA_STAR)   
    @ pynini.cdrewrite(pynini.cross(pynini.union("ee", "ii", "ei", "ie"), "ي"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross(pynini.union("oo", "uu", "ou", "uo"), "و"), "", "", SIGMA_STAR) 


    #Rule(s) 5: Short Vowels 
    @ pynini.cdrewrite(pynini.cross(pynini.union("a", "e", "è"), "َ"), a_consonants, "", SIGMA_STAR) #FATHA
    @ pynini.cdrewrite(pynini.cross(pynini.union("i", "e"), "ِ"), a_consonants, "", SIGMA_STAR) #KASRA
    @ pynini.cdrewrite(pynini.cross(pynini.union("u", "o"), "ُ"), a_consonants, "", SIGMA_STAR) #DAMMA
  


).optimize()


def e2a(istring: str) -> str:
    """Applies the Arabizi to Arabic letters rule.

    Args:
      istring: the Arabizi input string.

    Returns:
      The Arabic letters output string.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, E2A)

assert rewrite.one_top_rewrite("raa7", E2A) == "رَاح"
assert rewrite.one_top_rewrite("ma7lek", E2A) == "مَحْلِك"
assert rewrite.one_top_rewrite("Enas", E2A) == "إنَس"
assert rewrite.one_top_rewrite("m7ammarah", E2A) == "مْحَمّرَه"
