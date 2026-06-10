import re

html_path = 'index.html'
with open(html_path, 'r') as f:
    html = f.read()

pattern = r'\s*<button class="st-scan-btn" onclick="goTo\(\'qr-scan\'\)">\s*<svg.*?</svg>\s*Scan QR Code\s*</button>'
html = re.sub(pattern, '', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

with open('anda-pay-prototype.html', 'w') as f:
    f.write(html)
print("Removed st-scan-btn")

