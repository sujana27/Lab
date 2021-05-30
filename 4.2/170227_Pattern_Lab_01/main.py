import pandas as pd
from C4_5 import C45
from CART import cart
from func import module
from func3 import module3
from perceptron import Perceptron
import csv


if __name__ == '__main__':


    # dd = []
    # dd.append(['Rarely', 'False', 'True', 'No', ''])
    # dd.append(['Rarely', 'False', 'True', 'No', ''])
    # dd.append(['Rarely', 'False', 'True', 'No', ''])
    # dd.append(['Rarely', 'False', 'True', 'No', ''])
    
    # dd = pd.DataFrame(dd , columns=['EXERCISE', 'SMOKER', 'OBESE', 'FAMILY', 'Predicted_RISK'])
    # # saving the dataframe
    # dd = dd.to_csv("test_dataset.csv")

    base_train_filename = 'base_model_train_dataset.csv'
    meta_train_filename = 'meta_model_train_dataset.csv'
    test_filename = "test_dataset.csv"

    print("\n\n----------------------base_model_train_dataset---------------------------\n\n")
    base_input = pd.read_csv(base_train_filename)
    print(base_input)
    print("\n\n----------------------meta_model_train_dataset---------------------------\n\n")
    meta_input = pd.read_csv(meta_train_filename)
    print(meta_input)

    print("\n\n----------------------test_dataset---------------------------\n\n")

    # manually fixed input
    # input = [['rarely', 'False', 'true', 'no']]
    # test_data = pd.DataFrame(input,
    #                      columns=['EXERCISE', 'SMOKER', 'OBESE', 'FAMILY'])

    # # User input
    # a = input("EXERCISE = ")
    # b = input("SMOKER = ")
    # c = input("OBESE = ")
    # d = input("FAMILY = ")
    # input = [[a, b, c, d]]
    # test_data = pd.DataFrame(input,
    #                      columns=['EXERCISE', 'SMOKER', 'OBESE', 'FAMILY'])


    # Read Test Dataset from CSV
    test_data = pd.read_csv(test_filename)
    if 'PRED_RISK' in test_data.columns:
        test_data.drop(columns= ['PRED_RISK'])
    print(test_data)


    print("\n\n------------------------C4.5----------------------------\n\n")
    
    target_attribute = ['RISK']
    attribute = ["SMOKER", "EXERCISE", "OBESE", "FAMILY"]

    objC4_5 = C45()
    root = objC4_5.c4_5(0, base_input, attribute, target_attribute, None)
    tree1 = root
    
    objModule = module()

    print("### Prediction of C4.5 ###")
    x1 = objModule.predict_C45_08(tree1, test_data)
    print("Risk is:", x1)
    
    print("\n\n----------------------CART---------------------------\n\n")

    objCART = cart()
    root2 = objCART.Cart(0, base_input, attribute, target_attribute)
    tree2 = root2
    print("### Prediction of Cart ###")
    x2 = objModule.predict_cart(tree2, test_data)
    print("Risk is:", x2)
    
    objModule3 = module3()
    x1 = objModule3.assume(x1)
    x2 = objModule3.assume(x2)

    print("")
    print("\n\n------------------------PERCEPTRON--------------------------\n\n")
    objPerceptron = Perceptron()
    Predicted_risk = objPerceptron.Single_Layer_Perceptron(meta_input, x1, x2)
    
    test_data['PRED_RISK'] = Predicted_risk
    test_data.to_csv(test_filename, index = False)

    print("\n\nfinal_result: ")
    for i in range(0, len(Predicted_risk)):
        print("\t\tfor testdata_", i+1, ", The RISK of heart disease is ", Predicted_risk[i] + '.')