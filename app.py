import os, zipfile, threading, subprocess, sys
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Online! ✅"

def run_bot():
    # هذا الاسم يجب أن يطابق اسم ملف الزيب المرفوع عندك
    zip_name = "zip.Zakaria (1).zip" 
    if os.path.exists(zip_name):
        with zipfile.ZipFile(zip_name, 'r') as z:
            z.extractall("my_bot")
        os.chdir("my_bot")
        py_files = [f for f in os.listdir('.') if f.endswith('.py')]
        if py_files: subprocess.Popen([sys.executable, py_files[0]])

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
