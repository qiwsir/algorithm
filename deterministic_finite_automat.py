class State:
    def __init__(self, value: str, is_end: bool):
        self.value = value
        self.is_end = is_end


class Rule:
    def __init__(self):
        self.table = dict()

    def add_rule(self, input_character: str, current_state: State, target_state: State):
        self.table[(input_character, current_state)] = target_state

    def lookup_rule(self, input_character: str, current_state):
        return self.table[(input_character, current_state)]


class Graph:
    def __init__(self, rule: Rule, alphabet: list, start_state: State):
        self.rule = rule
        self.alphabet = alphabet
        self.current_state = start_state

    def is_valid(self, input_string: str) -> bool:
        temp = self.current_state
        for input_char in input_string:
            if input_char in self.alphabet:
                temp = self.rule.lookup_rule(input_char, temp)
            else:
                raise ValueError("State is not full")
        return temp.is_end


if __name__ == '__main__':
    q0 = State("q0", True)

    alphabet = ['0', '1']

    q1 = State("q1", False)
    q2 = State("q2", False)
    q3 = State("q3", False)
    rule = Rule()
    rule.add_rule("1", q0, q1)
    rule.add_rule("1", q1, q0)

    rule.add_rule("1", q2, q3)
    rule.add_rule("1", q3, q2)

    rule.add_rule("0", q0, q2)
    rule.add_rule("0", q2, q0)

    rule.add_rule("0", q0, q1)
    rule.add_rule("0", q1, q0)

    graph = Graph(rule, alphabet, q0)
    line = input("Please enter a string: ")
    print(graph.is_valid(line))
