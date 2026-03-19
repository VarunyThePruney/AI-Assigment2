def countvowels(text: str) -> int:
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

def reverse_string(text: str) -> str:
    return text[::-1]
