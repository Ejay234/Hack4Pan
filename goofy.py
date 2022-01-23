# importing regex and random
import re
import random


class GoofyBot:
    # potential negative input
    negative_responses = ("no", "nope", "nah", "naw", "song", "bruh",
                          "not thanks", "no thank you", "sorry", "n", "sing",)

    # potential positive input
    positive_responses = ("sure", "yeah", "down", "bet", "say less", "i'm down", "your cream", "fho sho",
                          "yes", "ok", "okay", "yee", "yea", "k", "kk", "y", "cream", "sundae", "ight", "yuh", "i guess")

    # words for exiting the program
    exit_commands = ("done", "quit", "exit", "goodbye", "bye", "later")

    # random easy questions
    easy_questions = (
        "What month of the year has 28 days? ",
        "What goes up but never goes down? ",
        "This has two answers but one is fine. What can you not eat during breakfast? ",
    )

    def __init__(self):
        self.riddles = {'easy_intent': r'.*\s*(lunch|dinner|all|age|every).*',
                        'mid_intent': r'.*\s*(five|5|table|fire).*',
                        'hard_intent': r'.*\s*(seven|7|silence|quiet|light|dark).*',
                        'extreme_intent': r'.*\s*(map|day|letter|night|e|E).*'
                        }

    # start of the program
    def greet(self):
        # name input
        self.name = input(
            "Howdy Goober! I'm your favorite undersea peanut, Goofy Goober!, What's your name? ")
        # ask to talk to him
        will_help = input(
            f"{self.name}! Do you want to answer some of me riddles,,,? ")
        if will_help in self.positive_responses:
            print("That's the way to being goofy! Alright we'll start nice and easy,,, ")
        # starts the chatting program
            self.chat()
        # exits program if reply is an exit command
        elif will_help in self.negative_responses:
            print("stay goofy,,,ig \U0001F923\U0001F923\U0001F923")
            return True

    # exits program
    def make_exit(self, reply):
        if reply in self.exit_commands:
            # says one of the random goodbyes
            responses = ("alright,,,I see how it is,,,bye.", "you're not goofy or a goober.",
                         "ight,,,imma head out. ")
            print(random.choice(responses))
            return True

    # the main chat
    def chat(self):
        # asks questions
        reply = input(random.choice(self.easy_questions)).lower()
        # checks to see if input was an exit command
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()

    # checks the reply and matchs it with a topic
    def match_reply(self, reply):
        for key, value in self.riddles.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'easy_intent':
                return self.progress_1()
            elif found_match and intent == 'mid_intent':
                return self.progress_2()
            elif found_match and intent == 'hard_intent':
                return self.progress_3()
            elif found_match and intent == 'extreme_intent':
                return self.win()
        self.fail()

    # progress function
    def progress_1(self):
        # progess to mid
        do_continue = input(
            "Wow, you did great goober,,,I'll give you a slighty harder level. Wanna to hit again, hehe? ").lower()
        if do_continue in self.positive_responses:
            return self.mid_level()
        else:
            self.give_up()

    def mid_level(self):
        # random medium questions
        mid_questions = (
            "Mary has four daughters, and each of her daughters has a brother. How many children does Mary have? ",
            "I need air to live but if I touch water I perish. What am I? ",
            "I have four legs but I'm not alive? "
        )
        return (random.choice(mid_questions))

    def progress_2(self):
        # progess to hard
        do_continue = input(
            "Wow, wasn't that fun! I'll give you a much harder level. Dare to hit again my goober, whaha? ").lower()
        if do_continue in self.positive_responses:
            return self.hard_level()
        else:
            self.give_up()

    def hard_level(self):
        # random hard questions
        hard_questions = (
            "I am an odd number. Take away a letter and I become even. What number am I? ",
            "What is so fragile that saying its name breaks it? ",
            "What can fill a room but takes up no space? ",
        )
        return random.choice(hard_questions)

    def progress_3(self):
        # progess to extreme
        do_continue = input(
            "Sussy,,,Sussy,,,Goober,,,well here's the final Riddle,,,ready? ").lower()
        if do_continue in self.positive_responses:
            return self.extreme_level()
        else:
            self.give_up()

    def extreme_level(self):
        # random extreme questions
        extreme_questions = (
            "You see me once in June, twice in November and not at all in May. What am I? ",
            "I have lakes with no water, mountains with no stone and cities with no buildings. What am I? ",
            "This has two answers but one is fine. What breaks yet never falls, and what falls yet never breaks? ",
        )
        return random.choice(extreme_questions)

    # failure to answer a corect answer
    def fail(self):
        failure_response = ("Lol,,,can never be me. So what? Again? ",
                            "EH,,,wrong! Round 2?", "Boohoo Goober, would you like to try again? ")
        loss = input(random.choice(failure_response))
        if loss in self.positive_responses:
            return self.chat()
        else:
            self.give_up()

    # given up function
    def give_up(self):
        given_up = ("alright,,,I see how it is,,,bye.", "you're not goofy or a goober.",
                    "ight,,,imma head out. ")
        print(random.choice(given_up))
        exit()

    # winner
    def win(self):
        print("You're a goofy goober, YEAH! Good job! You answered all my riddles. As a reward you get a little sundae cream from your favorite peanut, Goofy Goober! ")
        win = input(
            "Unless, you want me to sing,,, Do you want cream or a song as an award? ")
        if win in self.positive_responses:
            print("CREAMMY!")
            exit()
        elif win in self.negative_responses:
            return self.lyrics()
        else:
            exit()

    # lyrics to the song goofy goober!
    def lyrics(self):
        print("I'm a goofy goober! Rock! You're a goofy goober! Rock! We're all goofy goobers! Rock! Goofy goofy goober goober! Rock!")
        print("Put your toys away Well all I got to say when you tell me not to play I say no way! NO! No way, no, no freaking way! I'm a kid you say")
        print("When you say I'm a kid I say 'Say it again.' And then I say thanks! (Thanks) Thank you very much So if you're thinking that you'd like to be like me. Go ahead and try, the kid inside will set you free!")
        print(" Humala bebuhla zeebuhla boobuhla Humala bebuhla zeebuhla bop")
        print("I'm a goofy goober! Rock! You're a goofy goober! Rock! We're all goofy goobers! Rock! Goofy goofy goober goober! Yeah!")
        exit()


# Calls the bot
bot = GoofyBot()
bot.greet()
