sum_int, sum_dict, sum_str = 0, 0, 0

def count_(m):
    global sum_int, sum_dict, sum_str

    for i in m:
        if isinstance(i, tuple):
            def tuple_(m):
                s = 0
                for k in m:
                    s += 1
                if s == 1:
                    for_(k)
                else:
                    count_(m)
            tuple_(i)

        if isinstance(i, int):
            sum_int += i
            print(i, type(i), i)
            continue

        if isinstance(i, str):
            sum_str += len(i)
            print(i , type(i),len(i))
            continue

        if isinstance(i, list):
            def list_(m):
                s = 0
                for k in m:
                    s += 1
                if s == 1:
                    list_(k)
                else:
                    count_(m)
            list_(i)
            continue

        if isinstance(i, dict):
            keys_len = len("".join(list(i)))
            value_sum=sum(i.values())
            dict_sum =keys_len+value_sum
            print(i,type(i),dict_sum)
            sum_dict += dict_sum
            continue
    return sum_int+sum_dict+sum_str

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
  ]

result = count_(data_structure)
print(f'\nИтоговая сумма = {result}')

















