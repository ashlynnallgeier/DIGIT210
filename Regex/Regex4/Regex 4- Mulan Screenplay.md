## Regex 4: Mulan Screenplay

The first thing that I did for this assingment was get rid of the metadata for now.

Then, I searched for any of XML's reserved characters (&, <, >). I found none.

Next, I found all blank lines using `(\n){3,}` and replaced them with `\n\n` to get rid of them.

I then wrapped each chunk of text in an `<sp>` element. I found each chunk using  `\n\n` and replaced it with `\n</sp>\n<sp>\n`.

I then enabled "dot matches all" and searched for the whole document using `.+` and replaced it with `<xml>\n\0\n</xml>` to wrap the whole document in a root element. 

The last thing I did was added the metadata back in and manually formatted it, and converted my file to XML.
