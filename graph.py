import matplotlib.pyplot as plt

heads = [2, 3, 5, 7]
losses = [0.8487, 0.7969, loss_for_head_5, loss_for_head_7]  # Replace with actual loss values

plt.plot(heads, losses)
plt.xlabel('Number of Heads')
plt.ylabel('Loss at Iteration 5000')
plt.title('Loss vs Number of Heads')
plt.savefig('figures/loss_vs_heads.png')