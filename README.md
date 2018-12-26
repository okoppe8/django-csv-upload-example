# django-csv-upload-example

自作のcsvファイル解析モジュールをwebアプリに組み込むためのシンプルなサンプルです。

要python 3.5以上

## 使い方

```
git clone https://github.com/okoppe8/django-csv-upload-example.git 
```

の後に以下のコマンドを実行

windows

```
cd django-csv-upload-example
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py runserver
```

MacOS/Linux

```
cd django-csv-upload-example
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

最後のコマンドで開発環境が起動するのでブラウザで`http://localhost:8000`にアクセスする。

初期状態ではCSVファイルをアップロードすると件数を表示するので、まずは動作確認をする。

あとは、`app/views.py`の処理部分を自分のコードで置き換える。
