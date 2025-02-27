from amldl import (
    ADD,
    C,
    CMP,
    CV,
    Descriptor,
    F,
    INC,
    M,
    R,
    SOME,
)


def embedding():

    with Descriptor() as theEmbedding:
        n = 3
        C("label")  # label
        CV("black", n)  # black[0], black[1], black[2]
        CV("white", n)  # white[0], white[1], white[2]
        CMP("black", "white")  # black[i] and white[i] are complement for each i

        p = 0.05
        atLeastOne = False
        notAll = True
        x = SOME("black", p, atLeastOne, notAll)  # vector with some elements in black

        # The right term of the duple has some elements from black
        # and the elements in white that are not their complementary:
        # e.g.: {black[0], black[2], white[1]} or {black[0], white[1], white[2]}
        duples = INC("label", M(x, R("white", CMP(x))))
        ADD(duples)

        return {
            "constants": [el.const for el in F("constants pending transfer to algebra").r],
            "constantsNames": [el.key for el in F("constants pending transfer to algebra").r],
            "positiveDuples": [(el.rl_L.s, el.rl_H.s) for el in F("inclusions").r],
            "negativeDuples": [(el.rl_L.s, el.rl_H.s) for el in F("exclusions").r],
            "labels": [el.const for el in F("label").v],
            "blackConstants": [el.const for el in F("black").v],
            "whiteConstants": [el.const for el in F("white").v],
        }  # fmt:skip
