#My Solution
def valid_phone_number(phone_number):
    accepted_char = ['(',')','-',' ','1','2','3','4','5','6','7','8','9','0']
    if len(phone_number) == 14:
        if phone_number[0] == "(" and phone_number[4]==")" and phone_number[5] == " " and phone_number[9]=="-":
            for char in phone_number:
                if char not in accepted_char:
                    return False
                    break
                else:
                    continue
            return True
        else:
            return False
    else:
        return False
valid_phone_number("(123)456-7890")

#CodeWars #1 Soloution

def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))