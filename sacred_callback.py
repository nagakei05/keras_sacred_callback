from keras.callbacks import Callback

class SacredTracker(Callback):
    """Callback that saves metrics to sacred metric API.
    # Arguments
        ARG_NAME : ARG_EXPLANATION 
            ARG_EXPLANATION
    # Raises
        SOMEError: explanation of the cause of error
    """

    def __init__(self, ex):
        super(SacredTracker self).__init__()
        self.ex = ex

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        for k in self.params['metrics']:
            if k in logs:
                self.ex.log_scalar(k, logs[k]))
