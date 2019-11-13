def turnOff(n,lights):
    # if number of lights is less than one
    if n < 1:
        return
    # if number of lights is greater or equal to one
    if n == 1:
        print("Turn off light", n)
        lights[n - 1] = 0
        print(lights)
    else:
        turnOff(n - 2, lights)
        print("Turn off light", n)
        lights[n - 1] = 0
        print(lights)
        turnOn(n - 2, lights)
        turnOff(n - 1, lights)


def turnOn(n, lights):
    # if number of lights is less than one
    if n < 1:
        return
    # if number of lights is 1
    if n == 1:
        print("Turn on light", n)         
        lights[n - 1] = 1
        print(lights)
    else:
        turnOn(n - 1, lights)
        turnOff(n - 2, lights)          
        print("Turn on light", n)
        lights[n - 1] = 1
        print(lights)
        turnOn(n - 2, lights)

def main():
    n = int(input("Please enter a number of lights: "))
    print()
    print("All lights are on")
    lights = [1] * n
    print(lights)

    turnOff(n, lights)
    # print("Number of steps", count)

if __name__ == "__main__":
    main()

'''
OUTPUT
--------

Please enter a number of lights: 3

All lights are on
[1, 1, 1]
Turn off light 1
[0, 1, 1]
Turn off light 3
[0, 1, 0]
Turn on light 1
[1, 1, 0]
Turn off light 2
[1, 0, 0]
Turn off light 1
[0, 0, 0]

'''
