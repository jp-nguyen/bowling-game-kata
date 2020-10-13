class Game:
    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        game_score = 0
        frame_index = 0
        for frame in range(10):
            if (self.__is_strike(frame_index)):
                game_score += 10 + self.__strike_bonus(frame_index)
                frame_index += 1
            elif (self.__is_spare(frame_index)):
                game_score += 10 + self.__spare_bonus(frame_index)
                frame_index += 2
            else:
                game_score += self.__sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return game_score

    def __sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def __spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def __is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def __strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def __is_strike(self, frame_index):
        return self.rolls[frame_index] == 10
