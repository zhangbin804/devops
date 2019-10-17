from random import choice

def random_str(types="type1",randomlength=16):
    ret = ''
    chars = {
        "type1":"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789",
        "type2":"0123456789",
        "type3":"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
        "type4":"ABCDEFGHIJKLMNOPQRSTUVWZXY",
        "type5":"abcdefghijklmnopqrstuvwxyz",
        "type6":r"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRtrSsTtUuVvWwXxYyZz0123456789-=+\;|&*#@",
                     }
    for i in range(randomlength):
        ret+=choice(list(chars[types]))
    return ret

