import re

for filename in ['index.html', 'anda-pay-prototype.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # Add to .bottom-nav
    content = re.sub(r'(\.bottom-nav\{[^\}]*?)(?=\})', r'\1 border-bottom-left-radius: 44px; border-bottom-right-radius: 44px;', content)

    # Add to .tab-bottom-nav
    content = re.sub(r'(\.tab-bottom-nav\{[^\}]*?)(?=\})', r'\1 border-bottom-left-radius: 44px; border-bottom-right-radius: 44px;', content)
    
    # Add WebKit mask to .phone
    content = re.sub(r'(\.phone\{[^\}]*?)(?=\})', r'\1 -webkit-mask-image: -webkit-radial-gradient(white, black); transform: translateZ(0);', content)

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")

