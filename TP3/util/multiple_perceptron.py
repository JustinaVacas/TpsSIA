import time
import math

import numpy as np


class Neuron:
    def __init__(self, weights, activation_f):
        self.weights = weights
        self.activation_f = activation_f
        self.last_delta = 0
        self.last_excited = 0
        self.last_activation = 0
        if self.weights is not None:
            self.batch_delta_w = [0] * len(weights)
        self.last_delta_w = 0

    def adjustment(self, prev_layer_activations, learning_rate, momentum):
        adjustment = learning_rate * self.last_delta
        delta_w = adjustment * np.array(prev_layer_activations)
        if momentum:
            delta_w += 0.8 * self.last_delta_w
        self.weights += delta_w
        self.last_delta_w = delta_w

    def get_batch_delta_w(self, prev_layer_activations, learning_rate, momentum):
        delta_w = learning_rate * self.last_delta * np.array(prev_layer_activations)
        if momentum:
            delta_w += 0.8 * self.last_delta_w  # Usamos momentum = 0.8
        self.last_delta_w = delta_w
        return delta_w

    def batch_adjustment(self):
        self.weights += self.batch_delta_w
        self.batch_delta_w = [0] * len(self.weights)

    def get_activation(self, prev_layer_activations):
        excited_state = np.inner(prev_layer_activations, self.weights)
        self.last_excited = excited_state
        self.last_activation = self.activation_f(excited_state)
        return self.last_activation


