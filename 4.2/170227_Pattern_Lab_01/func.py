### used modules for C4.5 and CART


def module1(data, target_attribute):
        probability = []
        df_split = data.groupby(target_attribute)
        for i, j in df_split:
            probability.append(len(j) / len(data))
        return probability

class module:
    def __init__(self):
        return 

    def predict_C45_08(self, root, input):
        result = []
        for i in range(0, len(input)):
            current = root
            value = input[current.attribute][i]
            while (1):
                for i in range(0, len(current.children)):
                    temp = current.children[i].previous_attribute_value
                    if value == temp:
                        current = current.children[i]
                        break
                if current.decision != None:
                    result.append(current.decision)
                    break

        return result

    def predict_cart(self, root, input):
        result = []
        for i in range(0, len(input)):
            current = root
            value = input[current.attribute][i]
            while (1):
                for i in range(0, len(current.children)):
                    temp = current.children[i].previous_attribute_value
                    if value == temp[0]:
                        current = current.children[i]
                        break
                if current.decision != None:
                    if len(current.decision[0]) == 1:
                        result.append(current.decision)
                    else:
                        result.append(current.decision[0])
                    break

        return result


    def gini(self, data1, data2, attribute, target_attribute):
        g = 0

        target_prob1 = module1(data1, target_attribute)
        target_prob2 = module1(data2, target_attribute)

        t = 0
        for i in range(0, len(target_prob2)):
            t = t + target_prob2[i] * target_prob2[i]

            g = g + len(data2) / (len(data2) + len(data1)) * (1 - t)
            t = 0
        for i in range(0, len(target_prob1)):
            t = t + target_prob1[i] * target_prob1[i]

            g = g + len(data1) / (len(data2) + len(data1)) * (1 - t)

        return g

    