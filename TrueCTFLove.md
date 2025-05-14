# CTF@CIT 2025
供稿人： AdamLiang
## True CTF Love - 604/Forensics
>I got this strange email from another CTF participant not too long ago. I am just not sure what they mean by this...
>Do you love CTFs as much as they do?
>
>SHA256: 07cb654ce87444f158a52228848eb4eb501738913dfca44a2f227fb73ee9ed4b

>**檔案下載連結** [LINK](https://ctf.cyber-cit.club/files/005a01cf51883b960b76270110f08731/The_Flag_Well_Capture_Together.eml?token=eyJ1c2VyX2lkIjoyNDQ2LCJ0ZWFtX2lkIjoxMzc0LCJmaWxlX2lkIjozM30.aA8dEQ.biWsk91ij0_PR1sh4kHTWogSHZ4)

### Solution
>檢查 .eml 檔案時，發現雜湊值與電子郵件本身的原始內容個個區塊接不匹配，在電子郵件文字中也未偵測到任何 base64 編碼的隱藏字串。
<<<<<<< HEAD

>dig deeper into the email body for hidden clues (base64, steganography)?

>The full email body does NOT match the SHA256 hash you provided.

>No base64-encoded hidden strings were detected inside the email text.

>No decoded hidden message matched the hash either.

>Subject → no match

>From address → no match

>To address → no match

>Message-ID → no match

>DKIM-Signature → no match

>✅ None of these fields match the SHA256 hash you provided.

>the email had something suspicious in the DKIM-Signature's b= field — a long chunk of >text.

>It looks like this:

=======
>
>dig deeper into the email body for hidden clues (base64, steganography)?
>
>The full email body does NOT match the SHA256 hash you provided.
>
>No base64-encoded hidden strings were detected inside the email text.
>
>No decoded hidden message matched the hash either.
>
>Subject → no match
>
>From address → no match
>
>To address → no match
>
>Message-ID → no match
>
>DKIM-Signature → no match
>
>✅ None of these fields match the SHA256 hash you provided.
>
>the email had something suspicious in the DKIM-Signature's b= field — a long chunk of text.
>
>It looks like this:
>
>>>>>>> a8e6d1a774e5ce860ea1e49c22fcbb515b5dadc6
>>"V293LCB3aGF0IGEgYmVhdXRpZnVsIGxpdHRsZSBwb2VtLiBJIGFsbW9zdCBzaGVkI
 GEgdGVhciByZWFkaW5nIHRoYXQuIEhvcGVmdWxseSB5b3UgbGVhcm5lZCBtb3JlIGFi
 b3V0IGVtYWlsIGhlYWRlcnMuIEJ1dCBzZXJpb3VzbHksIGl0IGdldHMgbWUgd29uZGV
 yaW5nLi4uIGRvIHlvdSBsb3ZlIENURnMgYXMgbXVjaCBhcyB0aGV5IGRvPwoKQ0lUe2
 lfbDB2M19jdGYkX3QwMH0="
<<<<<<< HEAD

>That's base64 encoded! 🚀

>I'll decode that next — it might have hidden content!

>從.eml 文件中提取的標題和字段檢查DKIM-Signature的b=欄位發現是base64編碼，運用工具解析後內容如下

>Wow, what a beautiful little poem. I almost shed a tear reading that. Hopefully you learned more about email headers. But seriously, it gets me wondering... do you love CTFs as much as they do?

**CIT{i_l0v3_ctf$_t00}**

### Important:

>Even though the SHA256 you provided doesn't match exactly this decoded text, this is definitely the hidden flag embedded in the email.

>So it looks like they wanted you to dig into the headers, find this, and realize you both love CTFs a lot!
