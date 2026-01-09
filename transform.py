from mapping import two_letter_map, one_letter_map

def remove_consecutive_duplicates(word):
    if not word:
        return ""

    result = word[0]  # start with the first character
    for char in word[1:]:
        if char != result[-1]:
            result += char  # add only if different from previous
    return result

# ---------------------------------------------
# 1. Check TWO-LETTER mapping (priority)
# ---------------------------------------------
def handle_two_letters(word):
    # Start with one empty possibility
    results = [""]

    i = 0
    while i + 1 < len(word):
        new_results = []
        
        pair = word[i:i+2]

        # If this pair exists and produces ONE output
        if pair in two_letter_map and isinstance(two_letter_map[pair], str):
            for r in results:
                new_results.append(r + two_letter_map[pair])
            results = new_results

            # Update the 'word' variable for this pair
            word = word[:i] + two_letter_map[pair] + word[i+2:]
            print(word)

            i += 2
            continue

        # If pair exists and produces MULTIPLE outputs (list or tuple)
        if pair in two_letter_map and isinstance(two_letter_map[pair], (list, tuple)):
            for r in results:
                for out in two_letter_map[pair]:
                    new_results.append(r + out)
            results = new_results
            i += 2
            continue
        
        i += 1

    return results, word

def transform_word(word):
    word = remove_consecutive_duplicates(word.lower())

    # Start with one empty possibility
    #results, word = handle_two_letters(word) # [""]
    results = [""]
    print(word)
    i = 0
    while i < len(word):

        new_results = []

        # ------------------------------------------------
        # 2. Handle SINGLE-LETTER mapping
        # ------------------------------------------------
        char = word[i]

        # If char has ONE possible output
        if char in one_letter_map and isinstance(one_letter_map[char], str):
            for r in results:
                new_results.append(r + one_letter_map[char])

        # If char has MULTIPLE possible outputs
        elif char in one_letter_map and isinstance(one_letter_map[char], (list, tuple)):
            for r in results:
                for out in one_letter_map[char]:
                    new_results.append(r + out)

        # If char not found → keep it unchanged
        else:
            for r in results:
                new_results.append(r + char)

        results = new_results
        i += 1

    return results


# ------------------------------------------------------
# 3. TRANSFORMATION FUNCTION
#    (Two-letter pairs FIRST, then single letters)
# OLD
# ------------------------------------------------------
def transform_word_reture_one_word(word):
    word = word.lower()
    result = ""
    i = 0

    while i < len(word):
        # Check for two-letter match
        if i + 1 < len(word):
            pair = word[i:i+2]
            if pair in two_letter_map:
                result += two_letter_map[pair]
                i += 2
                continue

        # Fall back to one-letter map
        char = word[i]
        if char in one_letter_map:
            result += one_letter_map[char]
        else:
            result += char  # Keep unknown characters

        i += 1

    if word[-1] == 'a':
        result += 'ا'
    return result
