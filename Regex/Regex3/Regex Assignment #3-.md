# Regex Assignment #3:
## Convert the text of a novel into XML

The first thing I did for this assingment was to find `&`, `<`, and `>`. None of these were found.

I then searched for all of the extra blank lines using `(\n){3,}` and replaced them with `\n\n` so that they were removed.

I then found all blocks of text using `\n\n`. I replaced them all with `</p>\n<p>` so that each text block was wrapped in a paragraph element.

Next, I found the chapter titles using `<p>([IVXLCDM]+)\.\s+(.*?)</p>` and then replaced it with `<title>\1. \2</title>`.

To find all the text within the chapters, I used `(\s+)([IVX]+\.)(\s\s)(.+)$` to find it, and then replaced it with `\n<title>\2 \4</title>` so that all the text in each chapter, including the titles, were wrapped in a chapter element.

The next step was to remove the extra closing chapter tag from the beginning of the first chapter. I used `<title>.+</title>\n<p>` to find it and replaced it with `</chapter>\n<chapter>\n\0`.

Lastly to find all the quotes, I used `"(.+?)"` and replaced it with `<quote>\1</quote>` to wrap them in quote elements.

I then went back through and manually added a `<booktitle>` element and an `<author>` element to the data at the top of the page.

The very last thing I did was use dot matches all and `(.+)` to highlight the whole document and wrapped it in a root element using `<xml>\1</xml>`.


