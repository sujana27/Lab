class Node:

    def __init__(self, attribute: str, previous_attribute_value: str, decision: str, children: list):
        self.attribute = attribute
        self.decision = decision
        self.children = []
        self.previous_attribute_value = previous_attribute_value

    