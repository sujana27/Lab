import pandas as pd
import numpy as np
from node import Node
from tree import Tree
from func import module


root2 = Node("Hello", None, None, None)
objModule = module()
class cart:

    def Cart(self, numOfnode, d, a, target_a):
        attribute_value = []
        arr1 = []
        arr2 = []
        gini = []

        for i in range(0, len(a)):
            dataset_split = d.groupby(a[i])
            arr1 = []

            for j, k in dataset_split:
                arr1.append(k)
                arr2.append(j)

            for j in range(0, len(arr1)):
                data1 = arr1[j]
                data2 = []
                for k in range(0, len(arr1)):
                    if j != k:
                        data2.append(arr1[k])

                data2 = pd.concat(data2)
                if len(gini) == 0:
                    gini.append([a[i], arr2[j], objModule.gini(data1, data2, a[i], target_a)])
                    gini_data1 = data1
                    gini_data2 = data2
                elif objModule.gini(data1, data2, a[i], target_a) < gini[0][2]:
                    gini.clear()
                    gini.append([a[i], arr2[j], objModule.gini(data1, data2, a[i], target_a)])
                    gini_data1 = data1
                    gini_data2 = data2


        global root2
        root2 = Node(gini[0][0], None, None, None)
        current = root2
        attribute_value = gini_data1[current.attribute]
        attribute_value = list(attribute_value)
        attribute_value = np.unique(np.array(attribute_value))
        decision = gini_data1[target_a]
        decision = np.array(decision)
        if len(np.unique(decision)) == 1:
            current.children.append(Node(None, attribute_value, np.unique(decision)[0], None))

        attribute_value = gini_data2[current.attribute]
        attribute_value = list(attribute_value)
        attribute_value = np.unique(np.array(attribute_value))
        decision = gini_data2[target_a]
        decision = np.array(decision)
        if len(np.unique(decision)) == 1:
            current.children.append(Node(None, attribute_value, decision[0], None))

        
        
        print("CART is implemented..........")
        print("\n................Tree Generate...............\n")
        #Tree Print
        final_root = Tree(current.attribute)
        df_split = d.groupby(current.attribute)
        child = {}
        ch = []
        for i, j in df_split:
            ch.append(i)
            decision = j[target_a[0]]
            decision = np.array(decision)
            if len(np.unique(decision)) == 1:
                child[i] = decision[0]
            
        
        final_root.children = [Tree(ch[0]), Tree(ch[1])]
        final_root.children[0].children = [Tree(child[ch[0]])]
        final_root.children[1].children = [Tree(child[ch[1]])]
        
        print(str(final_root))
        return root2
        


