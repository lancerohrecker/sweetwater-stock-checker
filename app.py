from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/check-stock", methods=["POST"])
def check_stock():
    data = request.json
    url = data.get("url")

    if not url or "sweetwater.com" not in url:
        return jsonify({"error": "Invalid or missing URL"}), 400

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_selector(".product-buy-box__availability", timeout=5000)
            status = page.locator(".product-buy-box__availability").inner_text()
            browser.close()
            return jsonify({"status": status.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
