import tensorflow as tf

class GeneratoreFrasi:

    def __init__(self, model_path) -> None:
        self.one_step_model = tf.saved_model.load(model_path)
    pass

    def frase(self, length):
        states = None
        next_char = tf.constant(['. '])
        result = []

        for n in range(length):
            next_char, states = self.one_step_model.generate_one_step(next_char, states=states)
            result.append(next_char)
        
        return tf.strings.join(result)[0].numpy().decode("utf-8")


generatore = GeneratoreFrasi('Modelli\one_step')
print("\n\n")
print(generatore.frase(100))