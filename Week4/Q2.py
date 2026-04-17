# Lab 04: Loops and Functions Practice
# Student Name: [Tan Phat Nguyen]
# Date: [2/3/2026]


# ============================================
# Question 1: Robot Return to Origin
# ============================================
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None


def two_sum_optimized(numbers, target):
    num_list = {}
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in num_list:
            return (num_list[needed], i)
        num_list[numbers[i]] = i

# ============================================
# Question 3: Shuffle the Array
# ============================================

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    
    second_half = nums[n:]   

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])   
    # TODO: Loop through range(n) and append alternating elements

    return result



# ============================================
# Question 4: First Unique Character
# ============================================

def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:   
            counts[char] = 1
    return counts

def first_unique_character(s):
    char_count = count_characters(s)
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    return -1
#test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()
   
print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print() 

print("=== Question 3: Shuffle the Array ===")
test_cases_2 = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases_2:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()


    # Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()