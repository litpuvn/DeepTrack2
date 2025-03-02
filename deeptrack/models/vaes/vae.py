import tensorflow as tf
from tensorflow.keras import layers

from ..utils import as_KerasModel


@as_KerasModel
class VAE(tf.keras.Model):
    def __init__(self, encoder=None, decoder=None, latent_dim=2, **kwargs):
        super().__init__(**kwargs)

        # Dimensionality of the latent space
        self.latent_dim = latent_dim

        if encoder is None:
            self.encoder = self.default_encoder()

        if decoder is None:
            self.decoder = self.default_decoder()

    def train_step(self, data):

        data, _ = data

        with tf.GradientTape() as tape:
            # The encoder outputs the mean and log of the variance of the
            # Gaussian distribution. The log of the variance is computed
            # instead of the variance for numerical stability.
            z_mean, z_log_var = tf.split(self.encoder(data), 2, axis=1)

            # Sample a random point in the latent space
            epsilon = tf.random.normal(shape=tf.shape(z_mean))
            z = z_mean + tf.exp(0.5 * z_log_var) * epsilon

            # Reconstruct the input image
            rdata = self.decoder(z)

            # Reconstruction loss
            rloss = self.loss(data, rdata)

            # KL divergence loss
            kl_loss = -0.5 * (
                1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)
            )
            kl_loss = tf.reduce_mean(tf.reduce_sum(kl_loss, axis=1))

            # Total loss
            loss = rloss + kl_loss

        # Compute gradients
        grads = tape.gradient(loss, self.trainable_weights)

        # Update weights
        self.optimizer.apply_gradients(
            zip(grads, self.trainable_weights),
        )

        # Update metrics
        self.compiled_metrics.update_state(data, rdata)

        return {
            "loss": loss,
            "reconstruction_loss": rloss,
            "kl_loss": kl_loss,
        }

    def call(self, inputs):
        return self.encoder(inputs)

    def default_encoder(self):
        return tf.keras.Sequential(
            [
                tf.keras.Input(shape=(28, 28, 1)),
                layers.Conv2D(
                    32,
                    kernel_size=3,
                    strides=2,
                    padding="same",
                ),
                layers.LeakyReLU(alpha=0.2),
                layers.Conv2D(
                    64,
                    kernel_size=3,
                    strides=2,
                    padding="same",
                ),
                layers.LeakyReLU(alpha=0.2),
                layers.Flatten(),
                layers.Dense(16),
                layers.LeakyReLU(alpha=0.2),
                layers.Dense(
                    self.latent_dim + self.latent_dim, name="z_mean_log_var"
                ),
            ],
            name="encoder",
        )

    def default_decoder(self):
        return tf.keras.Sequential(
            [
                tf.keras.Input(shape=(self.latent_dim,)),
                layers.Dense(7 * 7 * 64),
                layers.LeakyReLU(alpha=0.2),
                layers.Reshape((7, 7, 64)),
                layers.Conv2DTranspose(
                    64,
                    kernel_size=3,
                    strides=2,
                    padding="same",
                ),
                layers.LeakyReLU(alpha=0.2),
                layers.Conv2DTranspose(
                    32,
                    kernel_size=3,
                    strides=2,
                    padding="same",
                ),
                layers.LeakyReLU(alpha=0.2),
                layers.Conv2D(
                    1,
                    kernel_size=3,
                    activation="sigmoid",
                    padding="same",
                ),
            ],
            name="decoder",
        )
