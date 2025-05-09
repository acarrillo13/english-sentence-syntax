from collections import deque, defaultdict

class PDA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.start_state = 'q0'
        self.start_symbol = 'S'
        self.transitions = self.define_transitions()
        self.terminals = {'noun', 'verb', 'det', 'adj', 'prep', 'conj', 'adv'}

    def define_transitions(self):
        transitions = defaultdict(list)

        #S
        transitions[('q1', 'S')].extend([
            ['NP', 'VP'],
            ['S', 'conj', 'S'],
            ['adv','S']
        ])

        #NP
        transitions[('q1', 'NP')].extend([
            ['noun'],
            ['det', 'noun'],
            ['det', 'AdjP', 'noun'],
            ['NP', 'PP'],
            ['NP', 'conj', 'NP']
        ])

        #VP
        transitions[('q1', 'VP')].extend([
            ['verb'],
            ['verb', 'NP'],
            ['verb', 'NP', 'PP'],
            ['verb', 'PP'],
            ['VP', 'conj', 'VP'],
            ['adv', 'VP'],
            ['VP', 'adv']
        ])

        #AdjP
        transitions[('q1', 'AdjP')].extend([
            ['adj'],
            ['adj', 'AdjP']
        ])

        #PP
        transitions[('q1', 'PP')].append(['prep', 'NP'])

        return transitions

    def accept_trace(self, input_string):
        input_tokens = input_string.strip().split()
        queue = deque()

        #initial start state
        queue.append(('q0', 0, [], [('q0', [])]))
        visited = set()

        while queue:
            state, pos, stack, trace = queue.popleft()

            key = (state, pos, tuple(stack[-5:]))
            if key in visited:
                continue
            visited.add(key)

            if state == 'q0':
                new_stack = stack.copy()
                new_stack.append('S')
                new_trace = trace + [('q1', new_stack.copy())]
                queue.append(('q1', pos, new_stack, new_trace))
                continue

            if not stack and pos == len(input_tokens):
                print("accept")
                for s, st in trace:
                    print(f"State: {s}, Stack: {st}")
                return True

            if not stack:
                continue

            top = stack.pop()

            if (state, top) in self.transitions:
                for production in self.transitions[(state, top)]:
                    new_stack = stack.copy()
                    for sym in reversed(production):
                        new_stack.append(sym)
                    new_trace = trace + [(state, new_stack.copy())]
                    queue.append((state, pos, new_stack, new_trace))

            elif pos < len(input_tokens) and top == input_tokens[pos]:
                new_trace = trace + [(state, stack.copy())]
                queue.append((state, pos + 1, stack.copy(), new_trace))

        print("reject")
        return False

#main
if __name__ == "__main__":
    user_input = input("Enter a space-separated string (e.g. 'det adj noun verb'):\n")
    pda = PDA()
    pda.accept_trace(user_input)