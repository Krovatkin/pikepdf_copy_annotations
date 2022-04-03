### Installation:

```shell
 pip install pikepdf
```

### Annotations format:

* Annotations are contained in `page1["/Annots"]`
* User annotations usually have the `"/AP"` property
* Highlights have the following subtype: `"/Subtype": "/Highlight",`

example.txt -- contains 3 annotations
example2.txt -- no annotations
example3.txt -- 1 highlight

### Run the example

* create a pdf file with a single highlight
* make the copy of the file w/o the highlight
* run the example