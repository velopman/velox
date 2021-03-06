from token import Token


class RuntimeError(Exception):
    # Lifecycle methods

    def __init__(
        self,
        token: Token,
        message: str,
    ) -> None:
        super().__init__(message)

        self.token = token
        self.message = message
