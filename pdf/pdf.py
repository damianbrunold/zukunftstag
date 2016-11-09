class pdf_bool(object):
    def __init__(self, value):
        self.value = value
    def fmt(self):
        if self.value:
            return 'true'
        else:
            return 'false'

class pdf_numeric(object):
    def __init__(self, value):
        self.value = value
    def fmt(self):
        return str(self.value)

class pdf_string(object):
    def __init__(self, value):
        self.value = value
    def fmt(self):
        return '(' + self.value + ')'

class pdf_name(object):
    def __init__(self, value):
        self.value = value
    def fmt(self):
        return "/" + self.value

class pdf_array(object):
    def __init__(self, values):
        self.values = values
    def fmt(self):
        return "[" + " ".join([value.fmt() for value in self.values]) + "]"

class pdf_dictionary(object):
    def __init__(self, entries={}):
        self.entries = entries
    def fmt(self):
        return "<< " + " ".join([key.fmt() + " " + value.fmt() for key, value in self.entries]) + " >>"

class pdf_stream(object):
    def __init__(self, contents, entries={}):
        self.dictionary = pdf_dictionary(entries)
        self.contents = contents
        self.dictionary[pdf_name("/Length")] = pdf_numeric(len(contents))
    def fmt(self):
        return self.dictionary.fmt() + "\r\n" + \
               "stream\r\n" + \
               self.contents + "\r\n" + \
               "endstream"
    
class pdf_indirect_obj(object):
    def __init__(self, num, gen, value):
        self.num = num
        self.gen = gen
        self.value = value
    def fmt(self):
        return self.num + " " + self.gen + " obj\r\n" + \
               self.value.fmt() + \
               "endobj"

def pdf_xref(object):
    def __init__(self):
        self.xrefs = [(0, 0, 65535, "f")]
    def add(self, num, gen, offset):
        self.xrefs.append((num, gen, offset, "n"))
    def fmt(self):
        return "xref" # TODO

def pdf_trailer(object):
    def __init(self):
        self.xrefoffset =  0
        self.size = 0
    def fmt(self):
        return "trailer" # TODO

def pdf_file(object):
    def __init__(self):
        self.objects = []
    def fmt(self):
        result = "%PDF-1.4"
        xref = pdf_xref()
        trailer = pdf_trailer()
        for obj in self.objects:
            xref.add(obj.num, obj.gen, len(result))
        trailer.xrefoffset = len(result)
        trailer.size = len(self.objects)
        result += xref.fmt()
        result += trailer.fmt()
        return result


def create_pdf(data):
    return "\r\n".join(["%PDF=1.4",
                ["1 0 obj",
                 "  << /Type /Catalog",
                 "    /Pages 2 0 R",
                 "  >>",
                 "endobj"],
                ["2 0 obj",
                 "  << /Type /Pages",
                 "    /Kids [3 0 R]",
                 "    /Count 1",
                 "  >>",
                 "endobj"],
                ["3 0 obj",
                 "  << /Type /Page",
                 "    /Parent 2 0 R",
                 "    /MediaBox [0 0 x y]",
                 "    /Contents 4 0 R",
                 "    /Resources << /ProcSet 5 0 R /Font << /F1 6 0 R >> >>",
                 "  >>",
                 "endobj"],
                ["4 0 obj",
                 "  << /Length x >>",
                 "stream",
                 data,
                 "endstream",
                 "endobj"],
                ["5 0 obj",
                 "  [/PDF /Text]",
                 "endobj"],
                ["6 0 obj",
                 "  << /Type /Font",
                 "     /Subtype /Type1",
                 "     /Name /F1",
                 "     /BaseFont Helvetica",
                 "     /Encoding /MacRomanEncoding",
                 "  >>",
                 "endobj"]])
            
