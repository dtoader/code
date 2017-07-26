# basic_wsgi_pdf_server.py
# Basic WSGI PDF server in Python.
# Adapted from:

# http://www.reddit.com/r/Python/comments/1eboql/python_website_tuts_that_dont_use_django/c9z3qyz

from PDFWriter import PDFWriter
from wsgiref.simple_server import make_server

host = 'localhost'
port = 8888

def app(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    print "path:", path
    print "method:", method

    #response = 'This is the page for "{}"'.format(path)

    lines = [
            "Jack and Jill went up the hill",
            "Humpty Dumpty sat on a wall,",
            "'You are old, Father William,' the young man said,",
            "Master of all masters"
            ]

    pdf_filename = "Nursery-rhymes-and-stories.pdf"
    pw = PDFWriter(pdf_filename)
    pw.setFont("Courier", 12)
    pw.setHeader("Excerpts from nursery rhymes and stories")
    pw.setFooter("Generated by xtopdf and basic_wsgi_pdf_server")

    for line in lines:
        pw.writeLine(line)
        pw.writeLine(" ")
    pw.close()

    with open(pdf_filename, "rb") as fil:
        response = fil.read()

    #start_response('200 OK', [('Content-type', 'text/html')])
    start_response('200 OK', [('Content-type', 'application/pdf')])
    return [response]

make_server(host, port, app).serve_forever()
