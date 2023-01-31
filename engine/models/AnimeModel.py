from dataclasses import dataclass, field

from enum import Enum

import json


class ErrorCodes(Enum):
    SUCCESS = 0
    NUDITY = 2114
    NO_FACE = 1001
    AUTH_FAILED = -2111
    USER_IP_COUNTRY = 2119
    PARAM_INVALID = -2100
    CONNECTION_CLOSED = 141


@dataclass
class AnimeModel:
    """
    serializing class for response
    """
    code: int
    msg: str
    images: list = ""
    faces: list = ""
    extra: list[str] = field(default_factory=list)
    videos: list = ""

    def __post_init__(self):

        match ErrorCodes(self.code):
            case ErrorCodes.AUTH_FAILED:
                pass
            case ErrorCodes.NUDITY:
                pass
            case ErrorCodes.NO_FACE:
                pass
            case ErrorCodes.USER_IP_COUNTRY:
                pass
            case ErrorCodes.PARAM_INVALID:
                pass
            case ErrorCodes.CONNECTION_CLOSED:
                pass
            case ErrorCodes.SUCCESS:
                self.extra = json.loads(self.extra)["img_urls"]

