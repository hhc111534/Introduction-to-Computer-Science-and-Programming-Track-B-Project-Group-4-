MAX_EDGE_LEN=60


def is_edge(b,h):
    y0=b[1]
    y1=b[3]

    if y0<h*0.08:
        return True

    if y1>h*0.92:
        return True

    return False


def is_short(b):
    s=b[4].strip()

    if len(s)<=MAX_EDGE_LEN:
        return True

    return False


def clean_blocks(blks,h):
    out=[]

    for b in blks:
        if is_edge(b,h)==True and is_short(b)==True:
            continue
        out.append(b)

    return out


def fix_hyphen(s):
    return s.replace("-\n","")


def norm_space(s):
    tmp=[]

    for c in s:
        if c=="\n":
            tmp.append(" ")
        elif c=="\t":
            tmp.append(" ")
        elif c=="\u3000":
            tmp.append(" ")
        elif c=="\xa0":
            tmp.append(" ")
        elif c=="\u200b":
            continue
        else:
            tmp.append(c)

    out="".join(tmp)

    while "  " in out:
        out=out.replace("  "," ")

    return out.strip()


def clean_text(s):
    s=fix_hyphen(s)
    s=norm_space(s)
    return s