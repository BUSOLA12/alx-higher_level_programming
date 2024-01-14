#!/usr/bin/python3

    def multiple_returns(sentence):
        count = len(sentence)
        if count == 0:
            tuple_ = (count, None)
        return tuple_
        first_char = sentence[0]
        tuple_ = (count, first_char)
        return tuple_

