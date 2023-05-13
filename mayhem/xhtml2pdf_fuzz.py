#!/usr/bin/env python3
import io
import sys
import atheris

with atheris.instrument_imports(include=['xhtml2pdf']):
    from xhtml2pdf.w3c.cssParser import CSSParseError
    from xhtml2pdf import pisa
    from xhtml2pdf.context import pisaContext
    from xhtml2pdf.parser import pisaParser
    from xhtml2pdf.document import pisaDocument
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    #opt = fdp.ConsumeIntInRange(1, 3)
    consumed_bytes = fdp.ConsumeBytes(fdp.remaining_bytes())

    try:
        html_bytes = b"<html><body><p>" + consumed_bytes + b"</p></body></html>"
        # Test parser
        #if opt == 1:
         #   pisaParser(html_bytes, pisaContext(None))


        pisaParser(html_bytes, pisaContext(None))
        # Test in memory file
        # with io.BytesIO() as in_memory_file:
        #     if opt == 2:
        #         pisaDocument(html_bytes, dest=in_memory_file)
        #     else:
        #         # convert HTML to PDF
        #         pisa.CreatePDF(html_bytes, dest=in_memory_file, quiet=True, log_warn=1, log_err=1)
    except (CSSParseError, ValueError, TypeError, AttributeError):
        return


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


# Main program
if __name__ == "__main__":
    #fh = open('/dev/null', 'wb')
    main()
    #fh.close()
