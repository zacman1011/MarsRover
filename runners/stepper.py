from runners.runner import Runner


class Stepper(Runner):
    def run(self, instructions_list):
        # Assumption made that each list of instructions is the same length
        print("Running...")
        num_instructions = len(instructions_list)
        instructions_list_length = len(instructions_list[0])

        for instruction_index in range(instructions_list_length):
            print(self.board)
            print("\n")
            for rover_index, rover in enumerate(self.rovers):
                current_instruction = instructions_list[rover_index % num_instructions][instruction_index]
                rover.process(current_instruction)

        for rover in self.rovers:
            print(f"Final rover {rover}")
        print("Finished")
        print(self.board)
