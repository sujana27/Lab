from func3 import module3

class Perceptron:

    def __init__(self):
        return 


    def Single_Layer_Perceptron(self, dd, x1, x2):
        obj = module3()
        level = dd.columns
        bias = 1
        iterator = 0
        alpha = 1
        t = []
        # initial_weights = [10, 50, -20]     ######### c4.5, cart, bias
        initial_weights = [1, 1, 1]     ######### c4.5, cart, bias
        newlist = []
    

        for i in range(0, len(dd)):
            while 1:
                newlist = list(dd.iloc[i])
                yin, target = obj.neuron_fire(initial_weights, newlist, bias)
                y = obj.activation_function(yin)
                if y == target:
                    if i == 0:
                        print("\n\n###########    After the Iteration ", iterator, "    ##############")
                        print("present_Weights =>", initial_weights)
                        print("y[0] = ", y, " compared to actual output y = ", target)
                    print("Training with train_data_" + str(i+1) + ", weights have been adjusted")
                    if (i == len(dd)-1):
                        print("\nSucessfully Done!!!!!!!!!!!!!")
                    break
                else:
                    print("\n\n###########    Updates Weights after the Iteration ", iterator, "    #############")
                    print("present_Weights =>", initial_weights)
                    print("y[0] = ", y, " compared to actual output y = ", target)
                    print("not matching, weights need to be changed")
                    initial_weights[0] = initial_weights[0] + obj.change_in_weights(newlist[0], y, alpha, target)
                    initial_weights[1] = initial_weights[1] + obj.change_in_weights(newlist[1], y,  alpha, target)
                    initial_weights[2] = initial_weights[2] + obj.change_in_weights(bias, y, alpha, target)
                    iterator = iterator + 1


        final_result = obj.result(x1, x2, initial_weights)
        print("\n\n\nfinal result = ", final_result)
        print("Total Epoch = ", iterator+1)
        print("Updated Weight = ", initial_weights)
        final_result = obj.rev_assume(final_result)
        # print("\n\nfinal_result: \n\t\tThe RISK of heart disease is", final_result,"\n")
        return final_result