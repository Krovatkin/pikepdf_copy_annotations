from pikepdf import Pdf

example = Pdf.open('./wordpress.pdf')
page1 = example.pages[0]
print(page1)
# AP is just an attribute with used in an annotation dict
# see `comment.txt`
popups = [x for x in page1["/Annots"] if "/AP" in x]
no_annot = Pdf.open('wordpress_no_annot.pdf')
# note the use of `copy_foreign`
no_annot.pages[0]["/Annots"].append(no_annot.copy_foreign(popups[0]))
no_annot.save('no_annot2.pdf')