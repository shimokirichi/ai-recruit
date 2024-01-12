# ベースイメージの指定
FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージが記入されたファイルをコピー
COPY requirements.txt /app/

# Pythonパッケージをインストール
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . /app

# アプリケーションを実行
CMD ["python", "app.py"]
