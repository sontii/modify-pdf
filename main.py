import os
import sys
import fitz  # import PyMuPDF...for whatever reason it is called fitz

from bolt import boltok

def main():
    dir = None

    if len(sys.argv) > 1:
        dir = sys.argv[1]

    for bolt, kod in boltok.items():   
        for file in os.listdir(dir):
            if file.lower().endswith("szla.pdf") and kod in file.lower():
                doc = fitz.open(dir + "\\" + file) # the file with the text you want to change
                for page in doc:
                    found = page.search_for(kod)  # list of rectangles where to replace
                    for item in found:
                        page.add_redact_annot(item, '')  # create redaction for text
                        page.apply_redactions()  # apply the redaction now
                        page.insert_text(item.bl - (0, 2), kod + " - " + bolt, fontsize=8)

                doc.saveIncr()


if __name__ == "__main__":
    main()