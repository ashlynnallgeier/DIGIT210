# Regex Autotagging: Dracula

The first thing I did was search for any of XML's reserved characters. I found 16 occurences of `&` and I replaced them with `&amp;`. Then I searched for `<` and `>` and found none.

Next, I found all blank lines using `^\s*\n` and replaced them with nothing to get rid of them.

Next, I wrapped every line in a `<p>` element using `find: ^.+$` and replaced with `<p>\0</p>`.

The next step was to replace <p> tags with <heading> tags for chapter headings. I found `(<p>)(CHAPTER [IVXLCD]+)(</p>)` and replaced it with `<heading>\2</heading>`.

Add <chapter> tags to enclose each chapter and its heading. I found the `<heading>` element and replaced it with `</chapter>\n\n<chapter>\n\n\0`.

	
I then enabled "dot matches all" and searched for the whole document using `.+` and replaced it with `<xml>\n\0\n</xml>` to wrap the whole document in a root element.

The last thing I did was manually wrap "DRACULA" in a `<title>` tag.

Then, I worked on the XSLT.


