import matplotlib.pyplot as plt

heads = [2, 3, 5, 7]
losses = [0.7824, 0.7183, 0.6534, 0.6163]

plt.plot(heads, losses)
plt.xlabel('Number of Heads')
plt.ylabel('Loss at Iteration 5000')
plt.title('Loss vs Number of Heads')
plt.savefig('figures/loss_vs_heads.png')