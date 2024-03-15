def look_and_say(n):
    res = ["1"]
    for _ in range(n - 1):
        current_term = res[-1]
        new_term = ""
        count = 1
        for i in range(1, len(current_term)):
            if current_term[i] == current_term[i - 1]:
                count += 1
            else:
                new_term += str(count) + current_term[i - 1]
                count = 1
        new_term += str(count) + current_term[-1]
        res.append(new_term)
    return res

# Generate and print the first 10 terms of the look and say sequence
n = 111221
look_and_say_sequence = look_and_say(n)
for i, term in enumerate(look_and_say_sequence):
    print(f"Term {i + 1}: {term}")
