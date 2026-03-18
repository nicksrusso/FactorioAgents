import random
import gymnasium


if __name__ == "__main__":
    env = gymnasium.make("CartPole-v1", render_mode="human")

    episodes = 10
    for ep in range(1, episodes):
        state, _ = env.reset()
        done = False
        score = 0
        while not done:
            act = random.choice([0, 1])
            observation, reward, terminated, truncated, info = env.step(act)
            done = terminated or truncated
            score += reward
            env.render()
            print(f"Episode: {ep}, Score: {score}")
