with open('index.html', 'r') as f:
    lines = f.readlines()

phone_close_idx = -1
for i, line in enumerate(lines):
    if "</div><!-- /phone -->" in line:
        phone_close_idx = i
        break

kb_start_idx = -1
kb_end_idx = -1
for i, line in enumerate(lines):
    if "<!-- ANDROID KEYBOARD -->" in line:
        kb_start_idx = i
    if kb_start_idx != -1 and "</div><!-- /app-shell -->" in line:
        kb_end_idx = i - 1
        break

if phone_close_idx != -1 and kb_start_idx != -1 and kb_end_idx != -1:
    kb_lines = lines[kb_start_idx:kb_end_idx+1]
    
    # Remove kb lines
    del lines[kb_start_idx:kb_end_idx+1]
    
    # Since we removed lines AFTER phone_close_idx, phone_close_idx is unchanged
    # Insert kb_lines before phone_close_idx
    lines = lines[:phone_close_idx] + kb_lines + lines[phone_close_idx:]
    
    with open('index.html', 'w') as f:
        f.writelines(lines)
    print("Fixed!")
else:
    print("Failed to find indices:", phone_close_idx, kb_start_idx, kb_end_idx)