class MultilayerPerceptron:
    def __init__(self, training_set, expected_output, learning_rate, hidden_layers, adaptive_eta_params, beta,
                 batch=False, momentum=False):
        self.LIMIT = 0.001
        self.training_set = np.array(list(map(lambda t: [1] + t, training_set)))  # add e0 = 1
        self.expected_output = expected_output
        self.adaptive_eta = adaptive_eta_params[0]
        self.adaptive_eta_increase = adaptive_eta_params[1]
        self.adaptive_eta_decrease = adaptive_eta_params[2]
        self.adaptive_eta_max_iterations = adaptive_eta_params[3]
        self.layers = [len(self.training_set[0])] + list(map(lambda units: units + 1, hidden_layers)) + [
            1]  # add one unit to each layer --> v0
        self.layers_amount = len(self.layers)
        self.learning_rate = learning_rate
        self.neurons = {0: [Neuron(None, self.activation_function) for i in range(self.layers[0])]}
        self.beta = beta
        self.batch = batch
        self.momentum = momentum

        # connect hidden_layer i con i+1
        for layer_i in range(1, self.layers_amount):  # initialize hidden layers weights
            self.neurons[layer_i] = []
            for i in range(self.layers[layer_i]):
                # El nodo umbral tienen siempre activacion 1 y no tiene pesos entrantes
                if i == 0 and layer_i != self.layers_amount - 1:
                    self.neurons[layer_i].append(
                        Neuron(None, self.activation_function))  # Neurona umbral no tiene pesos entrantes
                    self.neurons[layer_i][i].last_activation = 1
                else:
                    w = np.random.uniform(size=(self.layers[layer_i - 1]), low=-1, high=1)

                    self.neurons[layer_i].append(Neuron(w, self.activation_function))

    def activation_function(self, h):
        return np.tanh(self.beta * h)

    def deriv_activation_function(self, h):
        return self.beta * (1 - self.activation_function(h) ** 2)

    def train(self, epochs_amount):
        min_error = float('inf')
        aux_learning_rate = self.learning_rate

        start_time = time.process_time()
        for epoch in range(epochs_amount):
            aux_training = self.training_set.copy()
            aux_expected = self.expected_output.copy()
            k = 0
            acum_error = 0
            last_error = None
            if self.adaptive_eta:
                self.learning_rate = aux_learning_rate

            while len(aux_training) > 0:
                i_x = np.random.randint(0, len(aux_training))  # get random input
                expected = aux_expected[i_x]
                self.apply_input_to_layer_zero(aux_training[i_x])  # V0_k = Eu_k

                aux_training = np.delete(aux_training, i_x, axis=0)
                aux_expected = np.delete(aux_expected, i_x, axis=0)

                self.propagate()  # propagate activations

                last_layer_neurons = self.neurons[self.layers_amount - 1]  # calculate output layer delta
                for i in range(self.layers[-1]):
                    last_layer_neurons[i].last_delta = self.deriv_activation_function(
                        last_layer_neurons[i].last_excited) * (expected - last_layer_neurons[i].last_activation)

                self.back_propagate()  # backpropagate delta

                if self.batch:
                    self.accumulate_input_deltas()  # batch: accumulate delta_w until epoch is finished
                else:
                    self.update_weights()  # incremental: update each neuron weights every iteration

                aux_error = self.calculate_error(expected)
                acum_error += aux_error  # calculate error\

                # Compare errors for adaptive eta
                if self.adaptive_eta and last_error:
                    k = self.apply_adaptive_eta(aux_error, last_error, k)
                last_error = aux_error
            error = 0.5 * acum_error / len(self.training_set)

            if error < min_error:
                min_error = error

            if error < self.LIMIT:
                break
            if self.batch:  # new epoch --> update weights
                self.batch_update_weights()

        end_time = time.process_time()
        print('Training...')
        print("Epochs = ", epochs_amount)
        print("Time: " + str(end_time - start_time) + " s")
        print("Error_min = " + str(min_error))
        print('\n')

    # Cuando ya agarr?? el input, le asigno cada componente a el estado de activaci??n de cada unidad de la capa cero
    def apply_input_to_layer_zero(self, inputs):
        for i in range(len(inputs)):
            self.neurons[0][i].last_activation = inputs[i]

    # Calculo el estado de activaci??n para todas las neuronas de la red para el input que agarr??
    def propagate(self):
        # Empiezo desde la primera capa oculta
        for layer_i in range(1, self.layers_amount):  # V[m][i] = activations[layer][unit]

            neurons = self.neurons[layer_i]
            prev_layer_neurons = self.neurons[layer_i - 1]
            pln_activations = np.array(list(map(lambda n: n.last_activation, prev_layer_neurons)))

            for i in range(self.layers[layer_i]):
                # No propago en la neurona umbral
                if not (i == 0 and layer_i != self.layers_amount - 1):
                    neurons[i].get_activation(pln_activations)

    # Hago el camino inverso para calcular los deltas
    def back_propagate(self):
        #   Para calcular el delta de un nodo, necesitamos hacer la sumatoria de los weights que salen hacia un nodo * el delta de dicho nodo
        #   Empiezo desde la primera capa oculta

        for layer_i in range(self.layers_amount - 1, 1, -1):  # delta[layer][unit] voy desde M-1 hasta 2     e0 -- w --- V0
            neurons = self.neurons[layer_i - 1]
            upper_level_neurons = self.neurons[layer_i]
            # Si las neuronas del nivel superior estan en una capa oculta, saco el nodo umbral
            if layer_i != self.layers_amount - 1:
                upper_level_neurons = self.neurons[layer_i][1:]
            upper_deltas = [n.last_delta for n in upper_level_neurons]
            # No propago hacia atras sobre la neurona umbral --> solo tomo las neuronas no umbral de las capas ocultas
            for unit in range(1, self.layers[layer_i - 1]):
                deriv = self.deriv_activation_function(neurons[unit].last_excited)
                w = [n.weights[unit] for n in upper_level_neurons]
                inner = np.inner(w, upper_deltas)
                neurons[unit].last_delta = deriv * inner  # delta = g' * (expected - real) se calcula el delta de la capa de salida

    def update_weights(self):
        for layer_i in range(1, self.layers_amount):
            neurons = self.neurons[layer_i]
            prev_layer_neurons = self.neurons[layer_i - 1]
            pln_activations = np.array(list(map(lambda n: n.last_activation, prev_layer_neurons)))

            for unit in range(self.layers[layer_i]):
                if not (unit == 0 and layer_i != self.layers_amount - 1):  # Las neuronas umbral no tienen pesos
                    neurons[unit].adjustment(pln_activations, self.learning_rate, self.momentum)

    def batch_update_weights(self):
        for layer_i in range(1, self.layers_amount):
            for i in range(self.layers[layer_i]):
                # No propago en la neurona umbral
                if not (i == 0 and layer_i != self.layers_amount - 1):
                    self.neurons[layer_i][i].batch_adjustment()

    # Devuelve un array con todos los deltas_w de ese input y se lo tiene que sumar al array de accum_deltas
    def accumulate_input_deltas(self):
        for layer_i in range(1, self.layers_amount):
            neurons = self.neurons[layer_i]
            prev_layer_neurons = self.neurons[layer_i - 1]
            pln_activations = np.array(list(map(lambda n: n.last_activation, prev_layer_neurons)))

            for unit in range(self.layers[layer_i]):
                if not (unit == 0 and layer_i != self.layers_amount - 1):
                    delta_w = neurons[unit].get_batch_delta_w(pln_activations, self.learning_rate,
                                                              self.momentum)  # calculo TODOS los delta_w de la neurona
                    neurons[unit].batch_delta_w += delta_w

    def calculate_error(self, expected):
        # for i in range(len(self.training_set)):
        #     expected = self.expected_output[i]
        activation = self.neurons[self.layers_amount - 1][0].last_activation
        error = (expected - activation) ** 2
        return error

    def apply_adaptive_eta(self, error, last_error, k):
        if error < last_error:
            if k > 0:
                k = 0
            k -= 1
        elif error > last_error:
            if k < 0:
                k = 0
            k += 1
        else:
            k = 0
        if k == -self.adaptive_eta_max_iterations:  # decreci?? k veces seguidas --> aumento eta
            self.learning_rate += self.adaptive_eta_increase

        elif k == self.adaptive_eta_max_iterations:  # creci?? k veces seguidas --> diminuyo eta
            self.learning_rate -= self.adaptive_eta_decrease * self.learning_rate

        return k

    def get_output(self, inputs):
        aux_inputs = np.array(list(map(lambda t: [1] + t, inputs)))
        output = []
        for elem in aux_inputs:
            self.apply_input_to_layer_zero(elem)
            self.propagate()
            output.append([neuron.last_activation for neuron in self.neurons[self.layers_amount - 1]])

        return output
