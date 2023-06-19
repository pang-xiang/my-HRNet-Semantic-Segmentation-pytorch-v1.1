
input = 16

kernel_size = 16
stride=8
padding=4
output_padding = 7
output = (input-1)*stride + output_padding -2*padding + kernel_size
print(output)