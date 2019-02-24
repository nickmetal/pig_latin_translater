class BaseTranslationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        _args_message = " ".join(args).strip()
        _kwargs_message = str(kwargs or "").strip()

        self.error_text = f"{self.text}: {_args_message} {_kwargs_message}".strip()
        self.args = (self.code, self.error_text)


class TranslationTypeNotFoundError(BaseTranslationError):
    code = 400
    text = "translation type not found"


class UnsupportedDialectError(BaseTranslationError):
    code = 400
    text = "dialect is not supported"
