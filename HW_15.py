import json


class MyClass:
    def __init__(self, src_path='HW.json', dest_path='HW_result.json'):
        self.__src_path = src_path
        self.__dest_path = dest_path
        self.__data = {}
    def load(self):
        with open(self.__src_path, 'r') as json_file:
            self.__data = json.load(json_file)
    def dump(self):
        with open(self.__dest_path, 'w') as json_file:
            json.dump(self.__data, json_file, indent=4)
    def __str__(self):
        return json.dumps(self.__data, indent=4)
    def __repr__(self):
        return self.__str__()

    def create_task(self):
        result = {}
        data = self.__data
        for key, lst in data.items():
            dict_intitial = {}
            for el in lst:
                firstName = el.get('firstName')
                lastName = el.get('lastName')
                fullName = '{} {}'.format(firstName, lastName)
                d_types = {
                    'int': 'int',
                    'str': 'string',
                    'float': 'float',
                    'NoneType': 'none_type',
                    'bool': 'bool'
                }
                d_res = dict.fromkeys(d_types.values(), [])
                lst_tpl = [(tpl[0], tpl[1].__class__.__name__) for tpl in el.items()]
                for tpl in lst_tpl:
                    value, typeValye = tpl
                    custom_value = d_types.get(typeValye)
                    d_res[custom_value] = d_res.get(custom_value, []) + [value]
                dict_intitial[fullName] = d_res
            result[key] = dict_intitial
        self.__data = result


def main():
    obj = MyClass()
    obj.load()
    print(obj)
    obj.create_task()
    print(obj)
    obj.dump()


if __name__ == '__main__':
    main()
