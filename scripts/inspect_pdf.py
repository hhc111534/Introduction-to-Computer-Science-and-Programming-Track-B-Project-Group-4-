import argparse
import pymupdf

def show_page(p,n):
    h=p.rect.height
    blks=p.get_text("blocks")
    nchar=len(p.get_text())

    print()
    print(f"=== 第 {p.number + 1} 页 ===")
    print(f"块的数量：{len(blks)}")
    print(f"字符数：{nchar}")
    print(f"页面高度：{round(h)}")

    for b in blks:
        x0=b[0]
        y0=b[1]
        x1=b[2]
        y1=b[3]
        t=b[4]
        bno=b[5]
        bt=b[6]

        if bt==0:
            k="文字"
        else:
            k="图片"

        s=t.replace("\n", " / ")
        s=s.strip()
        s=s[:n]

        tag=""
        if y0<h*0.08:
            tag="   <-- 顶部边缘，可能是页眉"
        elif y1>h*0.92:
            tag="   <-- 底部边缘，可能是页脚"

        print(f"[{bno}] {k}   y = {round(y0, 1)} ~ {round(y1, 1)}")
        print(f'     "{s}"{tag}')


def main():
    ap=argparse.ArgumentParser(description="打印 PDF 每一页的文字块")
    ap.add_argument("pdf", help="PDF 文件的路径")
    ap.add_argument("--page", type=int, default=0, help="只看第几页（从 1 开始），不填就看全部")
    ap.add_argument("--chars", type=int, default=40, help="每个块最多显示多少个字")
    a=ap.parse_args()

    d=pymupdf.open(a.pdf)
    print(f"文件：{a.pdf}")
    print(f"总页数：{d.page_count}")

    if a.page>0:
        if a.page>d.page_count:
            print(f"没有第 {a.page} 页，这个文件一共只有 {d.page_count} 页。")
            d.close()
            return
        ps=[d[a.page - 1]]
    else:
        ps=d

    for p in ps:
        show_page(p, a.chars)

    d.close()


if __name__=="__main__":
    main()
