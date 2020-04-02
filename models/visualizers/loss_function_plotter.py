from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from matplotlib import pyplot

def kerasAnn(trainX, trainy, testX, testy, inputnn, outputnn):
    model = Sequential()
    model.add(Dense(inputnn, input_dim=20, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(outputnn, activation='linear'))
    opt = SGD(lr=0.01, momentum=0.9)
    model.compile(loss='mean_squared_error', optimizer=opt)
    # fit model
    history = model.fit(trainX, trainy, validation_data=(testX, testy), epochs=100, verbose=0)
    # evaluate the model
    train_mse = model.evaluate(trainX, trainy, verbose=0)
    test_mse = model.evaluate(testX, testy, verbose=0)
    print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))
    # plot loss during training
    pyplot.title('Loss / Mean Squared Error')
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()