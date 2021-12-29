import json
import sys


def itarate(_tests, _values):
    for k in _tests:
        test_id = k['id']
        # test_value = ""
        try:
            for s in _values:
                if s['id'] == test_id:
                    test_value = s['value']
                    k['value'] = test_value
        except:
            pass
          
        try:
            itarate(k['values'], _values)
        except:
            pass


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        a = file.read()
        aa = json.loads(a)
        file.close()
    with open(sys.argv[2]) as file:
        b = file.read()
        bb = json.loads(b)
        file.close()

    tests = aa['tests']
    values = bb['values']

    itarate(tests, values)

    with open("report.json", 'w') as file:
        json.dump(aa, file)
