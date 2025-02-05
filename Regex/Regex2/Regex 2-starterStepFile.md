## Regex 2: Lots of sonnets

Cut the top and bottom from Project Gutenberg out as not relevant / worth keeping here. 


First step was to search for the characters that will disrupt XML encoding: 
`&`, `<`, `>`. 
XML is not allowed to contain raw ampersand characters `&`. 
I searched for:

```
&
```
and did not find any.

I also searched for `<` and `>` and did not find them. 

I then searched for all leading spaces at the beginning of the lines using find:
`^\s\s`
. I then replaced it with nothing, trimming off the extra spaces at the beginning of each line.

I then found all lines using `^(.*)$` and used `<line>\1</line>` to wrap all the lines.

I found all the Roman numerals by using `<line>\s*([IVXLCDM]+)\s*</line>` and replaced them with `<sonnet number="\1">` so that the roman numerals became an attribute within the sonnet element.

Next, I did some formatting with the line elements, searching for `<line>` and replacing it with `\t\t\0`
.

I then found the beginning sonnet tag using `(<sonnet number="([IVXLCDM]+)">)`
and replaced it with `</sonnet>\1` so that there would be a closing sonnet tag at the end of each sonnet. I manually went back and removed the closing sonnet tage before the first sonnet.

The last thing I did was find the whole document using `^.+` and checked "dot matches all", then replaced it with `<xml>\n,\0,\n</xml>` so that the whole text file was wrapped in an xml element.

I converted the file to an xml file.