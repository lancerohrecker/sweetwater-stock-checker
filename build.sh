#!/bin/bash

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Playwright Chromium..."
npx playwright install chromium
