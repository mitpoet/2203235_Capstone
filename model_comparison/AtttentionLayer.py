# AttentionLayer.py
import tensorflow as tf
from tensorflow.keras.layers import Layer
from tensorflow.keras.saving import register_keras_serializable

@register_keras_serializable(package='CustomLayers', name='AttentionLayer')
class AttentionLayer(Layer):
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.W = self.add_weight(name="att_weight", shape=(input_shape[-1], 1), initializer="normal")
        self.b = self.add_weight(name="att_bias", shape=(input_shape[1], 1), initializer="zeros")
        super(AttentionLayer, self).build(input_shape)

    def call(self, x):
        et = tf.nn.tanh(tf.matmul(x, self.W) + self.b)
        at = tf.nn.softmax(et, axis=1)
        output = x * at
        return tf.reduce_sum(output, axis=1)

    def get_config(self):
        config = super(AttentionLayer, self).get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)