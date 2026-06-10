import re

for file in ['index.html', 'anda-pay-prototype.html']:
    with open(file, 'r') as f:
        html = f.read()

    # Find the line background:url('Onboadrign bg.png') center/cover no-repeat;
    html = re.sub(r"url\('Onboadrign bg\.png'\)", "url('Assets/Onboadrign%20bg.svg')", html)
    html = re.sub(r'url\("Onboadrign bg\.png"\)', "url('Assets/Onboadrign%20bg.svg')", html)
    html = html.replace('url(Onboadrign bg.png)', "url('Assets/Onboadrign%20bg.svg')")

    with open(file, 'w') as f:
        f.write(html)

print("Splash fixed")
