from abc import ABC, abstractmethod
from enum import Enum
from aiohttp.client import ClientSession

from .errors import DataApiResponseError, TranslationTypeNotFoundError


class TranslatorTypeEnum(Enum):
    ENG_TO_PIG_LATING = "eng_to_pig_latin"


class AbstractTranslator(ABC):
    def __init__(self, translator_type: TranslatorTypeEnum):
        self.__translator_type = translator_type

    @abstractmethod
    async def translate(self, text_to_translate: str) -> str:
        pass


class EnglishToPigLatinTranslator(AbstractTranslator):
    async def translate(self, text_to_translate: str) -> str:
        # data api: https://funtranslations.com/api/piglatin
        api_url = "https://api.funtranslations.com/translate/piglatin"
        body = {"text": text_to_translate}

        async with ClientSession() as session:
            async with session.post(api_url, json=body) as resp:
                response_data = await resp.json()
                if resp.status == 200 and response_data.get("success"):
                    return response_data["contents"]["translated"].strip()
                raise DataApiResponseError(str(response_data))


def get_translator(translator_type: TranslatorTypeEnum) -> AbstractTranslator:
    if translator_type == TranslatorTypeEnum.ENG_TO_PIG_LATING:
        return EnglishToPigLatinTranslator(translator_type)
    raise TranslationTypeNotFoundError()
