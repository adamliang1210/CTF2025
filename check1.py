import hashlib
import base64
import re

# Provided SHA256 hash
provided_hash = "07cb654ce87444f158a52228848eb4eb501738913dfca44a2f227fb73ee9ed4b"

# Extracted text from the email
email_body = """
My dearest one, whose heart I hold,
In your eyes, I see a world untold.
Where logic and riddles dance like stars,
But you, my love, stand behind bars.

I know you don’t share in my joy,
The flags I chase, the games I deploy.
You sigh, you frown, and often retreat,
While I dive into challenges, so sweet.

But, oh, my love, can you see?
These puzzles are not just code to me.
They’re like whispers from a distant shore,
A challenge to unlock, a path to explore.

I dream of the day when you’ll join the chase,
And feel the thrill of solving with grace.
Not because you have to, but because you’ll find,
The joy in puzzles that ignites your mind.

I won’t push, I won’t rush,
No, I’ll be gentle, soft as a hush.
But if you ever wish to see what I see,
I’ll be here, waiting, with a flag for you and me.

Together, we can solve what’s unknown,
In the world of CTFs, you won’t be alone.
Let’s take it slow, no need to fear,
For love is the answer, my darling, my dear.

So, when you're ready, just take my hand,
Let’s solve the puzzle, make our stand.
And who knows, perhaps you’ll see—
That even CTFs, too, can be love’s key.
"""

# Function to hash and compare text
def check_hash(content: str) -> bool:
    sha256 = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return sha256 == provided_hash

# Step 1: Check the whole email body
whole_body_match = check_hash(email_body.strip())

# Step 2: Find any base64-like strings in the email (for hidden messages)
base64_candidates = re.findall(r'[A-Za-z0-9+/=]{20,}', email_body)

# Step 3: Attempt decoding any base64 and checking hash
decoded_matches = []
for candidate in base64_candidates:
    try:
        decoded = base64.b64decode(candidate).decode('utf-8')
        if check_hash(decoded.strip()):
            decoded_matches.append((candidate, decoded))
    except Exception:
        pass

whole_body_match, base64_candidates, decoded_matches

