def split_list(obj_list: list):
    list_len = len(obj_list)
    tem = [int(o) for o in obj_list]
    z = int(list_len / 2)
    if list_len > 4:
        return [[tem[0], tem[z - 1]], tem[z:z + 2], [tem[z + 2], tem[-1]]]
    else:
        return [[tem[0]], tem[z:z + 1], [tem[-1]]]


obj = input()

z = str(obj).split(',')
print(split_list(z))
