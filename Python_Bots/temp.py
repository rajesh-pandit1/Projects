import platform
import numpy as np
import tensorflow as tf

@@ -18,12 +19,9 @@

from .tfutil import TfExpression, TfExpressionEx

try:
    # TensorFlow 1.13
    from tensorflow.python.ops import nccl_ops
except:
    # Older TensorFlow versions
    import tensorflow.contrib.nccl as nccl_ops
_collective_ops_warning_printed = False
_collective_ops_group_key       = 831766147
_collective_ops_instance_key    = 436340067