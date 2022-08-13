from dataclasses import dataclass

from typing import AnyStr, List, Tuple, Union

MAX_SIZE = 4098

@dataclass
class BaseHashTable:
    _data = None
    _size: int = 0

    def __init__(self, size: int = MAX_SIZE):
        self._size = size
        self._data = [None] * size
    
    def _get_index(self, key):
        # Hashing
        key = str(key)
        key_sum1 = sum([ord(letter) for letter in key])

        key_sum = 2 * int(key_sum1) + 5

        index = key_sum % self._size

        return index

    def _get_valid_index(self, key):
        orginal_index = index = self._get_index(key)
        is_key_found = False

        while True:

            key_value = self._data[index]

            if key_value is None: # Key does not exists
                #is_valid = True
                return index, is_key_found
            else:
                data_key, _ = key_value
                if data_key == key: # Key is found
                    is_key_found = True
                    return index, is_key_found

            index += 1

            if index == orginal_index:
                index = None
                return index, is_key_found

            if index == self._size:
                index = 0
    
    def insert(self, key: AnyStr, value: AnyStr) -> bool:
        result = False

        index, is_key_found = self._get_valid_index(key)

        if index is not None and is_key_found is False:
            self._data[index] = (key, value)
            result = True
        
        return result, index
    
    def find(self, key: AnyStr) -> Tuple[Union[None, AnyStr], bool]:
        result = None
        index, is_key_found = self._get_valid_index(key)

        if is_key_found is True:
            super_result = self._data[index]

        if super_result is not None:
            result = super_result[1]

        return result, is_key_found

    def update(self, key, value):
        index, is_key_found = self._get_valid_index(key)

        if is_key_found is True:
            self._data[index] = (key, value)
        return is_key_found

    def list_all(self):
        result = []
        for key_value in self._data:
            if key_value is not None:
                key, _ = key_value

            result.append(key)
        return result
