import base64


from typing import Union

from dataclasses import dataclass


@dataclass
class Data:
    extra_data: str = "{\"face_rects\":[],\"version\":2,\"platform\":\"web\",\"data_report\":{" \
                      "\"parent_trace_id\":\"4c689320-71ba-1909-ab57-13c0804d4cc6\",\"root_channel\":\"\",\"level\":0}}"

    url: str = "https://ai.tu.qq.com/overseas/trpc.shadow_cv.ai_processor_cgi.AIProcessorCgi/Process"

    hash_url: str = "https://h5.tu.qq.com{}HQ31X02e"

    
def image_to_base64(image: Union[str, bytes]):
    """
    convert image content to base64
    :param image:
    :type image:
    :return:
    :rtype:
    """
    # if image is path
    if isinstance(image, str):
        with open(image, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')

    # if image is IO object
    if isinstance(image, bytes):
        return base64.b64encode(image).decode('utf-8')



