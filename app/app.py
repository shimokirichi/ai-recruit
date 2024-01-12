import os
from openai import OpenAI
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from openai_service import OpenaiService
from recuirt_position import RecruitPosition

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('profile.html')

@app.route('/upload', methods=['POST'])
def upload_and_summarize():
    service = OpenaiService()

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)

        # PDFからテキストを抽出
        print("start extract_text")
        resume_content = extract_text(pdf_path)
        print("end extract_text")

        print("start request OpenAI")
        response = service.analysis(resume_content, RecruitPosition.ENGINNEER)
        summary = response.choices[0].message.content
        print("receive request OpenAI")

        summary = summary.removeprefix("```html") if summary.startswith("```html") else summary
        summary = summary.removesuffix("```") if summary.endswith("```") else summary

        # 一時的に保存したPDFを削除
        # os.remove(pdf_path)

        return jsonify({"summary": summary}), 200

    return jsonify({"error": "File is not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
