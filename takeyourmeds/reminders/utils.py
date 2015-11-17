from django.utils.crypto import get_random_string

def get_ident_default():
     return get_random_string(40)
