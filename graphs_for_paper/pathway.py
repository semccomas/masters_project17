import matplotlib.pyplot as plt 

#names = ['synapse', 'cell junction', 'membrane', 'macromolecular complex', 'extracellular matrix', 'cell part', 'organelle', 'extracellular region']
colors = ['salmon', 'navajowhite','mediumseagreen', 'skyblue', 'sandybrown',  'blue', 'mediumorchid', 'steelblue',] #alpha or whatever? 
names = ['transporter activity' , 'translation regulation', 'catalytic activity', 'channel regulator', 'receptor activity', 'signal transductor', 'antioxidant activity', 'structural activity', 'binding']
#percentages = [0.004, 0.01, 0.125, 0.155, 0.012, 0.404, 0.25, 0.041]
percentages = [0.068, 0.009, 0.442, 0.002, 0.039, 0.01, 0.003, 0.075, 0.352]

plt.pie(percentages, startangle =90, colors = colors)
#plt.legend(names, loc = 'lower left', bbox_to_anchor = (0.59, -0.129))
#plt.bar(names, percentages)
plt.legend(names, loc = 'lower right', bbox_to_anchor = (0.31, -0.129))

plt.axis('equal')

plt.savefig('pathway_jejunum2.png', dpi = 600)
#plt.show()