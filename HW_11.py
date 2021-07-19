import json

fpath = 'HW.json'
fpath_res = 'HW_result_task_done.json'
data = {}
result = {}
with open(fpath, 'r') as json_file:
    data = json.load(json_file)


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

    with open(fpath_res, 'w') as file:
        json.dump(result, file, indent=2)
