class NoTextLayerError(ValueError):
    pass


MIN_AVG_CHARS=30


def page_chars(d):
    out=[]

    for pno in range(d.page_count):
        p=d[pno]
        s=p.get_text()
        out.append(len(s.strip()))

    return out


def avg_chars(chars):
    if len(chars)==0:
        return 0

    total=0
    for n in chars:
        total=total+n

    return total/len(chars)


def text_report(d):
    chars=page_chars(d)

    total=0
    for n in chars:
        total=total+n

    empty=0
    for n in chars:
        if n==0:
            empty=empty+1

    return {
        "page_count": len(chars),
        "total_chars": total,
        "avg_chars": avg_chars(chars),
        "empty_pages": empty,
        "page_chars": chars,
    }


def check_text_layer(d):
    rep=text_report(d)

    if rep["total_chars"]==0:
        raise NoTextLayerError("这份 PDF 没有文字层，看起来是扫描件。请换一份可以直接复制文字的 PDF。")

    if rep["avg_chars"]<MIN_AVG_CHARS:
        a=round(rep["avg_chars"],1)
        raise NoTextLayerError("这份 PDF 平均每页只有 "+str(a)+" 个字符，大部分页面可能是扫描页。请换一份可以直接复制文字的 PDF。")

    return rep