def words_sorting(*args):
    words_dict = {}
    result_str = []
    for word in args:
        if word not in words_dict:
            words_dict[word] = 0
            for ch in word:
                words_dict[word] += ord(ch)

    if not sum(words_dict.values()) % 2 == 0:
        for word in sorted(words_dict.items(), key=lambda x: -x[1]):
            result_str.append(f"{word[0]} - {word[1]}")
    else:
        for word in sorted(words_dict.items(), key=lambda x: x[0]):
            result_str.append(f"{word[0]} - {word[1]}")

    return "\n".join(result_str)


# Second variant (better)
# def words_sorting(*args):
#     def calculate_word_value(word):
#         return sum(ord(x) for x in word)
#
#     words_dict = {word: calculate_word_value(word) for word in args}
#
#     total_words_value = sum(words_dict.values())
#     if total_words_value % 2 == 0:
#         result = sorted(words_dict.items())
#     else:
#         result = sorted(words_dict.items(), key=lambda p: p[1], reverse=True)
#
#     return '\n'.join(f'{word} - {count}' for (word, count) in result)


# Author's solution
# def words_sorting(*args):
#     words = {word: sum(map(ord, word)) for word in args}
#     result_str = []
#
#     if not sum(words.values()) % 2 == 0:
#         for word in sorted(words.items(), key=lambda x: -x[1]):
#             result_str.append(f"{word[0]} - {word[1]}")
#     else:
#         for word in sorted(words.items(), key=lambda x: x[0]):
#             result_str.append(f"{word[0]} - {word[1]}")
#
#     return "\n".join(result_str)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
