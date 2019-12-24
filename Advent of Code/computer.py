import itertools
class Computer:

    def parse_opcode(self, intcode, index):
        code_with_params = str(intcode[index])
        opcode = int(code_with_params[-2:])
        params = []
        if opcode in [1,2,7,8]:
            params = [0] * 3
        elif opcode in [3,4]:
            params = [0] * 1
        elif opcode in [5,6]:
            params = [0] * 2
        for par, index in zip(code_with_params[-3::-1], itertools.count()):
            params[index] = int(par)
        return opcode, params


    def get_params(self, intcode, index, op):
        if op in [1,2,7,8]:
            return intcode[index + 1: index + 4]
        elif op in [3,4]:
            return intcode[index + 1:index + 2]
        elif op in [5,6]:
            return intcode[index + 1: index + 3]

    
    def solve(self,intcode):
        index = 0
        while intcode[index] != 99:
            try:
                op, param_modes = self.parse_opcode(intcode, index)
                parameters = self.get_params(intcode, index, op)
                #print(intcode[index], op, param_modes, parameters)
                if op == 1:
                    total = 0
                    for mode, val in zip(param_modes, parameters[:-1]):
                        total = total + val if mode == 1 else total + intcode[val]
                    intcode[parameters[-1]] = total
                    index += 4

                elif op == 2:
                    total = 1
                    for mode, val in zip(param_modes, parameters[:-1]):
                        total = total * val if mode == 1 else total * intcode[val]
                    intcode[parameters[-1]] = total
                    index += 4

                elif op == 3:
                    user_inp = int(input('Please enter an input'))
                    intcode[parameters[-1]] = user_inp
                    index += 2

                elif op == 4:
                    print(intcode[parameters[-1]]) if param_modes[-1] == 0 else print(parameters[-1])
                    index += 2
                
                elif op == 5:
                    val1 = intcode[parameters[0]] if param_modes[0] == 0 else parameters[0]
                    if val1 != 0:
                        index = intcode[parameters[-1]] if param_modes[-1] == 0 else parameters[-1]
                    else:
                        index += 3
                
                elif op == 6:
                    val1 = intcode[parameters[0]] if param_modes[0] == 0 else parameters[0]
                    if val1 == 0:
                        index = intcode[parameters[-1]] if param_modes[-1] == 0 else parameters[-1]
                    else:
                        index += 3

                elif op == 7:
                    val1 = intcode[parameters[0]] if param_modes[0] == 0 else parameters[0]
                    val2 = intcode[parameters[1]] if param_modes[1] == 0 else parameters[1]
                    if val1 < val2:
                        intcode[parameters[-1]] = 1
                    else:
                        intcode[parameters[-1]] = 0
                    index += 4

                elif op == 8:
                    val1 = intcode[parameters[0]] if param_modes[0] == 0 else parameters[0]
                    val2 = intcode[parameters[1]] if param_modes[1] == 0 else parameters[1]
                    if val1 == val2:
                        intcode[parameters[-1]] = 1
                    else:
                        intcode[parameters[-1]] = 0
                    index += 4

            except:
                print("ran into error")
                break

# Some test cases
test1 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
comp = Computer()
comp.solve(test1)