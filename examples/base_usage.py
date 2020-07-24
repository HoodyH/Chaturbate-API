from enum import Enum
from chaturbate_api import ChaturbateSearch, ChatrubateCam, Type, Tag


if __name__ == '__main__':
    MyTag = Enum('MyTag', {'CUSTOM': 'asian/'})

    cams = ChaturbateSearch().search_tag(
        tag=MyTag.CUSTOM,
        gender=Type.FEMALE,
        nr_pages=2
    ).filter_by(
        age=lambda age: True if 18 <= age <= 19 else False,
        # uptime_min=lambda uptime_min: True if 50 <= uptime_min <= 300 else False,
        # spectators=lambda spectators: True if 1 <= spectators <= 20 else False,
    )

    if cams.filtered_results:
        for cam in cams.filtered_results:
            cam: ChatrubateCam
            print(
                cam.gender.name.title(),
                cam.age,
                cam.url,
                'location:"{}" uptime: {} spectators: {}'.format(cam.location, cam.uptime_min, cam.spectators)
            )
    else:
        print('No Results')
