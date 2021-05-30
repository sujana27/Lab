import math
from collections import Counter
import operator
import numpy as np
from node import Node
from tree import Tree


root = Node("C4.5", None, None, None)


def all_entropy(attribute_list):
    all = Counter(attribute_list)  #  propotion of class
    probability = []
    add = 0
    for i, j in all.items():
        probability.append(j / len(attribute_list))
    for p in probability:
        a = -p * math.log(p, 2)
        add = add + a
    return add

def information_gain(df, split_attribute_name, target_attribute_name, trace=0):

    total_entropy = all_entropy(df[target_attribute_name[0]])
    d = []
    df_split = df.groupby(split_attribute_name)
    for i, j in df_split:
        d.append(j)
    entropy_d = {}
    for i, j in df_split:
        entropy_d[i] = all_entropy(j['RISK'])

    remaining_entropy = 0
    for i, j in df_split:
        remaining_entropy = remaining_entropy + len(j) / len(df) * entropy_d[i]

    return total_entropy - remaining_entropy



class C45:
    def __init__(self):
        return 


    def c4_5(self, numOfnode, d, attributes, target_attribute, current_node):

        if numOfnode != 0:
            attribute_value = d[current_node.attribute]
            attribute_value = list(attribute_value)
            attribute_value = attribute_value[0]
            d.drop(current_node.attribute, inplace=True, axis=1)
            attributes.remove(current_node.attribute)

        dic = {}
        for i in range(0, len(attributes)):
            infoGain = information_gain(d, attributes[i], target_attribute)
            splitinfo = all_entropy(d[attributes[i]])
            # dic[smoke] = gainratio of smoke
            dic[attributes[i]] = infoGain / splitinfo
        i = 0
        dic2 = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

        if numOfnode == 0:
            global root
            root = Node(dic2[0][0], None, None, None)
            numOfnode = numOfnode + 1
            current_node = root
            dataset_split = d.groupby(current_node.attribute)
            for i, j in dataset_split:
                attribute_value = j[current_node.attribute]
                attribute_value = list(attribute_value)
                attribute_value = attribute_value[0]
                decision = j[target_attribute[0]]
                decision = np.array(decision)
                if len(np.unique(decision)) == 1:
                    current_node.children.append(Node(None, attribute_value, decision[0], None))
                    continue
                c4_5(numOfnode, j, attributes, target_attribute, current_node)
        else:
            array = []
            df_split = d.groupby(dic2[0][0])
            n = Node(dic2[0][0], attribute_value, None, None)
            current_node.children.append(n)
            current_node = n
            print(current_node.attribute)
            df_split = d.groupby(current_node.attribute)
            for i, j in df_split:
                
                attributes = j.columns
                attributes = list(attributes)
                attributes.remove(target_attribute[0])
                decision = j[target_attribute[0]]
                decision = np.array(decision)
                if len(np.unique(decision)) == 1:
                    current_node.children.append(Node(None, i, decision[0], None))
                    continue
                c4_5(numOfnode, j, attributes, target_attribute, current_node)



        print("C4.5 is implemented..........")
        print("\n................Tree Generate...............\n")
        #Tree Print
        final_root = Tree(current_node.attribute)
        p = 0
        df_split = d.groupby(current_node.attribute)
        child = {}
        ch = []
        for i, j in df_split:
            ch.append(i)
            decision = j[target_attribute[0]]
            decision = np.array(decision)
            if len(np.unique(decision)) == 1:
                child[i] = decision[0]
            
        
        final_root.children = [Tree(ch[0]), Tree(ch[1])]
        final_root.children[0].children = [Tree(child[ch[0]])]
        final_root.children[1].children = [Tree(child[ch[1]])]
        
        print(str(final_root))

        return root

        
        


    