import dataclasses
import hashlib
import json
from typing import Union

import aiohttp

from engine.models import AnimeModel
from engine.utils import helper, Data

@dataclasses.dataclass
class AnimeProcess:
    images: list[str]
    busiId: str = "different_dimension_me_img_entry"
    extra: str = "{\"face_rects\":[],\"version\":2,\"platform\":\"web\",\"data_report\":{\"parent_trace_id\":\"4c689320-71ba-1909-ab57-13c0804d4cc6\",\"root_channel\":\"\",\"level\":0}}"

    @staticmethod
    async def get_anime_data(init_image: Union[str, bytes]):
        """
        get answer and serializing it to AnimeModel
        :param init_image:
        :type init_image:
        :return:
        :rtype:
        """
        base64_image = helper.image_to_base64(image=init_image)
        post_data = AnimeProcess(images=[base64_image])
        post_str_data = json.dumps(post_data.__dict__)

        url = Data.hash_url.format(str(len(post_str_data))).encode()
        sign_value = hashlib.md5(url).hexdigest()

        headers = {
            'Host': 'ai.tu.qq.com',
            "x-sign-value": sign_value,
            "x-sign-version": "v1",
            'Origin': 'https://h5.tu.qq.com'
        }

        async with aiohttp.ClientSession() as session:

            req = await session.post(
                url=Data.url,
                headers=headers,
                json=post_data.__dict__
            )

            json_response = await req.json()

            anime = AnimeModel(**json_response)

        return anime


