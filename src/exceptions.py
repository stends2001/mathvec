class EmptyExpressionError(Exception):

    def __init__(self, action: str):
        msg = f'ERROR: Action {action} invalid for an empty expression.'
        super().__init__(msg)

class EmtpyExpressionName(Exception):

    def __init__(self):
        msg = f'ERROR: SAVE invalid for an expression with an empty name.'
        super().__init__(msg)