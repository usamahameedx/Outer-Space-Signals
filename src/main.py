import string
from collections import Counter

# Step 1: Read file
with open("signal.txt", "r") as f:
    data = f.read()

# Allowed characters
valid_chars = set(string.ascii_uppercase + " ")

# Step 1.1: Extract the 721-char probable message
best_segment = ""
best_score = float('inf')

# English letter frequency (rough %)
english_freq_order = "ETAOINRSHU"
english_freq = {
    'E': 12.0, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'U': 2.8
}

for i in range(len(data) - 721):
    seg = data[i:i+721]
    if set(seg).issubset(valid_chars):
        counts = Counter(seg.replace(" ", ""))
        if counts:
            freq_list = [x[0] for x in counts.most_common(10)]
            # Score: mismatch with target top 10 letters
            score = sum(1 for a, b in zip(freq_list, english_freq_order) if a != b)
            if score < best_score:
                best_score = score
                best_segment = seg

cipher_text = best_segment

# Step 2: Frequency mapping
cipher_counts = Counter(cipher_text.replace(" ", ""))
most_common_cipher = [x[0] for x in cipher_counts.most_common(10)]

mapping = {}
for cipher_letter, plain_letter in zip(most_common_cipher, english_freq_order):
    mapping[cipher_letter] = plain_letter

# Fill unmapped letters with placeholders
for letter in string.ascii_uppercase:
    if letter not in mapping:
        mapping[letter] = "_"

# Step 3: Decode with initial guess
decoded = "".join(mapping.get(ch, ch) if ch != " " else " " for ch in cipher_text)

print("First 9 words:", " ".join(decoded.split()[:9]))
