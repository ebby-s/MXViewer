from drawing import save_and_disp_png


# How is SE associated across address space?

# Parameters
# Widths of row and column addresses.
h_bits = 4
w_bits = 4
# Address bits used to associate with SE.
h_se_idx = [3,2,1,0]
w_se_idx = [3]
# Output file name.
filename = 'testout.png'
# Make image bigger if small address space.
mult = int(1) if max(h_bits, w_bits) > 7 else int(2**(8 - max(h_bits, w_bits)))


# Calculate colour steps.
r_step = int(255/2**len(h_se_idx))
b_step = int(255/2**len(w_se_idx))

# Split rows and columns by SE and colour them in.
r_map = [int(''.join([str(int((h_c&(1<<idx))!=0)) for idx in h_se_idx]),2)*r_step+r_step for h_c in range(2**h_bits)]
b_map = [int(''.join([str(int((w_c&(1<<idx))!=0)) for idx in w_se_idx]),2)*b_step+b_step for w_c in range(2**w_bits)]

# Create 2D array of pixel values, save and display as PNG.
data = [[(r_map[h_c], 0, b_map[w_c]) for w_c in range(2**w_bits) for i in range(mult)] for h_c in range(2**h_bits) for j in range(mult)]

save_and_disp_png(data, filename)





# Matmul for later
out_features = 4
in_features = 4
batch = 4






