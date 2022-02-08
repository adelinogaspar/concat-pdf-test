import base64, os

__BASE_DIR__ = os.path.dirname(__file__)

def get_file(filename):
    with open(filename, "rb") as binary_file:
        return binary_file.read()


def encode(text):
    return base64.b64encode(text)


def decode_and_write_file(destination_file, base64_string):
    decoded_file = base64.b64decode(base64_string)
    with open(destination_file, "wb") as binary_dest_file:
        binary_dest_file.write(decoded_file)


def merge_pdfs(pdfs):
    import PyPDF2, io
    
    merge_file = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merge_file.append(PyPDF2.PdfFileReader(io.BytesIO(pdf)), 'rb')

    tmp = io.BytesIO()
    merge_file.write(tmp)
    return tmp.getvalue()


def main():
    google = get_file(f"{__BASE_DIR__}/pdf/logo-google.pdf")
    instagram = get_file(f"{__BASE_DIR__}/pdf/logo-instagram.pdf")
    google_insta = merge_pdfs([google, instagram])
    google_insta_base64 = base64.b64encode(google_insta)

    decode_and_write_file(f"{__BASE_DIR__}/pdf/test-concat.pdf", google_insta_base64)


if __name__ == "__main__":
    main()        