import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Keep API credentials in .env. Never commit .env to GitHub.
AIFORTHAI_API_KEY = os.getenv("AIFORTHAI_API_KEY", "").strip()


def analyze_with_aiforthai(text):
    """
    Calls AIForThai's sentiment service using the official `aift` package.
    Check the current AIForThai documentation and account permissions because
    service names, API access, and response formats can change.
    """
    if not AIFORTHAI_API_KEY:
        raise ValueError(
            "ยังไม่ได้ตั้งค่า AIFORTHAI_API_KEY ในไฟล์ .env "
            "โปรดอ่าน README.md ก่อนเริ่มใช้งาน"
        )

    try:
        from aift import setting
        from aift.nlp import sentiment
    except ImportError as exc:
        raise RuntimeError(
            "ไม่พบแพ็กเกจ aift กรุณารัน pip install -r requirements.txt"
        ) from exc

    setting.set_api_key(AIFORTHAI_API_KEY)
    return sentiment.analyze(text, engine="emonews")


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    result = None
    error = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if not text:
            error = "กรุณากรอกข้อความก่อนวิเคราะห์"
        elif len(text) > 5000:
            error = "กรุณากรอกข้อความไม่เกิน 5,000 ตัวอักษร"
        else:
            try:
                result = analyze_with_aiforthai(text)
            except Exception as exc:
                # Keep user-facing errors helpful, without exposing secret values.
                error = str(exc)

    return render_template("index.html", text=text, result=result, error=error)


@app.route("/health")
def health():
    return {"status": "ok", "api_key_configured": bool(AIFORTHAI_API_KEY)}


if __name__ == "__main__":
    # Local development only. For deployment, use a production WSGI server.
    app.run(debug=True)
