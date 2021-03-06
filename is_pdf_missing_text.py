import pdftotext
import click

POSITIVE = "YES"
NEGATIVE = "NO"

@click.command()
@click.argument('paths', type=click.Path(exists=True), nargs=-1)
@click.option('--verbose', is_flag=True, default=False, help="Prints affirmative/negative answers for every file.")
def report_text_presence(paths, verbose):
    """ This script detects text in pdf files and prints the path to STDOUT if no text is found.
    Every file is treated as a pdf and the contents of its text layer are inspected. 
    If the file is not a pdf or has no text, a positive answer is returned. 
    Otherwise, a negative answer is returned.

    Note: PATHS accepts any positive number of filepaths. 

    Note: By default the paths returned are those of files missing text. Use the verbose flag to change this.

    """
    
    for path in paths:
        result = is_pdf_missing_text(path)
        
        if verbose:
            report = POSITIVE + "\t: " if result else NEGATIVE + "\t: "
            report += path
        else:
            report = path if result else None
        
        if report:
            print(report)


def is_pdf_missing_text(path):
    text = load(path)

    if not text or text is None:
        return True
    else:
        return False


def load(path):
    with open(path, "rb") as f:
        try:
            document = pdftotext.PDF(f)
            text = ("\n".join(document))
            text = text.strip()
            if not text:
                text = None
        except pdftotext.Error:
            text = None


    return text

if __name__ == '__main__':
    report_text_presence()
