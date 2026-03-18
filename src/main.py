import gym
from fle.env.gym_env.action import Action

from fle.env.gym_env.registry import list_available_environments, get_environment_info

if __name__ == "__main__":
    env_ids = list_available_environments()
    print(f"Found {len(env_ids)} environments")

    for envId in env_ids:
        info = get_environment_info(envId)
        print(f"EnvName: {envId}")
        print(f"Description: {info['description']}\n\n")

# 3. Create the environment
env = gym.make("iron_ore_throughput", run_idx=0)

# 4. Use the environment
obs = env.reset(options={"game_state": None})
print(f"Initial observation keys: {list(obs.keys())}")

# 5. Take actions
current_state = None
for step in range(5):
    action = Action(agent_idx=0, game_state=current_state, code=f'print("Step {step}: Hello Factorio!")')
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    current_state = info["output_game_state"]
    print(f"Step {step}: Reward={reward}, Done={done}")

    if done:
        break

# 6. Clean up
env.close()
