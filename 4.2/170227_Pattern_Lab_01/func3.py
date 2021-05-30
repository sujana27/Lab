### used modules for perceptron


def activation_function(yin):
    if yin >= 0:
        return 1
    else:
        return 0

def neuron_fire_1(weight, input1, input2, bias):
    yin = 0
    yin = (weight[0] * input1) + (weight[1] * input2) + (weight[2] * bias)
    # for i in range(0, len(weight)-1):
    #     yin = yin + int(weight[i] * input[i]) + + int(weight[i] * input[i])
    # yin = yin + int(weight[i+1] * bias)
    return yin


class module3:

    def __init__(self):
        return 

    def rev_assume(self, x):
        s = []
        for i in x:
            if i == 0:
                s.append("low")
            else:
                s.append("high")
        return s

    def result(self, a, b, w):
        y = []
        bias = 1
        for i in range(0, len(a)):
            yin = neuron_fire_1(w, a[i], b[i], bias)
            y.append(activation_function(yin))
        return y

    def assume(self, x):
        a = []
        for i in x:
            if i == "low":
                a.append(0)
            else:
                a.append(1)
        return a

    def activation_function(self, yin):
        if yin >= 0:
            return 1
        else:
            return 0


    # ------------------------------------------------
    def change_in_weights(self, inputs, found, alpha, target):
        # w(n+1) = w(n) + alpha*[d(n) - y(n)]*x(n)
        delta_weight = alpha * (target - found) * inputs 
        return delta_weight


    # ------------------------------------------------
    def neuron_fire(self, weight, input, bias):
        yin = 0
        for i in range(0, len(input)-1):
            yin = yin + weight[i] * input[i]

        yin = yin + weight[i+1] * bias
        yin = int(yin)
        return yin, input[i+1]


    


