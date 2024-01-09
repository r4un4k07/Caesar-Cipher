universal_list_forward = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

universal_list_backward = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

type = input("encode or decode: ")

input_word = input("enter your word: ")

count = int(input("enter the number of jumps: "))

input_word_list = list(input_word)

current_position = 0

result = ''

if type == 'encode':
    for letter in input_word_list:
        letter_position = int(universal_list_forward.index(letter))
        if (25 - letter_position) < count:
            new_position = count - ((25 - letter_position) + 1)
            input_word_list[current_position] = universal_list_forward[new_position]
        else:
            input_word_list[current_position] = universal_list_forward[letter_position + count]
        current_position += 1
        
elif type == 'decode':
    for letter in input_word_list: 
        letter_position = int(universal_list_backward.index(letter))
        if (25 - letter_position) < count:
            new_position = count - ((25 - letter_position) + 1)
            input_word_list[current_position] = universal_list_backward[new_position]
        else:
            input_word_list[current_position] = universal_list_backward[letter_position + count]
        current_position += 1

for letter in input_word_list:
    result += letter
    
print(result)
            
