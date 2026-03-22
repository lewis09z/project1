def xor_encode(webhook_url, key=0x55):
    return '/' + '/'.join(f"{ord(c) ^ key:02x}" for c in webhook_url)

webhook = ""  # thay vào đây
print(xor_encode(webhook))

