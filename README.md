# online-tfrecords-processing

If your tfrecord file is on-line generating during the training process, when using the tf.train.string_input_producer function to load the filenames into the filename_queue, the filename_queue will be closed when reading the tfrecords which are generating.

this code will show you how to read the tfrecords with the online-changing-processing.
