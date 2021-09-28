class Singleton(type):
    __instance = None

    def __new__(mcs, *args, **kwargs):
        if not isinstance(mcs.__instance, mcs):
            mcs.__instance = super(Singleton, mcs).__new__
        return mcs.__instance


class Sun:
    @staticmethod
    def inst():
        return Singleton


if __name__ == '__main__':
    x = Sun.inst()
    y = Sun.inst()
    print(x is y)
