from dataclasses import dataclass
from typing import List
import tensorflow as tf
from tensorflow.keras import layers

@dataclass
class FFN_Hyperparams:
    num_inputs: int
    num_outputs: int

    hidden_dims: List[int]              # [10] -- [100, 100, 100]
    activation_fcn: str                 # 'relu', 'tanh', 'sigmoid', 'elu', 'selu', 'softplus'
    learning_rate: float                # od 0.1 do 0.00001


def get_hyperparams():
    return FFN_Hyperparams(num_inputs=25, num_outputs=1, hidden_dims=[25, 25],
                           activation_fcn='softmax', learning_rate=0.01)


def build_model(hp: FFN_Hyperparams):

    model = tf.keras.Sequential()

    model.add(layers.Dense(hp.num_inputs, activation=hp.activation_fcn, input_shape=[hp.num_inputs], name='ukryta_1'))

    for i, hidden_dim in enumerate(hp.hidden_dims):
        model.add(layers.Dense(hidden_dim, activation=hp.activation_fcn, name='ukryta_' + str(i + 2)))

    model.add(layers.Dense(hp.num_outputs, name='wyjsciowa'))

    optimizer = tf.keras.optimizers.Adam(learning_rate=hp.learning_rate)

    model.compile(optimizer=optimizer, loss=tf.keras.losses.mse,
                  metrics=[tf.keras.metrics.mean_absolute_error, 'mse'])

    return model
