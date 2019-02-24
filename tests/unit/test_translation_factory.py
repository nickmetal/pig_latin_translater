import pytest

from translator_app.core.errors import TranslationTypeNotFoundError
from translator_app.core.translator import (
    get_translator,
    TranslatorTypeEnum,
    PigLatinDialectEnum,
    EnglishToPigLatinTranslator,
)


def test_valid_type_for_eng_to_pig_latin_translator():
    translator_type = TranslatorTypeEnum("eng_to_pig_latin")
    translator = get_translator(translator_type, PigLatinDialectEnum.AY.value)
    assert isinstance(translator, EnglishToPigLatinTranslator)


def test_invalid_type_for_eng_to_pig_latin_translator():
    with pytest.raises(
        TranslationTypeNotFoundError, match=TranslationTypeNotFoundError.text
    ):
        get_translator("invalid TranslatorTypeEnum value", PigLatinDialectEnum.AY.value)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_text, expected_text",
    [
        ("welcome", "elcome-way"),
        ("yellow", "ellow-yay"),
        ("Hello", "ello-hay"),
        ("duck", "uck-day"),
        ("ultimate", "ultimate-ay"),
        ("Rhythm", "ythm-rhay"),
        ("another one", "another-ay one-ay"),
    ],
)
async def test_valid_eng_to_pig_latin_translation_ay(input_text, expected_text):
    translator_type = TranslatorTypeEnum("eng_to_pig_latin")
    translator = get_translator(translator_type, PigLatinDialectEnum.AY.value)

    actual_result = await translator.translate(input_text)
    assert actual_result.lower() == expected_text.lower()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_text, expected_text",
    [("welcome", "elcome-wway"), ("yellow", "ellow-yway"), ("Hello", "ello-hway")],
)
async def test_valid_eng_to_pig_latin_translation_way(input_text, expected_text):
    translator_type = TranslatorTypeEnum("eng_to_pig_latin")
    translator = get_translator(translator_type, PigLatinDialectEnum.WAY.value)

    actual_result = await translator.translate(input_text)
    assert actual_result.lower() == expected_text.lower()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_text, expected_text",
    [("welcome", "elcome-wyay"), ("yellow", "ellow-yyay"), ("Hello", "ello-hyay")],
)
async def test_valid_eng_to_pig_latin_translation_yay(input_text, expected_text):
    translator_type = TranslatorTypeEnum("eng_to_pig_latin")
    translator = get_translator(translator_type, PigLatinDialectEnum.YAY.value)

    actual_result = await translator.translate(input_text)
    assert actual_result.lower() == expected_text.lower()
