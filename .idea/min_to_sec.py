def minute_to_second1(values):
    #print(1)
    for val in values:
        new_val = val.replace("m", "").replace("s", "")
        print(new_val)
        if new_val.isnumeric():
            new_val = str(int(new_val))
            #print(1)
        if len(new_val) > 2:
            minute = int(new_val[:-2])
            second = int(new_val[-2:])
            print(int(minute*60 + second))
            return int(minute*60 + second)
        else:
            print(new_val)
            return new_val
val1 = ["04m37s","05m30s","37s"]
minute_to_second1(val1)