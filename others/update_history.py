import re

html_path = 'index.html'
with open(html_path, 'r') as f:
    html = f.read()

# 1. Update the CSS for the dashboard amount wrap issue and add dividers
old_stat_val = ".hist-stat-val{font-size:20px;font-weight:700;color:#fff;letter-spacing:-.5px;font-family:'Gilroy',sans-serif;line-height:1.2;}"
new_stat_val = ".hist-stat-val{font-size:18px;font-weight:700;color:#fff;letter-spacing:-.5px;font-family:'Gilroy',sans-serif;line-height:1.2;white-space:nowrap;}\n.hist-stats-card > .hist-stat:not(:last-child){border-right: 1px solid rgba(255,255,255,0.1); padding-right: 15px;}\n.hist-stats-card{gap: 15px;}"
html = html.replace(old_stat_val, new_stat_val)

# If it's already there from previous run, update it
html = re.sub(r'\.hist-stats-card\{background:#1d1e25;border-radius:16px;padding:18px 20px;display:flex;justify-content:space-between;margin-bottom:20px;color:#fff;\}',
              r'.hist-stats-card{background:#1d1e25;border-radius:16px;padding:18px 20px;display:flex;justify-content:space-between;margin-bottom:20px;color:#fff;gap:15px;}', html)


# 2. Replace the History list
# From <!-- Today --> down to right before <div class="tab-bottom-nav">
pattern = r'<!-- Today -->.*?<div class="tab-bottom-nav">'
new_list = """<!-- Today -->
        <div class="hist-date-hdr" style="font-size:13px; font-weight:600; color:#575757; margin-bottom:8px; font-family:'Gilroy',sans-serif;">Today · 12 May 2025</div>
        <div class="hist-card" style="margin-bottom: 20px;">
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">João Baptista</div>
              <div class="hist-sub">Bajaj tuk-tuk · 09:34</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+25,000 Kz</div>
              <div class="hist-ref">#AP-0514-8834</div>
            </div>
          </div>
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">Maria Santos</div>
              <div class="hist-sub">Smartphone · 09:12</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+8,500 Kz</div>
              <div class="hist-ref">#AP-0514-8801</div>
            </div>
          </div>
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">Esperança Lima</div>
              <div class="hist-sub">Bajaj tuk-tuk · 08:14</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+25,000 Kz</div>
              <div class="hist-ref">#AP-0514-8729</div>
            </div>
          </div>
        </div>

        <!-- Yesterday -->
        <div class="hist-date-hdr" style="font-size:13px; font-weight:600; color:#575757; margin-bottom:8px; font-family:'Gilroy',sans-serif;">Yesterday · 11 May 2025</div>
        <div class="hist-card" style="margin-bottom:80px;">
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">João Baptista</div>
              <div class="hist-sub">Bajaj tuk-tuk · 09:34</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+25,000 Kz</div>
              <div class="hist-ref">#AP-0514-8834</div>
            </div>
          </div>
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">Maria Santos</div>
              <div class="hist-sub">Smartphone · 09:12</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+8,500 Kz</div>
              <div class="hist-ref">#AP-0514-8801</div>
            </div>
          </div>
          <div class="hist-item">
            <div class="pay-avatar" style="background:transparent;"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div class="hist-info" style="flex:1;">
              <div class="hist-name">Alberto Cunha</div>
              <div class="hist-sub">Battery replace · 08:58</div>
            </div>
            <div class="hist-right" style="text-align:right;">
              <div class="hist-amount" style="color:#1d1e25;">+15,000 Kz</div>
              <div class="hist-ref">#AP-0514-8779</div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-bottom-nav">"""

html = re.sub(pattern, new_list, html, flags=re.DOTALL)

