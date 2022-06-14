import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import json
import dataclasses
import os
import ast
from model_definition import build_model, FFN_Hyperparams, get_hyperparams

import random


def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error [MPG]')
    plt.legend()
    plt.grid(True)
    plt.show()


def train(model, train_data, valid_data=None, exp_dir='exp_00'):

    (x, y) = train_data

    # TODO define callbacks EarlyStopping, ModelCheckpoint, TensorBoard
    # my callbacks
    es_cbk = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=1000,
        restore_best_weights=True,
    )
    ckp_cbk = tf.keras.callbacks.ModelCheckpoint(
        os.path.join(exp_dir, "model_best_weights"),
        save_best_only=True,
        save_weights_only=True,
    )
    tb_cbk = tf.keras.callbacks.TensorBoard(exp_dir)

    # tensorboard --logdir=.

    # training
    if valid_data is None:
        history = model.fit(x=x, y=y, batch_size=64, validation_split=0.2,
                            epochs=250, verbose=1, callbacks=[es_cbk, ckp_cbk, tb_cbk])
    else:
        history = model.fit(x=x, y=y, batch_size=64, validation_data=valid_data,
                            epochs=250, verbose=1, callbacks=[es_cbk, ckp_cbk, tb_cbk])

    return model, history


def single_run(hp, train_data, experiment_dir, valid_data=None, verbose=True):

    if verbose:
        print(f"Training model with hyperparams: {hp}")

    os.makedirs(experiment_dir, exist_ok=True)

    #save hyperparams
    with open(os.path.join(experiment_dir, 'hp.json'), 'w') as f:
        json.dump(dataclasses.asdict(hp), f)

    # build model
    model = build_model(hp)

    if verbose:
        print(model.summary())

    # train model
    return train(model, train_data, valid_data=valid_data, exp_dir=experiment_dir)


def data_split(features, targets, valid_ratio=0.2):
    valid_mask = np.random.choice([False, True], features.shape[0], p=[1 - valid_ratio, valid_ratio])
    return (features[~valid_mask, :], targets[~valid_mask]), (features[valid_mask, :], targets[valid_mask])


def get_random_hp(constants):
    hidden_dims_len_range = [1, 3]
    hidden_dims_values_range = [10, 100]
    activation_fcn_choices = ['relu', 'tanh', 'sigmoid', 'elu', 'selu', 'softplus']
    lr_exponent_range = [-5, -1]

    hidden_dims_len = random.randint(hidden_dims_len_range[0], hidden_dims_len_range[1])
    hidden_dims = []
    for i in range(hidden_dims_len):
        hidden_dims.append(random.randint(hidden_dims_values_range[0], hidden_dims_values_range[1]))

    activation_fcn = random.choice(activation_fcn_choices)

    lr = 10 ** random.uniform(lr_exponent_range[0], lr_exponent_range[1])

    return FFN_Hyperparams(constants[0], constants[1], hidden_dims=hidden_dims,
                            activation_fcn=activation_fcn, learning_rate=lr)


def my_load_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()

    _train_features = []
    _train_targets = []
    for line in data:
        feature, target = line.split(':')
        feature = np.array(ast.literal_eval(feature))
        target = int(target)
        _train_features.append(feature)
        _train_targets.append(target)

    return np.array(_train_features), np.array(_train_targets)


if __name__ == '__main__':

    train_features, train_targets = my_load_data('train_data.txt')

    # print(train_features)
    # print(train_targets)

    experiment_dir = 'output'

    hp = get_hyperparams()

    _, history = single_run(hp, (train_features, train_targets), experiment_dir)
    plot_loss(history)
