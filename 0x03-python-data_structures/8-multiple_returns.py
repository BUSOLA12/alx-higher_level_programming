#!/usr/bin/python3

    def multiple_returns(sentence):
        if sentence == "":
            tuple_ = (0, None)
        return tuple_
        count = len(sentence)
        first_char = sentence[0]
        tuple_ = (count, first_char)
        return tuple_