# 3. Update the SVGs logic
active_svgs = {
    'home': '<svg width="24" height="24" viewBox="32 12 24 24" fill="none"><path d="M51.5402 18.8199L45.7802 14.7899C44.2102 13.6899 41.8002 13.7499 40.2902 14.9199L35.2802 18.8299C34.2802 19.6099 33.4902 21.2099 33.4902 22.4699V29.3699C33.4902 31.9199 35.5602 33.9999 38.1102 33.9999H48.8902C51.4402 33.9999 53.5102 31.9299 53.5102 29.3799V22.5999C53.5102 21.2499 52.6402 19.5899 51.5402 18.8199ZM44.2502 29.9999C44.2502 30.4099 43.9102 30.7499 43.5002 30.7499C43.0902 30.7499 42.7502 30.4099 42.7502 29.9999V26.9999C42.7502 26.5899 43.0902 26.2499 43.5002 26.2499C43.9102 26.2499 44.2502 26.5899 44.2502 26.9999V29.9999Z" fill="currentColor"/></svg>',
    'search': '<svg width="24" height="24" viewBox="128 12 24 24" fill="none"><path d="M139 33C144.247 33 148.5 28.7467 148.5 23.5C148.5 18.2533 144.247 14 139 14C133.753 14 129.5 18.2533 129.5 23.5C129.5 28.7467 133.753 33 139 33Z" fill="currentColor"/><path d="M148.801 34.0001C148.621 34.0001 148.441 33.9301 148.311 33.8001L146.451 31.9401C146.181 31.6701 146.181 31.2301 146.451 30.9501C146.721 30.6801 147.161 30.6801 147.441 30.9501L149.301 32.8101C149.571 33.0801 149.571 33.5201 149.301 33.8001C149.161 33.9301 148.981 34.0001 148.801 34.0001Z" fill="currentColor"/></svg>',
    'history': '<svg width="24" height="24" viewBox="223 12 24 24" fill="none"><path d="M231.789 18.29C231.369 18.29 231.039 17.95 231.039 17.54V14.75C231.039 14.34 231.369 14 231.789 14C232.209 14 232.539 14.34 232.539 14.75V17.53C232.539 17.95 232.209 18.29 231.789 18.29Z" fill="currentColor"/><path d="M239.211 18.29C238.791 18.29 238.461 17.95 238.461 17.54V14.75C238.461 14.33 238.801 14 239.211 14C239.631 14 239.961 14.34 239.961 14.75V17.53C239.961 17.95 239.631 18.29 239.211 18.29Z" fill="currentColor"/><path d="M243.07 16.5C242.41 16.01 241.46 16.48 241.46 17.31V17.41C241.46 18.58 240.62 19.66 239.45 19.78C238.1 19.92 236.96 18.86 236.96 17.54V16.5C236.96 15.95 236.51 15.5 235.96 15.5H235.04C234.49 15.5 234.04 15.95 234.04 16.5V17.54C234.04 18.33 233.63 19.03 233.01 19.42C232.92 19.48 232.82 19.53 232.72 19.58C232.63 19.63 232.53 19.67 232.42 19.7C232.3 19.74 232.17 19.77 232.03 19.78C231.87 19.8 231.71 19.8 231.55 19.78C231.41 19.77 231.28 19.74 231.16 19.7C231.06 19.67 230.96 19.63 230.86 19.58C230.76 19.53 230.66 19.48 230.57 19.42C229.94 18.98 229.54 18.22 229.54 17.41V17.31C229.54 16.54 228.72 16.08 228.07 16.41C228.06 16.42 228.05 16.42 228.04 16.43C228 16.45 227.97 16.47 227.93 16.5C227.9 16.53 227.86 16.55 227.83 16.58C227.55 16.8 227.3 17.05 227.09 17.32C226.98 17.44 226.89 17.57 226.81 17.7C226.8 17.71 226.79 17.72 226.78 17.74C226.69 17.87 226.61 18.02 226.54 18.16C226.52 18.18 226.51 18.19 226.51 18.21C226.45 18.33 226.39 18.45 226.35 18.58C226.32 18.63 226.31 18.67 226.29 18.72C226.23 18.87 226.19 19.02 226.15 19.17C226.11 19.31 226.08 19.46 226.06 19.61C226.04 19.72 226.03 19.83 226.02 19.95C226.01 20.09 226 20.23 226 20.37V29.13C226 31.82 228.18 34 230.87 34H240.13C242.82 34 245 31.82 245 29.13V20.37C245 18.78 244.24 17.39 243.07 16.5ZM235.5 29.42H230.86C230.45 29.42 230.11 29.08 230.11 28.67C230.11 28.25 230.45 27.91 230.86 27.91H235.5C235.92 27.91 236.25 28.25 236.25 28.67C236.25 29.08 235.92 29.42 235.5 29.42ZM238.28 25.71H230.86C230.45 25.71 230.11 25.37 230.11 24.96C230.11 24.54 230.45 24.2 230.86 24.2H238.28C238.7 24.2 239.04 24.54 239.04 24.96C239.04 25.37 238.7 25.71 238.28 25.71Z" fill="currentColor"/></svg>',
    'settings': '<svg width="24" height="24" viewBox="319 12 24 24" fill="none"><path d="M331.5 27C333.157 27 334.5 25.6569 334.5 24C334.5 22.3431 333.157 21 331.5 21C329.843 21 328.5 22.3431 328.5 24C328.5 25.6569 329.843 27 331.5 27Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M321.5 24.8799V23.1199C321.5 22.0799 322.35 21.2199 323.4 21.2199C325.21 21.2199 325.95 19.9399 325.04 18.3699C324.52 17.4699 324.83 16.2999 325.74 15.7799L327.47 14.7899C328.26 14.3199 329.28 14.5999 329.75 15.3899L329.86 15.5799C330.76 17.1499 332.24 17.1499 333.15 15.5799L333.26 15.3899C333.73 14.5999 334.75 14.3199 335.54 14.7899L337.27 15.7799C338.18 16.2999 338.49 17.4699 337.97 18.3699C337.06 19.9399 337.8 21.2199 339.61 21.2199C340.65 21.2199 341.51 22.0699 341.51 23.1199V24.8799C341.51 25.9199 340.66 26.7799 339.61 26.7799C337.8 26.7799 337.06 28.0599 337.97 29.6299C338.49 30.5399 338.18 31.6999 337.27 32.2199L335.54 33.2099C334.75 33.6799 333.73 33.3999 333.26 32.6099L333.15 32.4199C332.25 30.8499 330.77 30.8499 329.86 32.4199L329.75 32.6099C329.28 33.3999 328.26 33.6799 327.47 33.2099L325.74 32.2199C324.83 31.6999 324.52 30.5299 325.04 29.6299C325.95 28.0599 325.21 26.7799 323.4 26.7799C322.35 26.7799 321.5 25.9199 321.5 24.8799Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/></svg>'
}

