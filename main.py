from mnist import MNIST
from Network import Network

IMG_WIDTH = 28

mndata = MNIST('Resources')

images, labels = mndata.load_training()

# print(mndata.display(images[0]))
# print(labels[0])

network = Network([IMG_WIDTH * IMG_WIDTH])
network.setInput(list(reversed(images[2])))

network.print()