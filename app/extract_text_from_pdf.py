from pdfminer import high_level

# PDF ファイルからテキストを抽出する関数
def extract_text_from_pdf(file_path):
    try:
        text = high_level.extract_text(file_path)
        return text
    except Exception as e:
        print(f"Failed to extract text from PDF: {e}")
        return None

# # ローカル実行用
# if __name__ == "__main__":
#     pdf_file = "document4.pdf"  # 抽出する PDF ファイルのパスを指定します
#
#     extracted_text = extract_text_from_pdf(pdf_file)
#     if extracted_text:
#         with open("document.txt", "w") as file:
#             file.write(extracted_text)