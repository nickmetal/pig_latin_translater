from abc import ABC, abstractmethod
from enum import Enum
from aiohttp.client import ClientSession

from .errors import UnsupportedDialectError, TranslationTypeNotFoundError


class TranslatorTypeEnum(Enum):
    ENG_TO_PIG_LATIN = "eng_to_pig_latin"


class PigLatinDialectEnum(Enum):
    YAY = "yay"
    WAY = "way"
    AY = "ay"


class AbstractTranslator(ABC):
    def __init__(self, translator_type: TranslatorTypeEnum, dialect: str):
        self.dialect = self.validate_dialect(dialect)
        self.__translator_type = self.validate_translator_type(translator_type)

    def validate_dialect(self, dialect: str) -> Enum:
        try:
            return self.dialect_cls(dialect)
        except ValueError:
            raise UnsupportedDialectError(dialect)

    def validate_translator_type(self, translator_type: Enum) -> TranslatorTypeEnum:
        if not isinstance(translator_type, TranslatorTypeEnum):
            raise TranslationTypeNotFoundError(translator_type)
        return translator_type

    @property
    def dialect_cls(self):
        return self.__dialect_cls__

    @abstractmethod
    async def translate(self, text_to_translate: str) -> str:
        pass


class EnglishToPigLatinTranslator(AbstractTranslator):
    __dialect_cls__ = PigLatinDialectEnum

    def _convert_word(self, word: str, sep: str) -> str:
        VOWELS = "aeiou"

        if word[0] in VOWELS:
            return f"{word}{sep}{self.dialect.value}"

        consonant_cluster = ""
        for letter in word:
            # end of consonant cluster
            if letter in VOWELS:
                break
            # make `y` great(vowel) again
            if consonant_cluster and letter == "y":
                break

            consonant_cluster += letter

        return (
            f"{word[len(consonant_cluster):]}{sep}{consonant_cluster}{self.dialect.value}"
        )

    async def translate(self, text: str, sep: str = "-") -> str:
        """
        Convert text according to Pig Latin rules

        Rules:
            https://www.wikihow.com/Speak-Pig-Latin

        Note:
            `compound words` are not supported

        Args:
        :text: text to translate
        :sep: character to separate translation word

        """
        return " ".join(self._convert_word(word, sep) for word in text.split())


def get_translator(
    translator_type: TranslatorTypeEnum, dialect: str
) -> AbstractTranslator:
    if translator_type == TranslatorTypeEnum.ENG_TO_PIG_LATIN:
        return EnglishToPigLatinTranslator(translator_type, dialect)
    raise TranslationTypeNotFoundError()
