import tensorflow as tf
import numpy as np

# load model
reload_model = tf.keras.models.load_model("./rnn_text_model")

# take input and predict
sample_text = input("Please type your comment about this movie: \n")
predictions = reload_model.predict(np.array([sample_text]))
print(predictions[0])
