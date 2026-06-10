import re

for filename in ['index.html', 'anda-pay-prototype.html']:
    with open(filename, 'r') as f:
        content = f.read()
    
    old_kb = '.android-kb { position: absolute; bottom: 0; left: 0; width: 375px; height: 288px; background: #ebedf3; display: flex; flex-direction: column; transform: translateY(100%); transition: transform 0.25s cubic-bezier(0.2,0.8,0.2,1); z-index: 1000; padding: 6px 4px 10px; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }'
    new_kb = '.android-kb { position: absolute; bottom: 0; left: 0; width: 375px; height: 288px; background: #ebedf3; display: flex; flex-direction: column; transform: translateY(100%); transition: transform 0.25s cubic-bezier(0.2,0.8,0.2,1), visibility 0s 0.25s; z-index: 1000; padding: 6px 4px 10px; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; visibility: hidden; pointer-events: none; }'
    
    old_show = '.android-kb.show { transform: translateY(0); }'
    new_show = '.android-kb.show { transform: translateY(0); visibility: visible; pointer-events: auto; transition: transform 0.25s cubic-bezier(0.2,0.8,0.2,1), visibility 0s; }'
    
    if old_kb in content:
        content = content.replace(old_kb, new_kb)
        content = content.replace(old_show, new_show)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find block in {filename}")

