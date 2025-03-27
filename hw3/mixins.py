import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class FileWriteMixin:
    def write(self, file_path):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(str(self.data) + '\n\n')

class StrMixin:
    def __str__(self):
        return f'{self.data}'
    
class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['_data']

    def __set__(self, instance, value):
        instance.__dict__['_data'] = value
    
class DescriptorMixin:
    data = Descriptor()

class ArrayWrapper(NDArrayOperatorsMixin, StrMixin, FileWriteMixin, DescriptorMixin):
    def __init__(self, data):
        self._data = np.array(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):

        args = [x.data if isinstance(x, ArrayWrapper) else x for x in inputs]
        result = getattr(ufunc, method)(*args, **kwargs)

        if isinstance(result, np.ndarray):
            return ArrayWrapper(result)
        return result
    