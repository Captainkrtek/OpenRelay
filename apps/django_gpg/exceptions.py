class GPGException(Exception):
    pass


class GPGVerificationError(GPGException):
    pass


class GPGSigningError(GPGException):
    pass


class GPGDecryptionError(GPGException):
    pass


class KeyDeleteError(GPGException):
    pass


class KeyGenerationError(GPGException):
    pass
    
    
class KeyFetchingError(GPGException):
    pass
