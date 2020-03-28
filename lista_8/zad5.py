def look_and_say(number):
    answer = []
    counter = 0
    tmp = number[0]
    for idx in range(0, len(number)):
        if tmp == number[idx]:
            counter += 1
        else:
            answer.append(('{}{}'.format(counter, tmp)))
            tmp = number[idx]
            counter = 1
    answer.append(('{}{}'.format(counter, tmp)))
    return answer


if __name__ == '__main__':
    print(look_and_say([1, 2, 1, 1]))
