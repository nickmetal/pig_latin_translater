class TranslationTypeNotFoundError(Exception):
    code = 400


class DataApiResponseError(Exception):
    code = 500
