
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from admin.common.models import ValueObject


class TensorFunction(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'

    def tf_function(self):
        mnist = tf.keras.datasets.mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_train, X_test = X_train / 255.0, X_test /255.0
        X_train = X_train[..., tf.newaxis]  # matrix [[]]로 표현 [ , ]도 가능.
        X_test = X_test[..., tf.newaxis]
        train_ds = tf.data.Dataset.from_tensor_slices(
            (X_train, y_train)
        ).shuffle(10000).batch(32)
        test_ds = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)
        plt.figure(figsize=(10,10))
        plt.imshow(train_ds[3])
        plt.savefig(f'{self.vo.context}train_ds.png')
        plt.imshow(test_ds[3])
        plt.savefig(f'{self.vo.context}test_ds.png')


class FashionClassification(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'
        self.class_name = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def fashion(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        # self.peek_datas(train_images, test_images, train_labels)
        model = keras.models.Sequential([
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(128, activation="relu"),  # neron count 128
            keras.layers.Dense(10, activation="softmax")  # 출력층 활성화함수는 softmax
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

            # keras.models. : 모듈
            # Sequential : 객체
        model.fit(train_images, train_labels, epochs = 5)
        # self.test_and_save_images(model, test_images, test_labels)
        model.save(f'{self.vo.context}fashion_classification.h5')


    def peek_datas(self, train_images, test_images, train_labels):
        print(train_images.shape)
        print(train_images.dtype)
        print(f'훈련 행: {train_images.shape[0]} 열: {train_images.shape[1]}')
        print(f'테스트 행: {test_images.shape[0]} 열: {test_images.shape[1]}')
        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False)
        plt.savefig(f'{self.vo.context}fashion_random.png')
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_name[train_labels[i]])
        plt.savefig(f'{self.vo.context}fashion_subplot.png')


    def test_and_save_images(self, model, test_images, test_labels):
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)  # verbose 는 학습하는 내부상황 보기 중 2번선택
        predictions = model.predict(test_images)
        i = 5
        print(f'모델이 예측한 값 : {np.argmax(predictions[1])}')
        print(f'정답: {test_labels[i]}')
        print(f'테스트 정확도: {test_acc}')
        plt.figure(figsize=(6, 3))
        plt.subplot(1, 2, 1)  # 1행 2열 1번째
        test_images, test_predictions, test_label = test_images[i], predictions[i], test_labels[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks(([]))
        plt.imshow(test_images, cmap=plt.cm.binary)
        test_pred = np.argmax(test_predictions)
        print(f'{test_pred}')
        print('#' * 100)
        print(f'{test_labels}')

        if test_pred == test_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} : {} %'.format(self.class_name[test_pred],
                                      100 * np.max(test_predictions),
                                      self.class_name[test_label], color))
        plt.subplot(1, 2, 2)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        this_plot = plt.bar(range(10), test_pred, color='#777777')
        plt.ylim([0, 1])
        test_pred = np.argmax(test_predictions)
        this_plot[test_pred].set_color('red')
        this_plot[test_label].set_color('blue')
        plt.savefig(f'{self.vo.context}fashion_answer2.png')

    '''
    def train_model(self, model, train_images, train_labels) -> object:
        model.fit(train_images, train_labels, epoch=5)
        return model

    def test_model(self, model, test_images, test_labels) -> object:
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
        # verbose 는 학습하는 내부상황 보기 중 2번 선택
        print(f'테스트 정확도 : {test_acc}')

    def predict(self, model, test_images, test_labels, index):
        prediction = model.predict(test_images)
        pred = prediction[index]
        answer = test_labels[index]
        print(f'모델이 예측한 값 {np.argmax(pred)}')
        print(f'정답 : {answer}')
        return model


    def plot_image(self):
        pass

    def plot_value_array(self):
        pass
    '''


class Perceptron(object):  # 퍼셉트론 분류기

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta  # float 학습률 (0.0과 1.0 사이)
        self.n_iter = n_iter  # int 훈련 데이터셋 반복 횟수
        self.random_state = random_state  # int 가중치 무작위 초기화를 위한 난수 생성기

    def fit(self, X, y) -> object:  # 훈련데이터 학습

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])  # 1d-array : 학습된 가중치
        self.errors_ = []  # list 에포크마다 누적된 분류 오류

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def predict(self, X):  # 단위 계단 함수를 사용하여 클래스 레이블 반환
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def net_input(self, X):  # 최종 입력 계산
        return np.dot(X, self.w_[1:]) + self.w_[0]


class AdalineGD(object):  # 적응형 선형 뉴런 분류기 # GD : Gradient Descent 경사 하강법

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        # X : {array-like}, shape = [n_samples, n_features]  X는 matrix, 파이썬에서 메트릭스는 다 데이터프레임
        #           n_samples 개의 샘플과 n_features 개의 특성으로 이루어진 훈련 데이터

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []  # 에포크마다 누적된 비용 함수의 제곱합

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            # Please note that the "activation" method has no effect
            # in the code since it is simply an identity function. We
            # could write `output = self.net_input(X)` directly instead.
            # The purpose of the activation is more conceptual, i.e.,
            # in the case of logistic regression (as we will see later),
            # we could change it to
            # a sigmoid function to implement a logistic regression classifier.
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return X

    def predict(self, X):  # 단위 계단 함수를 사용하여 클래스 레이블을 반환
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


class Calculator(object):

    def __init__(self):
        print(f'Tenserflow Version: {tf.__version__}')

    def process(self):
        print('*'*200)
        self.plus(4,8)
        print('*'*200)
        self.mean()

    def plus(self, a, b):
        print(tf.constant(a) + tf.constant(b))

    def mean(self):
        x_array = np.arange(18).reshape(3,2,3)
        x2 = tf.reshape(x_array, shape=(-1, 6)) # -1 은 그대로를 의미
        # 각 열의 합을 계산
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평군을 계산
        xmean = tf.reduce_mean(x2, axis=0)

        print(f'입력 크기: {x_array.shape} \n')
        print(f'크기가 변경된 입력 크기: \n{x2.numpy()}\n')
        print(f'열의 합: {xsum.numpy()}\n')
        print(f'열의 평균: {xmean.numpy()}\n')