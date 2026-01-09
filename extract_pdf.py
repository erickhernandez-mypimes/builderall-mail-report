
import pypdf

def extract_text_from_pdf(pdf_path, txt_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = pypdf.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            with open(txt_path, 'w') as txt_file:
                txt_file.write(text)
        print(f"Text extracted successfully and saved to {txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_text_from_pdf('terminos_convocatoria.pdf', 'convocatoria.txt')
