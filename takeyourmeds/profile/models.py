from django_auto_one_to_one import PerUserData

class UserData(PerUserData('profile')):
    pass
