

if __name__ == '__main__':
    
    outer = []

    with open('data/day3_data.txt') as file:
        inner = []
        for line in file:
            for char in line:
                if char != '\n':
                    inner.append(int(char))
            outer.append(inner.copy())
            inner.clear()


    most_freq = []
    for i in range(len(outer[0])):
        columns = [item[i] for item in outer]
        most_freq.append(max(set(columns), key=columns.count))
        columns.clear()

    
    most_freq = most_freq[::-1]

    gamma_rate = 0
    for i, elem in enumerate(most_freq):
        gamma_rate += elem * int(pow(2, i))


    least_freq = []
    for i in range(len(outer[0])):
        columns = [item[i] for item in outer]
        least_freq.append(min(set(columns), key=columns.count))
        columns.clear()

    least_freq = least_freq[::-1]

    epsilon_rate = 0
    for i, elem in enumerate(least_freq):
        epsilon_rate += elem * int(pow(2, i))

    print(gamma_rate * epsilon_rate)







