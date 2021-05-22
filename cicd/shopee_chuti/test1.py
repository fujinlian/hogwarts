

def splitArr(L):
    result = list()
    set_begin = True
    start = 0
    if L:
        for i in range(len(L)):
            if set_begin:
                start = i
                set_begin = False
            if i != len(L) - 1:
                if L[i + 1] - L[i] == 1:
                    continue
                else:
                    # result.append(L[start:i + 1])
                    result.append([L[start],L[i]])
                    set_begin = True
            else:
                # result.append(L[start:])
                result.append([L[start],L[-1]])
    print(result)
    return result
if __name__ == "__main__":
    nums = [9,8]
    splitArr(nums)

