import inflect

def convert_denominator(n_s, n, d):
    table = dict( {
        2:"half",
        3:"third",
        4:"quarter",
        5:"fifth",
        6:"sixth",
        7:"seventh",
        8:"eighth",
        9:"ninth",
        10:"tenth",
        11:"eleventh",
        12:"twelth",
        13:"thirteenth",
        14:"fourteenth",
        15:"fifteenth",
        16:"sixteenth",
        17:"seventeenth",
        18:"eighteenth",
        19:"nineteenth",
        20:"twetieth"
    })
    e = inflect.engine()
    ret = n_s
    if int(d) == 1:
        return ret
    else:
        d_s = e.plural(table[int(d)], n)
        ret = f'{ret} {d_s}'
        return ret