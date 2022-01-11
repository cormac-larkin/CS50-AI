from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, but not both
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),

    # A claims to be both a knight and a knave, if this is true then he is a knight (we know this cannot be true)
    Biconditional(AKnight, And(AKnave, AKnight))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A & B are either knights or knaves, but not both
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnight, AKnave)),

    # A says they are both knaves, for this to be true, A would have to be both a knight and a knave at the same time (impossible)
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A & B are either knights or knaves, but not both
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnight, AKnave)),
    Biconditional(AKnave, BKnight),
    
    # If A is a knight, then both must be the same kind
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If B is a knight, then both must be of different kinds
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))


    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, C are all either knights or knaves
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),

    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnave, CKnight)),
    
    # If A claimed to be a knave, he would have to be both a knight and a knave for this to be true (impossible)
    Biconditional(AKnave, And(AKnight, AKnave)),

    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight),
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
