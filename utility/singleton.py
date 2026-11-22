# Singletons class return only one instance of a class
# Eg:
# my_class_one = SomeSingletonClass()
# my class_two = SomeSingletonClass()

# my_class_one and my_class_two will be considered as the same object automatically

class Singleton(type):
    _instances = {}

    def __call__(class_type, *args, **kwargs):
        if (class_type not in class_type._instances):
            class_type._instances[class_type] = super().__call__(*args, **kwargs)
        return class_type._instances[class_type]