inactive_svgs = {
    'home': '<svg width="24" height="24" viewBox="32 12 24 24" fill="none"><path d="M40.52 14.8399L35.13 19.0399C34.23 19.7399 33.5 21.2299 33.5 22.3599V29.7699C33.5 32.0899 35.39 33.9899 37.71 33.9899H49.29C51.61 33.9899 53.5 32.0899 53.5 29.7799V22.4999C53.5 21.2899 52.69 19.7399 51.7 19.0499L45.52 14.7199C44.12 13.7399 41.87 13.7899 40.52 14.8399Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M43.5 29.99V26.99" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'search': '<svg width="24" height="24" viewBox="128 12 24 24" fill="none"><path d="M139 33C144.247 33 148.5 28.7467 148.5 23.5C148.5 18.2533 144.247 14 139 14C133.753 14 129.5 18.2533 129.5 23.5C129.5 28.7467 133.753 33 139 33Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M149.5 34L147.5 32" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'history': '<svg width="24" height="24" viewBox="223 12 24 24" fill="none"><path d="M231.5 14V17" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M239.5 14V17" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M230.5 25H238.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M230.5 29H235.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M239.5 15.5C242.83 15.68 244.5 16.95 244.5 21.65V27.83C244.5 31.95 243.5 34.01 238.5 34.01H232.5C227.5 34.01 226.5 31.95 226.5 27.83V21.65C226.5 16.95 228.17 15.69 231.5 15.5H239.5Z" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'settings': active_svgs['settings']
}

def replace_svg(match):
    full_str = match.group(0)
    tab_type = match.group(1)
    class_str = match.group(2)
    tab_name = match.group(3)
    
    is_active = True
    if 'off' in class_str or (tab_type == 'tab-item' and 'active' not in class_str):
        is_active = False

    new_svg = active_svgs.get(tab_name, '') if is_active else inactive_svgs.get(tab_name, '')
    
    new_str = re.sub(r'<svg.*?</svg>', new_svg, full_str, count=1, flags=re.DOTALL)
    
    color = '#1D1E25' if is_active else '#888'
    
    new_str = re.sub(r' style="color:#[0-9a-fA-F]+;"', '', new_str)
    new_str = re.sub(r'(class="(?:nav-tab-lbl|tab-item-lbl)")', f'\\1 style="color:{color};"', new_str)
    new_str = new_str.replace('<svg ', f'<svg style="color:{color};" ')
    return new_str

pattern_svg = r'<div class="(nav-tab|tab-item)([^"]*)"[^>]*onclick="navTap\(\'([a-z]+)\'\)".*?</div>'
html = re.sub(pattern_svg, replace_svg, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

with open('anda-pay-prototype.html', 'w') as f:
    f.write(html)
print("Updated index.html and anda-pay-prototype.html")

