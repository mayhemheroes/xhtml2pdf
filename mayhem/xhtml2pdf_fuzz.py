#!/usr/bin/env python3
import io
import sys
import atheris

with atheris.instrument_imports(include=['xhtml2pdf']):
    from xhtml2pdf.w3c.cssParser import CSSParseError
    from xhtml2pdf.context import pisaContext
    from xhtml2pdf.parser import pisaParser


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    consumed_bytes = fdp.ConsumeBytes(fdp.remaining_bytes())

    try:
        html_bytes = b"<html><body><p>" + consumed_bytes + b"</p></body></html>"
        c = pisaContext(".")
        pisaParser(html_bytes, c)
    except (CSSParseError, ValueError, TypeError, AttributeError):
        return


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


# Main program
if __name__ == "__main__":
    main()