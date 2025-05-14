# Extracted headers and fields from the .eml file
subject = "The_Flag_We’ll_Capture_Together"
from_address = "ilovectfs19@waifu.club"
to_address = "idespisectfs14@memeware.net"
message_id = "94db41ae58ad070173fc571e2008de8b@waifu.club"
dkim_signature = """
v=1; a=rsa-sha256; c=relaxed/simple; d=waifu.club; s=mail;
t=1745339340; bh=HSq3Fk4UngoT3615kRTwX9TQfq9o0GNk3L5esFLg2e4=;
h=Date:From:To:Subject:From;
b=e65uxTcZ2s8RKde5x7GoMWDhM27qMUa2vpmCC6uPR/kCsC5Tl1lgVNCik9TBiIn7x
ThMSG0m17ElJR+eQ3IFACqhDjoJkCdLo+iYAwvx4Go1OOYUYRx7dn7tUisIKy2p7Ns
DjJMauF8H1fwIpO6kFZKUPiPescPp6mBJIWBOARUNxRSSReBJv+B8GibZJbN4c64c0
wOVpmrc1P3sGs/K1i8sjzcHVJyNdBBV2e71n5gJFfbo5EkM/HSmba8Vvfdg2BGkVaY
OriRs9vs5+XwV8v9stPhL48avJipOSz1ykfbXW3//QZYpAOGyQz8lhE2cek5YLJulB
yO/Pz8vtbkwjA==
b=V293LCB3aGF0IGEgYmVhdXRpZnVsIGxpdHRsZSBwb2VtLiBJIGFsbW9zdCBzaGVkI
 GEgdGVhciByZWFkaW5nIHRoYXQuIEhvcGVmdWxseSB5b3UgbGVhcm5lZCBtb3JlIGFi
 b3V0IGVtYWlsIGhlYWRlcnMuIEJ1dCBzZXJpb3VzbHksIGl0IGdldHMgbWUgd29uZGV
 yaW5nLi4uIGRvIHlvdSBsb3ZlIENURnMgYXMgbXVjaCBhcyB0aGV5IGRvPwoKQ0lUe2
 lfbDB2M19jdGYkX3QwMH0=
"""

# Function to try hashing different parts
fields_to_check = {
    "subject": subject,
    "from_address": from_address,
    "to_address": to_address,
    "message_id": message_id,
    "dkim_signature": dkim_signature
}

# Check each field separately
field_matches = {}
for field_name, content in fields_to_check.items():
    field_matches[field_name] = hashlib.sha256(content.encode('utf-8')).hexdigest() == provided_hash

field_matches

#結果
#{'subject': False,
# 'from_address': False,
# 'to_address': False,
# 'message_id': False,
# 'dkim_signature': False}
