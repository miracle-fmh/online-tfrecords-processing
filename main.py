import tensorflow as tf
import numpy as np
import os

def _parse_function(example_proto):
    ## update soon
    
def gen_parallel(keys):
    ## update soon

if __name__=="__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    filenames = ["./data/train.tfrecords-000","./data/train.tfrecords-001"]
    dataset = tf.contrib.data.TFRecordDataset(filenames)
    dataset = dataset.map(_parse_function)
    dataset = dataset.batch(80)
    dataset = dataset.repeat()
    iterator = dataset.make_initializable_iterator()
    images, labels = iterator.get_next()
    
    with tf.Session() as sess:
        
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        for i in range(10):
            ## generate the tfrecords
            ## update soon
            gen_parallel(keys)
            ##
            sess.run(iterator.initializer)
            ## read the generated tfrecords file
            for batch_index in range(300):
                batch_images,batch_labels = sess.run([images,labels])
    
    

