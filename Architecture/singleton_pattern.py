
class MetaEncrypter(type):

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        """ Overidding the __call__ magic method"""
        if not cls._instance:
            print(cls, "creating instance ", args, kwargs)
        return cls._instance



class Encrypter(object):
    """ Encrypter class that shows the singleton pattern"""
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = object.__new__(cls)

        return cls._instance
