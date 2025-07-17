from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)
