# main.py

from transform import transform_word
import json
import os

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# -------------------------------------------------------
# TEST DICTIONARY (word → expected_result) # 19 Case
# Load test cases from test1.json (expects a JSON object: { "word": "expected", ... })
try:
    here = os.path.dirname(__file__) or os.getcwd()
    with open(os.path.join(here, "test2.json"), "r", encoding="utf-8") as f:
        test_cases = json.load(f)
    if not isinstance(test_cases, dict):
        raise ValueError("test2.json must contain a JSON object mapping words to expected results")
except Exception as e:
    print(f"Warning: could not load test1.json: {e}")
    test_cases = {}

# -------------------------------------------------------
# FUNCTION THAT COMPARES LETTER-BY-LETTER
# -------------------------------------------------------
def color_compare(output, expected):
    colored = ""
    max_len = max(len(output), len(expected))

    for i in range(max_len):
        o = output[i] if i < len(output) else ""
        e = expected[i] if i < len(expected) else ""

        if o == e:
            colored += f"{GREEN}{o}{RESET}   "
        else:
            # If missing or mismatch: print expected in GREEN, wrong in RED
            colored += f"{RED}{o}{RESET}   "

    return colored

# -------------------------------------------------------
# MAIN TEST LOGIC
# -------------------------------------------------------
def run_tests():
    correct_count = 0
    wrong_results = []

    for word, expected in test_cases.items():
        result = transform_word(word)

        if expected in result: #if result == expected:
            correct_count += 1
        else:
            wrong_results.append((word, result, expected))

    # Print summary
    print("\n=======================")
    print("      TEST RESULTS     ")
    print("=======================")
    print(f"Total tests: {len(test_cases)}")
    print(f"Correct: {correct_count}")
    print(f"Incorrect: {len(wrong_results)}\n")

    if wrong_results:
        print("Incorrect Words (Green = correct letters, Red = wrong):\n")
        for word, output, expected in wrong_results:
            print(f"Input Word: {word}")
            print(f"Your Output : {color_compare(output, expected)}")
            print(f"Correct One: {expected}")
            print("-" * 40)

if __name__ == "__main__":
    run_tests()