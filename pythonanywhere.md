# PythonAnyWhereアップロード時の変更点
- /post_test/settings.py
    1. DEBUG = False
    2. ALLOWED_HOSTS = ['barsy1414.pythonanywhere.com']
- /main/urls.py
    1. index以外のパスから'/'を消す