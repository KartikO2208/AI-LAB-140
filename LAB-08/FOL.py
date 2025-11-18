import re

facts = set([
    "American(Robert)",
    "Enemy(A,America)",
    "Owns(A,T1)",
    "Missile(T1)"
])

rules = [
    {
        "if": ["American(p)", "Weapon(q)", "Sells(p,q,r)", "Hostile(r)"],
        "then": "Criminal(p)"
    },
    {
        "if": ["Missile(x)", "Owns(A,x)"],
        "then": "Sells(Robert,x,A)"
    },
    {
        "if": ["Missile(x)"],
        "then": "Weapon(x)"
    },
    {
        "if": ["Enemy(x,America)"],
        "then": "Hostile(x)"
    }
]

goal = "Criminal(Robert)"

def match(statement, fact):
    s_pred, s_args = statement.split("(")
    f_pred, f_args = fact.split("(")
    if s_pred != f_pred:
        return None
    s_args = s_args[:-1].split(",")
    f_args = f_args[:-1].split(",")
    if len(s_args) != len(f_args):
        return None
    subs = {}
    for s, f in zip(s_args, f_args):
        if s[0].islower():
            subs[s] = f
        elif s != f:
            return None
    return subs

def substitute(statement, subs):
    for var, val in subs.items():
        statement = re.sub(rf'\b{var}\b', val, statement)
    return statement

def forward_chain(facts, rules, goal):
    new_inferred = True
    while new_inferred:
        new_inferred = False
        for rule in rules:
            matched_facts = []
            possible_subs = []
            for cond in rule["if"]:
                for fact in facts:
                    subs = match(cond, fact)
                    if subs:
                        matched_facts.append(cond)
                        possible_subs.append(subs)
                        break
            if len(matched_facts) == len(rule["if"]):
                combined = {}
                for d in possible_subs:
                    combined.update(d)
                inferred = substitute(rule["then"], combined)
                if inferred not in facts:
                    print(f"Inferred: {inferred}")
                    facts.add(inferred)
                    new_inferred = True
                    if inferred == goal:
                        print(f"\n✅ Goal {goal} proved by Forward Chaining!")
                        return True
    print(f"\n❌ Goal {goal} cannot be proved with given facts.")
    return False

forward_chain(facts, rules, goal)
