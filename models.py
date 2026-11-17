class Paragraph:

    def __init__(self,id,page,text,start,end,bbox):
        self.id=id
        self.page=page
        self.text=text
        self.start=start
        self.end=end
        self.bbox=bbox

    def to_dict(self):
        d={}
        d["id"]=self.id
        d["page"]=self.page
        d["text"]=self.text
        d["start"]=self.start
        d["end"]=self.end
        d["bbox"]=list(self.bbox)
        return d


class Page:

    def __init__(self,number,start,text,paragraphs,has_text_layer):
        self.number=number
        self.start=start
        self.text=text
        self.paragraphs=paragraphs
        self.has_text_layer=has_text_layer

    def to_dict(self):
        d={}
        d["number"]=self.number
        d["start"]=self.start
        d["text"]=self.text
        d["has_text_layer"]=self.has_text_layer
        ps=[]
        for p in self.paragraphs:
            ps.append(p.to_dict())
        d["paragraphs"]=ps
        return d


class Document:

    def __init__(self,doc_id,sha256,filename,page_count,pages,text,paragraphs):
        self.doc_id=doc_id
        self.sha256=sha256
        self.filename=filename
        self.page_count=page_count
        self.pages=pages
        self.text=text
        self.paragraphs=paragraphs

    def __repr__(self):
        return "Document(" + self.filename + ")"

    def page_of_offset(self,offset):
        for p in self.pages:
            page_end=p.start+len(p.text)
            if p.start<=offset<page_end:
                return p.number
        return -1

    def paragraph_at(self,offset):
        for para in self.paragraphs:
            if para.start<=offset<para.end:
                return para
        return None

    def to_dict(self):
        d={}
        d["doc_id"]=self.doc_id
        d["sha256"]=self.sha256
        d["filename"]=self.filename
        d["page_count"]=self.page_count
        d["text"]=self.text
        ps=[]
        for p in self.pages:
            ps.append(p.to_dict())
        d["pages"]=ps
        qs=[]
        for q in self.paragraphs:
            qs.append(q.to_dict())
        d["paragraphs"]=qs
        return d