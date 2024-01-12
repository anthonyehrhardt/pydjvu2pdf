import subprocess

def djvu_to_pdf(ddjvu_executable, input_djvu, output_pdf):
    try:
        subprocess.run([ddjvu_executable, "-format=pdf", "-quality=85", input_djvu, output_pdf], check=True)
        print(f"Conversion successful. PDF created: {output_pdf}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to convert DJVU to PDF.")

if __name__ == "__main__":
    #ddjvu_executable_path = r"C:\path\to\ddjvu.exe"  # Replace with the actual path
    ddjvu_executable_path = r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe"
    input_djvu_path = "file.djvu"
    output_pdf_path = "file.pdf"

    djvu_to_pdf(ddjvu_executable_path, input_djvu_path, output_pdf_path)
