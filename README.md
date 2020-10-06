# Is this PDF missing text?

Use this script to answer the question. 

```python is_this_pdf_missing_text.py <path/to/pdf>```

```python is_this_pdf_missing_text.py --help

Usage: is_pdf_missing_text.py [OPTIONS] [PATHS]...

  This script detects text in pdf files and prints the path to STDOUT if no
  text is found. Every file is treated as a pdf and the contents of its text
  layer are inspected.  If the file is not a pdf or has no text, a positive
  answer is returned.  Otherwise, a negative answer is returned.

  Note: PATHS accepts any positive number of filepaths.

  Note: By default the paths returned are those of files missing text. Use
  the verbose flag to change this.

Options:
  --verbose  Prints affirmative/negative answers for every file.
  --help     Show this message and exit.

```

# Install Dependencies

```pip install pdftotext click```



