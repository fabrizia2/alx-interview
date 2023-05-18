# UTF-8 Validation

## 0-main.py

- The test file.

## 0-validate_utf8.py

If a byte is the start of a new character, we determine the number of bytes for that character based on the leading bits. The valid bit patterns for the start of a character are as follows:

* Single-byte character: Starts with "0"
* Two-byte character: Starts with "110"
* Three-byte character: Starts with "1110"
* Four-byte character: Starts with "11110"

If a byte doesn't match any of these valid bit patterns, it's an invalid byte for the start of a character, and we return False.

Finally, after iterating over all the bytes, we check if there are any remaining bytes that haven't been accounted for. If there are remaining bytes, it means the data set is incomplete and not a valid UTF-8 encoding, so we return False. Otherwise, we return True to indicate that the data set is a valid UTF-8 encoding.
