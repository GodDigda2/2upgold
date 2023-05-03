import pdfkit

# txt 파일 경로
txt_file = "C:/Users\papam\OneDrive\Documents\카카오톡 받은 파일\눈물마시는 새.txt"

# pdf 파일 경로
pdf_file = 'C:\Users\papam\OneDrive\Documents\카카오톡 받은 파일\눈물새.pdf'

# txt 파일을 읽어와서 변수에 저장
with open(txt_file, 'r') as f:
    text = f.read()

# pdf 파일 생성
pdfkit.from_string(text, pdf_file)
