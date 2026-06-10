import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # 1. Add "position:relative;" to screen-driver-profile
    html = html.replace('<div class="screen" id="screen-driver-profile">', '<div class="screen" id="screen-driver-profile" style="position:relative;">')

    # 2. Replace everything from <div class="dp-header"> down to <!-- History tab -->
    # Find the bounds
    start_pattern = r'<div class="dp-header">'
    end_pattern = r'<!-- History tab -->'
    
    start_idx = html.find('<div class="dp-header">', html.find('id="screen-driver-profile"'))
    end_idx = html.find('<!-- History tab -->', start_idx)

    new_content = """<div class="dp-header">
        <div onclick="goBack()" style="cursor:pointer; display:flex; align-items:center; justify-content:flex-start; width:40px; height:40px;"><img src="Icons folder/arrow-left 2.svg" style="width:24px;height:24px;"></div>
        <span style="font-size:16px;font-weight:600;color:#1d1e25;">Driver Profile</span>
        <div style="width:40px;"></div>
      </div>
      <div class="dp-body">
        <div class="dp-hero">
          <div class="dp-hero-top">
            <div class="dp-av" style="width:80px;height:80px;border-radius:50%;background:transparent;overflow:hidden;flex-shrink:0;box-shadow: 0 4px 10px rgba(0,0,0,0.1);"><img src="Assets/Avatar.svg" style="width:100%;height:100%;object-fit:cover;"></div>
            <div style="flex:1;">
              <div class="dp-name-row" style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 2px;">
                <span class="dp-name" style="font-size:18px; font-weight:600; letter-spacing:-0.4px;">João Mbemba</span>
                <span class="dp-badge-active" style="background:#E2F6F4; color:#007B83; padding:4px 12px; border-radius:12px; font-size:10px; font-weight:700;">Active</span>
              </div>
              <div class="dp-sub" style="color:#575757; font-size:13px; margin-bottom: 4px;">AOL-2847-X · EV Bike</div>
              <div class="dp-phone" style="display:flex; align-items:center; gap:6px; font-size:12px; color:#575757; font-weight:500;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg> +244 923 456 789</div>
            </div>
          </div>
          <div class="dp-reliability" style="background:#F7F8F9; border-radius:12px; padding:12px 16px;">
            <div class="dp-rel-row"><span class="dp-rel-lbl" style="font-size:11px; font-weight:600; color:#575757;">Payment reliability · last 6 weeks</span><span class="dp-rel-score" style="font-size:11px; font-weight:700; color:#43848E;">4 / 6 on time</span></div>
            <div class="dp-dots-row" style="margin-top:10px;">
              <div class="dp-dots" style="gap:6px;">
                <div class="dp-dot p" style="width:16px;height:16px;border-radius:8px;background:#40C484;border:none;"></div><div class="dp-dot p" style="width:16px;height:16px;border-radius:8px;background:#40C484;border:none;"></div><div class="dp-dot m" style="width:16px;height:16px;border-radius:8px;background:#E5E7EB;border:1px solid rgba(0,0,0,0.05);"></div><div class="dp-dot p" style="width:16px;height:16px;border-radius:8px;background:#40C484;border:none;"></div><div class="dp-dot p" style="width:16px;height:16px;border-radius:8px;background:#40C484;border:none;"></div><div class="dp-dot x" style="width:16px;height:16px;border-radius:8px;background:#F5A623;border:none;"></div>
              </div>
            </div>
            <div class="dp-legend" style="display:flex; gap:16px; margin-top:10px;">
              <div class="dp-leg-item" style="display:flex; align-items:center; gap:6px;"><div class="dp-leg-dot p" style="width:8px;height:8px;border-radius:50%;background:#40C484;"></div><span class="dp-leg-lbl" style="font-size:10px;color:#575757;font-weight:500;">Paid</span></div>
              <div class="dp-leg-item" style="display:flex; align-items:center; gap:6px;"><div class="dp-leg-dot x" style="width:8px;height:8px;border-radius:50%;background:#F5A623;"></div><span class="dp-leg-lbl" style="font-size:10px;color:#575757;font-weight:500;">Partial</span></div>
              <div class="dp-leg-item" style="display:flex; align-items:center; gap:6px;"><div class="dp-leg-dot m" style="width:8px;height:8px;border-radius:50%;background:#E5E7EB;border:1px solid rgba(0,0,0,0.05);"></div><span class="dp-leg-lbl" style="font-size:10px;color:#575757;font-weight:500;">Missed</span></div>
            </div>
          </div>
        </div>
        <div class="dp-tabs">
          <button class="dp-tab active" id="dp-tab-balance" onclick="dpSwitchTab('balance')">Balance</button>
          <button class="dp-tab" id="dp-tab-history" onclick="dpSwitchTab('history')">History</button>
        </div>
        <!-- Balance tab -->
        <div id="dp-content-balance" style="padding-bottom:100px;">
          <div class="dp-balance-card" style="background: url('Assets/balance.svg') no-repeat center/cover; padding: 24px 20px; border-radius: 24px; color: #fff; box-shadow:none; margin-bottom:24px;">
            <div class="dp-bal-lbl" style="color:#fff; font-size:14px; font-weight:500;">Cash in hand</div>
            <div class="dp-bal-row" style="margin-bottom:24px;"><span class="dp-bal-amt" style="font-size:36px; line-height:1.1;">10,450 <span style="font-size:20px;">Kz</span></span><span class="dp-bal-of" style="color:#fff; padding-bottom:6px;">of 50,000 Kz</span></div>
            <div class="dp-prog" style="background:rgba(255,255,255,0.3); height:6px;"><div class="dp-prog-fill" style="width:59%; background:#fff;"></div></div>
            <div class="dp-prog-foot" style="color:#fff; font-weight:500; font-size:12px; margin-top:8px;"><span>59% paid</span><span>161.500 Kz remaining</span></div>
          </div>
          <div class="dp-breakdown-lbl" style="font-size: 12px; font-weight: 600; color: #6E717C; margin-bottom: 12px; font-family: 'Gilroy', sans-serif; text-transform: uppercase;">BREAKDOWN BY PRODUCT</div>
          <div class="dp-prod-card" style="border-radius:24px;">
            <div class="dp-prod-head"><div class="dp-prod-ic" style="background:#E2F6F4; border-radius:12px;"><img src="Assets/smartphone.png" style="width:16px;"></div><div class="dp-prod-name">Smartphone Plan</div><div class="dp-prod-pill ok" style="background:#E2F6F4; color:#007B83;">On Track</div></div>
            <div class="dp-prod-mid" style="margin-top:16px;"><span class="dp-prod-amt" style="font-size:22px;">8,500 <small style="font-size:14px;color:#575757;">Kz</small></span><span class="dp-prod-due" style="font-weight:500; color:#575757;">Due 20 May</span></div>
            <div class="dp-prod-bar" style="margin-top:6px; background:#f0f0f0;"><div class="dp-prod-fill ok" style="width:65%; background:#4CE1D2;"></div></div>
            <div class="dp-prod-labels" style="color:#575757; font-weight:500;"><span>65% paid</span><span>Ends Jan 2027</span></div>
          </div>
          <div class="dp-prod-card" style="border-radius:24px;">
            <div class="dp-prod-head"><div class="dp-prod-ic" style="background:#E2F6F4; border-radius:12px;"><img src="Assets/bike.png" style="width:20px;"></div><div class="dp-prod-name">EV Bike Loan</div><div class="dp-prod-pill late" style="background:#FCE0E0; color:#D83C3C;">2 days late</div></div>
            <div class="dp-prod-mid" style="margin-top:16px;"><span class="dp-prod-amt" style="font-size:22px;">12,000 <small style="font-size:14px;color:#575757;">Kz</small></span><span class="dp-prod-due" style="font-weight:500; color:#575757;">Was due 12 May</span></div>
            <div class="dp-prod-bar" style="margin-top:6px; background:#f0f0f0;"><div class="dp-prod-fill late" style="width:40%; background:#EF3739;"></div></div>
            <div class="dp-prod-labels" style="color:#575757; font-weight:500;"><span>40% paid</span><span>Ends Aug 2027</span></div>
          </div>
        </div>
        <!-- History tab -->"""

    html = html[:start_idx] + new_content + html[end_idx:]

    # 3. Add the floating Issue Payment button right before the end of screen-driver-profile
    # Find the closing tag of screen-driver-profile. It ends at:
    # </div> <!-- /screen-driver-profile --> or next screen
    # Let's search for "<!-- ══ SCREEN 21" or the end of the div
    
    # We can inject it just before the `</div>` that precedes `<!-- ══ SCREEN 21: `
    
    inject_idx = html.find('<!-- ══ SCREEN 21')
    if inject_idx != -1:
        # Step back to the </div> tag before SCREEN 21
        last_div_idx = html.rfind('</div>', 0, inject_idx)
        
        btn_html = """
      <button class="issue-pay-btn" style="position:absolute; bottom:30px; left:50%; transform:translateX(-50%); background:#1D1E25; color:#fff; border-radius:30px; padding:16px 36px; font-size:16px; font-weight:600; font-family:'Gilroy',sans-serif; border:none; box-shadow:0 8px 24px rgba(0,0,0,0.25); z-index:10; white-space:nowrap;">Issue payment</button>
"""
        html = html[:last_div_idx] + btn_html + html[last_div_idx:]

    with open(filepath, 'w') as f:
        f.write(html)

update_file('index.html')
update_file('anda-pay-prototype.html')

print("Updated Driver Profile!")

