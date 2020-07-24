from enum import Enum


class Tag(Enum):
    PETITE = 'petite'
    TEEN = 'teen'
    CUTE = 'cute'
    SHY = 'shy'
    ASIAN = 'asian'

    @staticmethod
    def tag_url(tag):
        return 'tag/{}/'.format(tag)
