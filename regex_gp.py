import sets
import node
import utils
import random

WARMUP = [['afoot', 'catfoot', 'dogfoot', 'fanfoot', 'foody', 'foolery', 'foolish', 'fooster', 'footage', 'foothot',
           'footle', 'footpad', 'footway', 'hotfoot', 'jawfoot', 'mafoo', 'nonfood', 'padfoot', 'prefool', 'sfoot',
           'unfool'],
          ['Atlas', 'Aymoro', 'Iberic', 'Mahran', 'Ormazd', 'Silipan', 'altared', 'chandoo', 'crenel', 'crooked',
           'fardo', 'folksy', 'forest', 'hebamic', 'idgah', 'manlike', 'marly', 'palazzi', 'sixfold', 'tarrock',
           'unfold']]

STARS = [['A New Hope', 'Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones',
          'Revenge of the Sith', 'The Force Awakens'],
         ['The Wrath of Kahn', 'The Search for Spock', 'The Voyage Home', 'The Final Frontier',
          'The Undiscovered Country', 'Generations', 'First Contact', 'Insurrection', 'Nemesis', 'Into Darkness',
          'Beyond', 'Star Trek']]


def gen_individual(accept, reject):
    while True:
        ind = node.Node(depth=0, root=True)
        score = utils.calc_score(ind, accept, reject)

        if score != -1000:
            break

    return [ind, score]
# end def gen_individual


def gen_population(length, accept, reject):
    pop = []

    while len(pop) < length:
        pop.append(gen_individual(accept, reject))

    return pop
# end def gen_population


accept = STARS[0]
reject = STARS[1]

sets.build_terminal_set(accept, reject)
sets.build_function_set()

population = gen_population(1000, accept, reject)

bestest = gen_individual(accept, reject)
for i in range(100):
    best = ['fjkghdfkghdfkghsdkfhgksdfjhgksjdfhgkjsdhfgkjhsdfkghsdfkjghksdfhgkj', -9999]
    print("\nGeneration:", i)

    new_pop = []

    for _ in range(800):
        while True:
            try:
                m1 = utils.tournament_selection(population, 50)
                m2 = utils.tournament_selection(population, 50)
                child = utils.crossover(m1[0], m2[0])
                child = [child, utils.calc_score(child, accept, reject)]
                new_pop.append(child)
                break
            except:
                pass

    for _ in range(100):
        new_pop.append(gen_individual(accept, reject))

    for _ in range(100):
        while True:
            try:
                a = random.choice(population)
                b = utils.mutate(a[0])
                b = [b, utils.calc_score(b, accept, reject)]
                new_pop.append(b)
                break
            except:
                pass

    population = new_pop[:]

    for tree in population:
        ii = utils.tree_to_regex(tree[0])
        if tree[1] > best[1]:
            best = [ii, tree[1]]
        elif tree[1] == best[1]:
            if len(ii) < len(best[0]):
                best = [ii, tree[1]]

    for tree in population:
        if tree[1] > bestest[1]:
            bestest = tree[:]
        elif tree[1] == bestest[1]:
            a = utils.tree_to_regex(tree[0])
            b = utils.tree_to_regex(bestest[0])
            if len(a) < len(b):
                bestest = tree[:]

    population.append(bestest)

    print(best[0], '   -   ', best[1])
    print(utils.tree_to_regex(bestest[0]), '   -   ', bestest[1])
