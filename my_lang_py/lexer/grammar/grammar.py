class Grammar:
    def __init__(self) -> None:
        self.__grammar = {
            # Non terminals and terminals will be represented as a list of characters
            "non_terminals": list[str],
            "terminals": list[str],
            # Productions will be represented as a dict where the key is the non terminal and the value is a list of productions
            "productions": dict,
            "start_symbol": str,  # Simple capital letter
        }
        self.__file = "lexer/grammar/g1.txt"
        self.__read_from_file()

    def __read_from_file(self) -> None:
        with open(self.__file, "r") as file:
            current: str = ""
            for line in file.readlines():
                # Setting the current variable as the current section of the file
                # In case the line starts with a special character, otherwise it will be a production
                if line.startswith("N:"):
                    current = "non_terminals"
                    self.__grammar["non_terminals"] = list()
                    continue
                if line.startswith("T:"):
                    current = "terminals"
                    self.__grammar["terminals"] = list()
                    continue
                if line.startswith("P:"):
                    current = "productions"
                    self.__grammar["productions"] = dict()
                    continue
                if line.startswith("S:"):
                    current = "start_symbol"
                    continue

                # Reading the current section of the file
                match current: 
                    case "non_terminals":
                        self.__grammar["non_terminals"].append(line.strip())
                    case "terminals":
                        self.__grammar["terminals"].append(line.strip())
                    case "productions":
                        # Splitting the line into the non terminal and the productions
                        non_terminal, productions = line.strip().split("->")
                        # Splitting the productions into a list of productions
                        productions = productions.split("|")
                        # Adding the productions to the grammar
                        self.__grammar["productions"][non_terminal] = productions
                    case "start_symbol":
                        self.__grammar["start_symbol"] = line.strip()
                    case _:
                        raise Exception("Invalid file format")

    def cfg_check(self) -> bool:
        for key in self.__grammar["productions"]:
            if len(key) > 1:
                return False
        return True 

    def check_productions_for_terminal(self):
        key = "productions"
        while True:
            non_terminal:str = input("Input non-terminal(-1 for exit): ")
            if non_terminal == "-1":
                return
            print(f"{non_terminal} -> {self.__grammar[key][non_terminal]}")

    def print_grammar(self) -> None:
        for key, value in self.__grammar.items():
            if key == "productions":
                print(key)
                for key, value in value.items():
                    print(key, value)
                continue
            print(key, value)
