'''
The forward-chaining algorithm PL-FC-ENTAILS? (KB, q) determines if a single proposition
symbol q—the query—is entailed by a knowledge base of definite clauses. It begins from
known facts (positive literals) in the knowledge base. 
known facts (positive literals) in the knowledge base.

Reference: https://dl.ebooksworld.ir/books/Artificial.Intelligence.A.Modern.Approach.4th.Edition.Peter.Norvig.%20Stuart.Russell.Pearson.9780134610993.EBooksWorld.ir.pdf

'''

import re

def find_symbols_in_kb(knowledge_base: list[str]) -> dict:
    '''
    Find all unique symbols in the Knowledge_base
    :param knowledge_base: a list of string of definite clauses
    :returns: a dictionary with symbols as the keys their values are False
    '''

    inferred = {}

    for i in range(len(knowledge_base)):
        symbols = re.findall(r'[a-zA-Z]', knowledge_base[i])
        for symbol in symbols:
            if symbol not in inferred:
                inferred[symbol] = False

    return inferred


def number_of_symbols_in_premise(knowledge_base: list[str]) -> dict:

    '''
    Count the number of prposiotion symbols in each premise of KB clause
    :param knowledge_base: a list of string of definite clauses
    :returns: a dictionary with key as the premise of KB clause and value of count of symbols in the premise
    '''

    count = {}
    for clause in knowledge_base:
        if(len(clause) != 1):
            index = clause.find("=>")
            premise = clause[:index]
            letters = ''.join(e for e in premise if e.isalpha())
            count[premise] = len(letters)

    return count


def get_known_facts(knowledge_base: list[str]) -> list[str]:
    '''
    Get the known facts in KB
    :param knowledge_base: a list of string of definite clauses
    :returns: list of facts

    '''

    facts = []
    for clause in knowledge_base:
        if len(clause) == 1:
            facts.append(clause)

    return facts




def forward_chaining(knowledge_base: list[str], query:str) -> bool:
    ''' Forward chaining on Knowledge Base(KB) of definite clauses
    :param knowledge_base: a list of string of definite clauses
    :param query: a single proposition symbol that you are checking if it is entailed by the  KB
    :returns: If the query entailed by the KB or not?
    >>> forward_chaining([ "P => Q", "L & M => P", "B&L=> M", "A&P=>L", "A&B=>L", "A", "B" ], "Q")
    True
    >>> forward_chaining([ "P => Q", "L & M => P", "B&L=> M", "A&P=>L", "A&B=>L", "A", "B" ], "C")
    False

    '''

    count = number_of_symbols_in_premise(knowledge_base)
    inferred = find_symbols_in_kb(knowledge_base)
    queue = get_known_facts(knowledge_base)

    while(len(queue) > 0):
        p = queue.pop()
        if p == query: return True
        if not inferred[p]:
            inferred[p] = True
            for clause in knowledge_base:
                index = clause.find("=>")
                premise = clause[:index]
                if p in premise:
                    count[premise] -= 1
                    if count[premise] == 0:
                        queue.append(clause[-1])

    return False




KB = [
        "P => Q",
        "L & M => P",
        "B&L=> M",
        "A&P=>L", 
        "A&B=>L", 
        "A",
        "B" ]

'''
1)- KB must be written in horn form.
2)- It must be written as an implcaion whose 
2)- It must be written as an implcaion whose
its premise(head) must be conjunction of positive literals and its conclusion(body)
3)- It must contains facts about the world which are written as a single proposition symbol
'''
QUERY = "Q"

'''
Query is a signe proposition symbol that you check if it is entailed by the KB

'''

if __name__ == "__main__":

    

    import doctest

    doctest.testmod(verbose=True)
   

    result = forward_chaining(KB, QUERY)
    print(result)