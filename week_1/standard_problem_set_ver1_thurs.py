def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))


def goldilocks_approved(nums):
    min_num, max_num = min(nums), max(nums)
    return next((num for num in nums if min_num < num < max_num), -1)

print(goldilocks_approved([3, 2, 1, 4]))
print(goldilocks_approved([1, 2]))
print(goldilocks_approved([2, 1, 3]))

def delete_minimum_elements(hunny_jars_sizes):
    new_list = []
    hunny_jar_sizes.sort()

    for ele in hunny_jar_sizes:
        new_list.append(ele)
        
    return new_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
        
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def final_value_after_operations(operations):
    final_sum = 1
    for i in range(len(operations)):
        if operations[i] in ["bouncy", "flouncy"]:
            final_sum +=1
        elif operations[i] == "trouncy" or operations == "pouncy":
            final_sum -=1
    return final_sum

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

def is_acronym(words, s):
    summer = 0
    for i in range(len(words)):
        if words[i][0].lower() == s[i].lower():
            summer +=1
    return summer == len(words)

words = ["christopher", "Robin", "milne"]
s = "crm"
print(is_acronym(words, s))

def make_divisible_by_3(nums):
    for ele in nums:
        req_ops = 0
        remainder = ele % 3

        if ele == 0:
            req_ops +=3
        elif remainder == 1:
            req_ops += 2
        elif remainder == 2:
            req_ops +=1
        
    return req_ops

nums1 = [1, 2, 3, 4]
print(make_divisible_by_3(nums1))

nums2 = [3, 6, 9]
print(make_divisible_by_3(nums2)) 