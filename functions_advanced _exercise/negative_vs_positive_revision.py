def find_positives_negatives(nums):   # or better use *args
    positives = [x for x in nums if x > 0]
    negatives = [x for x in nums if x < 0]
    positives_sum = sum(positives)
    negatives_sum = sum(negatives)

    if abs(negatives_sum) > (abs(positives_sum)):
        return f"{negatives_sum}\n{positives_sum}\nThe negatives are stronger than the positives"
    else:
        return f"{negatives_sum}\n{positives_sum}\nThe positives are stronger than the negatives"


numbers = [int(x) for x in input().split()]


print(find_positives_negatives(numbers))
