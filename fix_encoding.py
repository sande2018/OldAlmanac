import sys
data = open('app2.html', 'rb').read()
# Skip BOM if present
if data[:3] == b'\xef\xbb\xbf':
    data = data[3:]
# Read as UTF-8 (the garbled text)
text = data.decode('utf-8')
# Try to reverse the double-encoding: UTF-8 -> GBK bytes -> UTF-8
try:
    gbk_bytes = text.encode('gbk')
    original = gbk_bytes.decode('utf-8', errors='replace')
    open('app2.html', 'w', encoding='utf-8', newline='\r\n').write(original)
    print('Fixed! Written', len(original), 'chars')
except Exception as e:
    print('Error:', e)
    sys.exit(1)