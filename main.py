import os
import sys
import fitz  # import PyMuPDF...for whatever reason it is called fitz

def main():
    boltok = {
        'Anker': '31429_63668',
        'Centenárium': '31429_84206',
        'Jókai': '31429_83271',
        'József_Attila': '31429_84215',
        'Kada': '31429_82987',
        'Kecskemét': '31429_84218',
        'Legénybíró': '31429_84210',
        'Munkásotthon': '31429_65313',
        'Szabad_Május': '31429_45246',
        'Lovaspark': '31429_31429',
        'Roken': '70163',
        'Sun Leaves': '70206',
        'Tobacco Leaves': '70199',
        'Tobacconist Trade': '70116'
    }

    dir = ''

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