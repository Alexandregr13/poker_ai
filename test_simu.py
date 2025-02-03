import rlcard
from rlcard.agents.random_agent import RandomAgent

# Créer un environnement Texas Hold'em avec 6 joueurs
env = rlcard.make('no-limit-holdem', config={'game_num_players': 6})

# Créer 6 agents jouant de manière aléatoire
agents = [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players)]
env.set_agents(agents)

# Lancer une partie d'entraînement ou d'évaluation
trajectories, payoffs = env.run(is_training=False)

print("Trajectoires:", trajectories)
print("Résultats:", payoffs)
