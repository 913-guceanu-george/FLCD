from typing import List


class FiniteAutomaton:
    def __init__(self) -> None:
        self.__file: str = "C:\\Users\\maria\\Documents\\Code\\FLCD\\my_lang_py\\lexer\\finite_automaton\\FA.in"
        self.__fa: dict = self.__build_fa()

    def __open_file(self) -> List[str]:
        with open(self.__file, "r") as file:
            return file.readlines()

    def __menu(self) -> str:
        return f"We have the following FA:\n{str(self)}\n"

    def run(self) -> None:
        print(self.__menu())
        while True:
            user_input = input("Please enter a sequence(or 0 in case of exit): ")
            match user_input.strip():
                case "0":
                    break
                case _:
                    accepted = self.__is_seq_accepted(user_input)
                    if accepted:
                        print("Sequence accepted!")
                    else:
                        print("Sequence not accepted!")

    def __is_seq_accepted(self, sequence: str) -> bool:
        current_state: str = self.__fa["INITIAL STATE"][0]
        if sequence[0].isnumeric():
            current_state = sequence[0]
            print(f"Current state: {current_state} is not accepted!")
            return False
        build: str = ""
        for char in sequence:
            # Immediate conditions for not being accepted
            if current_state not in self.__fa["STATES"]:
                return False
            if char not in self.__fa["ALPHABET"].keys():
                current_state = char
                print(f"Current state: {current_state} is not accepted!")
                break
            if char.isnumeric():
                build += char
                current_state = self.__fa["STATES"][1]
                print(f"So far: {build}\nCurrent state: {current_state}\n")
                continue
            build += char
            current_state = self.__fa["STATES"][0]
            print(f"So far: {build}\nCurrent state: {current_state}\n")
        if current_state not in self.__fa["FINAL STATES"]:
            return False
        return True

    def __build_fa(self) -> dict:
        lines: List[str] = self.__open_file()
        fa: dict = {
            "INITIAL STATE": list(),
            "STATES": list(),
            "FINAL STATES": list(),
            "TRANSITIONS": list(),
            "ALPHABET": dict(),
        }
        index: int = 0
        last_matched: str = ""
        while index < len(lines):
            match lines[index].strip():
                case "INITIAL STATE":
                    last_matched = "INITIAL STATE"
                    index += 1
                case "STATES":
                    last_matched = "STATES"
                    index += 1
                case "FINAL STATES":
                    last_matched = "FINAL STATES"
                    index += 1
                case "TRANSITION FUNCTION":
                    last_matched = "TRANSITIONS"
                    index += 1
                case "ALPHABET":
                    last_matched = "ALPHABET"
                    index += 1
                case _:
                    last_matched = last_matched
            if last_matched == "ALPHABET":
                line = lines[index].strip().split()
                fa[last_matched][line[0]] = list()
                for i in range(1, len(line)):
                    if line[i] not in fa["TRANSITIONS"]:
                        raise ValueError(f"Invalid transition: {line[i]}")
                    fa[last_matched][line[0]].append(line[i])
                index += 1
                continue
            fa[last_matched].append(lines[index].strip())
            index += 1
        return fa

    def __str__(self) -> str:
        final_string: str = ""
        for key in self.__fa.keys():
            if key == "ALPHABET":
                final_string += (
                    f"{key}: {str(self.__fa[key].keys()).split('dict_keys')[1]}\n"
                )
                continue
            final_string += f"{key}: {self.__fa[key]}\n"
        return final_string
