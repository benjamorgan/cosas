import time
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from Modelos_TL_codes.load_data import load_data
from tensorflow.keras.preprocessing import image_dataset_from_directory


def train(modelo, base_dir, epoch, cp_callback, IMG_SIZE, seed, metodologia):
    train_dataset, validation_dataset, class_names = load_data(base_dir, IMG_SIZE, seed, metodologia) 
    print('start training')
    start_time = time.time()
    # Training the model
    
    history = modelo.fit(train_dataset,
                         epochs=epoch,
                         validation_data=validation_dataset,
                         callbacks=[cp_callback])

    end_time = time.time()
    print("--- Time taken to train : %s hours ---" % ((end_time - start_time) // 3600))
    # Freeze all the layers before the `fine_tune_at` layer

    return history

def final_train(modelo, base_dir, epoch, cp_callback, IMG_SIZE, seed, metodologia):
    train_dataset, class_names = final_load_data(base_dir, IMG_SIZE, metodologia) 
    print('start training')
    start_time = time.time()
    # Training the model
    
    history = modelo.fit(train_dataset,
                         epochs=epoch,
                         callbacks=[cp_callback])

    end_time = time.time()
    print("--- Time taken to train : %s hours ---" % ((end_time - start_time) // 3600))
    # Freeze all the layers before the `fine_tune_at` layer

    return history


def fine_tunning(modelo, base_dir, total_epoch, history, cp_callback, IMG_SIZE, seed):
    train_dataset, validation_dataset, class_names = load_data(base_dir, IMG_SIZE, seed)

    
    start_time = time.time()
    # Training the model
    history_fine = modelo.fit(train_dataset,
                              epochs=total_epoch,
                              validation_data=validation_dataset,
                              callbacks=[cp_callback],
                              initial_epoch=history.epoch[-1])

    end_time = time.time()
    print("--- Time taken to train : %s hours ---" % ((end_time - start_time) // 3600))
    # Freeze all the layers before the `fine_tune_at` layer

    return history_fine

def train_fusion(modelo, base_dir, epoch, cp_callback, seed, metodologia):
    IMG_SIZE = (248, 632)
    history = train(modelo, base_dir, epoch, cp_callback, IMG_SIZE, seed, metodologia)
    return history

