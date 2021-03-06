import Grid
import GridUtils
import numpy as np

import MeshExtraction
import SurfaceExtraction
import networkx as nx
import matplotlib.pyplot as plt

# grid = Grid.Grid()
# grid.make_grid([np.array([0.5, 1.5, 1.5])], 128)
# voxel = grid.insert_point([1.4, 2.4, 3])
# voxel = grid.insert_point([1.4, 2.4, 3])
# grid.set_occupied([1,1,1])
# GridUtils.refine_grid(grid, 256)
# print(voxel)
# init_phi = GridUtils.initial_phi(grid)
# GridUtils.diffusion(grid, init_phi)
# GridUtils.dilation(grid)
#
# graph = SurfaceExtraction.generate_graph(grid, init_phi, [], [])
# nx.draw(graph, with_labels=True, font_weight='bold')
# plt.show()
# print(SurfaceExtraction.calc_s_opt(graph))

grid = Grid.Grid()
grid.make_grid_from_file("bun000.ply", 128)

print("Create initial phi")
init_phi = GridUtils.initial_phi(grid)
print("Diffusion")
GridUtils.diffusion(grid, init_phi)
print("Dilation")
GridUtils.dilation(grid)

print("Generate Graph")
graph = SurfaceExtraction.generate_graph(grid, init_phi, [], [])

nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()

print("Calc S_opt")
s_opt, cut_edges = SurfaceExtraction.calc_s_opt(graph)


print(s_opt)

print("Extract Mesh")
mesh = MeshExtraction.extract_mesh(s_opt, cut_edges, grid)
