import re
import sets
import copy
import random


def tree_to_regex(node):
    #print('SCORE   -   ', node.depth)
    if node.left:
        left = tree_to_regex(node.left)
    else:
        left = ""

    if node.right:
        right = tree_to_regex(node.right)
    else:
        right = ""

    if node.value == '_|_':
        string = left + '|' + right
    elif node.value == '__':
        string = left + right
    elif node.value == '(_)':
        string = '(' + left + ')'
    elif node.value == '[_]':
        string = '[' + left + ']'
    elif node.value == '{_}':
        string = '{' + left + '}'
    elif node.value == '{_,_}':
        string = '{' + left + ',' + right + '}'
    elif node.value == '[^_]':
        string = '[^' + left + ']'
    elif node.value == '^_$':
        string = '^' + left + '$'
    elif node.value == '(?=_)':
        string = '(?=' + left + ')'
    elif node.value == '(?!_)':
        string = '(?!' + left + ')'
    elif node.value == '(?<=_)':
        string = '(?<=' + left + ')'
    else:
        string = left + node.value.replace('_', '')

    return string
# end def tree_to_regex


def tree_to_list(node):
    list = [copy.deepcopy(node)]

    if node.left is not None:
        list.extend(tree_to_list(node.left))

    if node.right is not None:
        list.extend(tree_to_list(node.right))

    return list
# end def tree_to_list


def calc_score(tree, accept, reject):
    score = 0

    regex = tree_to_regex(tree)

    try:
        for word in accept:
            result = re.search(regex, word)
            if result:
                score += 1
    except:
        return -1000

    for word in reject:
        result = re.search(regex, word)
        if result:
            score -= 1
        else:
            score += 1

    return score
# end def check


def crossover(mate_1, mate_2):
    l1 = tree_to_list(mate_1)
    l2 = tree_to_list(mate_2)

    new = random.choice(l1)
    new.left = random.choice(l2)

    return new
# end def crossover


def tournament_selection(population, size):
    best = random.choice(population)[:]

    for i in range(size):
        new = random.choice(population)[:]
        a = tree_to_regex(new[0])
        b = tree_to_regex(best[0])

        if new[1] > best[1]:
            best = new[:]
        elif new[1] == best[1] and len(a) < len(b):
                best = new[:]

    return best
# end def selection


def mutate(node):
    chance = random.random()

    if chance > 0.8 or (node.left is None and node.right is None):
        node.value, num_children = sets.random_value()
    else:
        chance_2 = random.random()
        if chance_2 > 0.5:
            node.left = mutate(node.left)
        else:
            node.right = mutate(node.right)

    return node
# end def mutate
