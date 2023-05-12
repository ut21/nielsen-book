# Neural Network and Deep Learning
Solutions of the examples from Michael Nielsen's book Neural Network and Deep Learning. Also a good use case to learn how to work with LaTeX files, so created the solution pdf using LaTeX.
## About the first chapter
The first chapter goes over perceptrons, and sigmoid (logistical) neurons. It discusess weights, activation functions, biases, inputs and outputs of the neurons and gives their mathematical formulations. It also goes over the formulation of percptron neurons as a type of NAND gate and uses the universality of NAND gates to extend the idea of using these neurons as logic gates. An especially insightful passage from the chapter is:
>The adder example demonstrates how a network of perceptrons can be used to simulate a circuit containing many NAND gates. And because NAND gates are universal for computation, it follows that perceptrons are also universal for computation.
The computational universality of perceptrons is simultaneously reassuring and disappointing. It's reassuring because it tells us that networks of perceptrons can be as powerful as any other computing device. But it's also disappointing, because it makes it seem as though perceptrons are merely a new type of NAND gate. That's hardly big news!
However, the situation is better than this view suggests. It turns out that we can devise learning algorithms which can automatically tune the weights and biases of a network of artificial neurons. This tuning happens in response to external stimuli, without direct intervention by a programmer. These learning algorithms enable us to use artificial neurons in a way which is radically different to conventional logic gates. Instead of explicitly laying out a circuit of NAND and other gates, our neural networks can simply learn to solve problems, sometimes problems where it would be extremely difficult to directly design a conventional circuit.

The chapter moves on to discuss the architectural heuristics of neural networks using the example of digit detection from hand written digits. 

Then the author begins discussion on **Cost Function** and **Gradient Descent** as a way of the net _learning_ which is just an optimisation problem given the smooth cost function. The author shows the necessary math for a two dimensional cost function then generalises the math for a cost function with _n_ inputs. **Stochastic Gradient Descent** is introduced as a way to decrease the training time of the net. 

The chapter ends with an implementation of a neural netwrok that detects hand written digits using MNIST training data
