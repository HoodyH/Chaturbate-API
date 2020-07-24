from enum import Enum


class Type(Enum):
    NONE = '', '', ''
    MALE = 'genderm', 'male-cams/', 'm/'
    FEMALE = 'genderf', 'female-cams/', 'f/'
    COUPLE = 'genderc', 'couple-cams/', 'c/'
    TRANS = 'gendert', 'trans-cams/', 't/'

    @staticmethod
    def gender_by_id(gender_id: str):
        """
        Check if the GenderItem is in Gender
        evaluate by ITEM[1] : [genderm, genderf, genderc, gendert]
        :param gender_id:
        :return:
        """
        items_list = [attr for attr in dir(Type) if not callable(getattr(Type, attr)) and not attr.startswith("__")]
        for attr in items_list:
            if gender_id == getattr(Type, attr).value[0]:
                return getattr(Type, attr)
        return Type.NONE
