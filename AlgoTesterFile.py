from math import ceil
word_array = ["1","12","123","1234","12345",
              "123456","1234567","12345678",
              "123456789","1234567890", "1234567891011"]

for part in word_array:
    new_text = ''
    if len(part) <= 3:
        new_part = ''
        new_part = f"<b>{part[0]}</b>"
        new_part += ''.join(part[1:])
        new_text += ' ' + new_part
    elif len(part) % 2 == 0:
        point = ceil(int(len(part) * 0.5))
        new_part = ''
        new_part = f"<b>{part[0:point]}</b>"
        new_part += ''.join(part[point:])
        new_text += ' ' + new_part 
    else:
        point = ceil(int(len(part) * 0.6))
        new_part = ''
        new_part = f"<b>{part[0:point]}</b>"
        new_part += ''.join(part[point:])
        new_text += ' ' + new_part 
    print(new_text)      