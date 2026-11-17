import hashlib
import os

import pymupdf

from paperlens.common.models import Document, Page, Paragraph
from paperlens.pdf.cleaner import clean_blocks, clean_text
from paperlens.pdf.quality import check_text_layer


def file_sha(path):
    h=hashlib.sha256()
    f=open(path,"rb")
    while True:
        chunk=f.read(8192)
        if chunk==b"":
            break
        h.update(chunk)
    f.close()
    return h.hexdigest()


def open_pdf(path):
    if os.path.exists(path)==False:
        raise ValueError(f"文件不存在：{path}")

    try:
        d=pymupdf.open(path)
    except Exception:
        raise ValueError(f"这个文件打不开，可能不是 PDF 或者已损坏：{path}")

    return d


def page_blocks(p):
    out=[]
    for b in p.get_text("blocks"):
        if b[6]!=0:
            continue
        out.append(b)
    return out


def block_text(b):
    return clean_text(b[4])


def blocks_to_paras(blocks,pno,base):
    paras=[]
    pos=base

    for i in range(len(blocks)):
        b=blocks[i]
        txt=block_text(b)
        if txt=="":
            continue

        pid="p"+str(pno)+"-"+f"{i:02d}"
        start=pos
        end=start+len(txt)

        paras.append(Paragraph(
            id=pid,
            page=pno,
            text=txt,
            start=start,
            end=end,
            bbox=(b[0],b[1],b[2],b[3]),
        ))

        pos=end+2

    return paras


def extract_pdf(path):
    d=open_pdf(path)
    rep=check_text_layer(d)
    fp=file_sha(path)

    pages=[]
    all_paras=[]
    base=0

    for pno in range(d.page_count):
        p=d[pno]
        blks=page_blocks(p)
        blks=clean_blocks(blks,p.rect.height)
        paras=blocks_to_paras(blks,pno,base)

        texts=[]
        for x in paras:
            texts.append(x.text)
        ptext="\n\n".join(texts)

        pages.append(Page(
            number=pno,
            start=base,
            text=ptext,
            paragraphs=paras,
            has_text_layer=rep["page_chars"][pno]>0,
        ))

        all_paras.extend(paras)
        base=base+len(ptext)+2

    d.close()

    texts=[]
    for x in pages:
        texts.append(x.text)
    full="\n\n".join(texts)

    return Document(
        doc_id=fp[:16],
        sha256=fp,
        filename=os.path.basename(path),
        page_count=len(pages),
        pages=pages,
        text=full,
        paragraphs=all_paras,
    )
