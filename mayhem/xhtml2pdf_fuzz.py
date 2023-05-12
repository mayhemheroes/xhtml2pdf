#!/usr/bin/env python3

import sys
import atheris

with atheris.instrument_imports(include=['xhtml2pdf']):
    from xhtml2pdf.w3c.cssParser import CSSParseError
    from xhtml2pdf import pisa


def TestOneInput(data):
    # convert HTML to PDF
    global run
    fdp = atheris.FuzzedDataProvider(data)
    run += 1
    try:
        consumed_bytes = fdp.ConsumeBytes(fdp.remaining_bytes())
        fh = open('/dev/null', 'wb')
        pisa.CreatePDF(consumed_bytes, dest=fh, quiet=True, log_warn=1, log_err=1)
        fh.close()
    except (CSSParseError, ValueError):
        if run > 10000:
            raise
        return


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


# Main program
if __name__ == "__main__":
    run = 0
    main()
