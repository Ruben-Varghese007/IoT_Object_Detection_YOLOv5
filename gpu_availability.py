# Checks if a CUDA-compatible GPU is available on the system.
# Retrieves the number of GPUs present.
# Prints the name of the first GPU (device 0) if available.

import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))