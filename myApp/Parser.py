

# This class is for parsing command strings
# for a string literal use
class Parser(object):

    commandLabel = ""
    argumentList = []

    def parseCommand(self, command: str):
        self.commandLabel = ""
        self.argumentList = []

        # in case of command with no arguments or (), ie: help
        if command.__contains__('(') == False:
            self.commandLabel = command
            return

        if command.__contains__(')') == False:
            self.commandLabel = command
            return

        # grab the command label
        self.commandLabel = command.split('(')[0]

        # find the index of the first '('
        index = command.index('(')

        # parse everything between ( ... )
        parameterStack = []
        i = index
        while True:

            if command[i] == '(':
                parameterStack.append('(')

            elif command[i] == ')':
                parameterStack.pop()

            # read literal argument
            elif command[i] == "[":
                literal = ""
                bracketStack = ['[']
                for j in range(i + 1, len(command)):
                    if command[j] == '[':
                        bracketStack.append('[')
                    if command[j] == ']':
                        bracketStack.pop()
                    if len(bracketStack) == 0:
                        j = j + 1
                        i = j
                        break
                    literal += command[j]

                self.argumentList.append(literal)

            elif command[i] == " ":
                pass

            # just record until ',' or ')' is found
            else:
                argument = ""
                for j in range(i, len(command)):

                    if command[j] == ')':
                        self.argumentList.append(argument)
                        i = j - 1
                        break

                    if command[j] == ',':
                        self.argumentList.append(argument)
                        i = j
                        break

                    argument += command[j]


            # quit if first '(' is closed with ')'
            if len(parameterStack) == 0:
                break
            i = i + 1

        return







