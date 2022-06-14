from dataclasses import dataclass
from typing import List
import tensorflow as tf
from tensorflow.keras import layers

@dataclass
class FFN_Hyperparams:
    # stale (zalezne od problemu)
    num_inputs: int
    num_outputs: int

    # do znalezienia optymalnych (np. metodą Random Search) [w komentarzu zakresy wartości, w których można szukać]
    hidden_dims: List[int]              # [10] -- [100, 100, 100]
    activation_fcn: str                 # wybor z listy, np: ['relu', 'tanh', 'sigmoid', 'elu', 'selu', 'softplus']
    learning_rate: float                # od 0.1 do 0.00001 (losowanie eksponensu 10**x, gdzie x in [-5, -1])


def get_hyperparams():
    return FFN_Hyperparams(num_inputs=25, num_outputs=1, hidden_dims=[25, 625, 25], activation_fcn='sigmoid',
                           learning_rate=0.01)


def build_model(hp: FFN_Hyperparams):

    model = tf.keras.Sequential()

    model.add(layers.Dense(hp.num_inputs, activation='relu', input_shape=[hp.num_inputs], name='ukryta_1'))

    for i, hidden_dim in enumerate(hp.hidden_dims):
        model.add(layers.Dense(hidden_dim, activation=hp.activation_fcn, name='ukryta_'+str(i+2)))

    model.add(layers.Dense(hp.num_outputs, name='wyjsciowa'))

    optimizer = tf.keras.optimizers.Adam(learning_rate=hp.learning_rate)

    model.compile(optimizer=optimizer, loss=tf.keras.losses.mse,
                  metrics=[tf.keras.metrics.mean_absolute_error, 'mse'])

    return model
