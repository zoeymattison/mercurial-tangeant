inputs = [12,4]
weights = [0.5,-1]
bias = -0.5

sum = 0
for i in range(len(inputs)):
    sum += inputs[i] * weights[i]
sum += bias

def activate(sum):
    if sum > 0:
        return sum
    else:
        return 0

print(activate(sum))