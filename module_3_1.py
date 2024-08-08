calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    print(len(string), str.upper(string), str.lower(string))


def is_contains(string, list_to_search):
    count_calls()
    for z in range(len(list_to_search)):
        if str.casefold(string) == str.casefold(list_to_search[z]):
            return True
    else:
        return False


(string_info('Capybara'))
(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
