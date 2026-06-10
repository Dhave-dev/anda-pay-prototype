import re

html_path = 'index.html'
with open(html_path, 'r') as f:
    html = f.read()

svgs = {
    'home': '<svg width="24" height="24" viewBox="32 12 24 24" fill="none"><path d="M51.5402 18.8199L45.7802 14.7899C44.2102 13.6899 41.8002 13.7499 40.2902 14.9199L35.2802 18.8299C34.2802 19.6099 33.4902 21.2099 33.4902 22.4699V29.3699C33.4902 31.9199 35.5602 33.9999 38.1102 33.9999H48.8902C51.4402 33.9999 53.5102 31.9299 53.5102 29.3799V22.5999C53.5102 21.2499 52.6402 19.5899 51.5402 18.8199ZM44.2502 29.9999C44.2502 30.4099 43.9102 30.7499 43.5002 30.7499C43.0902 30.7499 42.7502 30.4099 42.7502 29.9999V26.9999C42.7502 26.5899 43.0902 26.2499 43.5002 26.2499C43.9102 26.2499 44.2502 26.5899 44.2502 26.9999V29.9999Z" fill="currentColor"/></svg>',
    'search': '<svg width="24" height="24" viewBox="128 12 24 24" fill="none"><path d="M139 33C144.247 33 148.5 28.7467 148.5 23.5C148.5 18.2533 144.247 14 139 14C133.753 14 129.5 18.2533 129.5 23.5C129.5 28.7467 133.753 33 139 33Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M149.5 34L147.5 32" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'history': '<svg width="24" height="24" viewBox="223 12 24 24" fill="none"><path d="M231.5 14V17" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M239.5 14V17" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M230.5 25H238.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M230.5 29H235.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M239.5 15.5C242.83 15.68 244.5 16.95 244.5 21.65V27.83C244.5 31.95 243.5 34.01 238.5 34.01H232.5C227.5 34.01 226.5 31.95 226.5 27.83V21.65C226.5 16.95 228.17 15.69 231.5 15.5H239.5Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'settings': '<svg width="24" height="24" viewBox="319 12 24 24" fill="none"><path d="M331.5 27C333.157 27 334.5 25.6569 334.5 24C334.5 22.3431 333.157 21 331.5 21C329.843 21 328.5 22.3431 328.5 24C328.5 25.6569 329.843 27 331.5 27Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M321.5 24.8799V23.1199C321.5 22.0799 322.35 21.2199 323.4 21.2199C325.21 21.2199 325.95 19.9399 325.04 18.3699C324.52 17.4699 324.83 16.2999 325.74 15.7799L327.47 14.7899C328.26 14.3199 329.28 14.5999 329.75 15.3899L329.86 15.5799C330.76 17.1499 332.24 17.1499 333.15 15.5799L333.26 15.3899C333.73 14.5999 334.75 14.3199 335.54 14.7899L337.27 15.7799C338.18 16.2999 338.49 17.4699 337.97 18.3699C337.06 19.9399 337.8 21.2199 339.61 21.2199C340.65 21.2199 341.51 22.0699 341.51 23.1199V24.8799C341.51 25.9199 340.66 26.7799 339.61 26.7799C337.8 26.7799 337.06 28.0599 337.97 29.6299C338.49 30.5399 338.18 31.6999 337.27 32.2199L335.54 33.2099C334.75 33.6799 333.73 33.3999 333.26 32.6099L333.15 32.4199C332.25 30.8499 330.77 30.8499 329.86 32.4199L329.75 32.6099C329.28 33.3999 328.26 33.6799 327.47 33.2099L325.74 32.2199C324.83 31.6999 324.52 30.5299 325.04 29.6299C325.95 28.0599 325.21 26.7799 323.4 26.7799C322.35 26.7799 321.5 25.9199 321.5 24.8799Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/></svg>'
}

def replace_svg(match):
    full_str = match.group(0)
    tab_type = match.group(1)
    class_str = match.group(2)
    tab_name = match.group(3)
    
    is_active = True
    if 'off' in class_str or (tab_type == 'tab-item' and 'active' not in class_str):
        is_active = False

    new_svg = svgs.get(tab_name, '')
    
    # We replace everything from <svg... to </svg>
    new_str = re.sub(r'<svg.*?</svg>', new_svg, full_str, count=1, flags=re.DOTALL)
    
    color = '#1D1E25' if is_active else '#888'
    
    # Remove existing inline style color if any
    new_str = re.sub(r' style="color:#[0-9a-fA-F]+;"', '', new_str)
    
    # Apply new style
    new_str = re.sub(r'(class="(?:nav-tab-lbl|tab-item-lbl)")', f'\\1 style="color:{color};"', new_str)
    
    new_str = new_str.replace('<svg ', f'<svg style="color:{color};" ')
    return new_str

pattern = r'<div class="(nav-tab|tab-item)([^"]*)"[^>]*onclick="navTap\(\'([a-z]+)\'\)".*?</div>'
new_html = re.sub(pattern, replace_svg, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done")
