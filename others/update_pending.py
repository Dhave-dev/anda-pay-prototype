import re

old_block = """        <!-- Pending deposit card -->
        <div class="hpnd-card">
          <div class="hpnd-card-label">Deposit under review</div>
          <span class="hpnd-amount-big">49,450 <span style="font-size:18px;font-weight:600;">Kz</span></span>
          <div class="hpnd-prog-wrap"><div class="hpnd-prog-fill"></div></div>
          <div class="hpnd-prog-labels"><span>Admin review in progress</span><span>Est. ~2hrs</span></div>
          <button class="hpnd-wait-btn">Waiting for confirmation</button>
        </div>"""

new_block = """        <!-- Pending deposit card -->
        <div class="hpnd-card-wrapper" style="position:absolute; top:130px; left:20px; width:335px; border-radius:24px; overflow:hidden;">
          <img src="Assets/Export card.svg" style="width:100%; display:block;">
        </div>"""

for filename in ['index.html', 'anda-pay-prototype.html']:
    with open(filename, 'r') as f:
        content = f.read()
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find block in {filename}")

