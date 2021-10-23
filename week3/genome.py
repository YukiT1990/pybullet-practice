# 3.203 Generate a genome
# 3.204 Genome spec
# 3.208 Gene to graph - implementation

import numpy as np
import copy

class Genome():
  @staticmethod
  def get_random_gene(length):
    gene = np.array([np.random.random() for i in range(length)])
    return gene

  @staticmethod
  def get_random_genome(gene_length, gene_count):
    genome = [Genome.get_random_gene(gene_length) for i in range(gene_count)]
    return genome

  @staticmethod
  def get_gene_spec():
    gene_spec = {
      "link-shape": {"scale": 1},
      "link-length": {"scale": 1},
      "link-radius": {"scale": 1},
      "link-recurrance": {"scale": 4},
      "link-mass": {"scale": 4},
      "joint-type": {"scale": 1},
      "joint-parent": {"scale": 1},
      "joint-axis-xyz": {"scale": 1},
      "joint-origin-rpy-1": {"scale": np.pi * 2},
      "joint-origin-rpy-2": {"scale": np.pi * 2},
      "joint-origin-rpy-3": {"scale": np.pi * 2},
      "joint-origin-xyz-1": {"scale": 1},
      "joint-origin-xyz-2": {"scale": 1},
      "joint-origin-xyz-3": {"scale": 1},
      "control-waveform": {"scale": 1},
      "control-amp": {"scale": 0.25},
      "control-freq": {"scale": 1},
      }
    ind = 0
    for key in gene_spec.keys():
      gene_spec[key]["ind"] = ind
      ind = ind + 1
    return gene_spec

  @staticmethod
  def expandLinks(parent_link, uniq_parent_name, flat_links, exp_links):
    children = [l for l in flat_links if l.parent_name == parent_link.name]
    for c in children:
      for r in range(c.recur):
        c_copy = copy.copy(c)
        c_copy.parent_name = uniq_parent_name
        uniq_name = c_copy.name + str(len(exp_links))
        c_copy.name = uniq_name
        exp_links.append(c_copy)
        Genome.expandLinks(c, uniq_name, flat_links, exp_links)



class URDFLink():
  def __init__(self, name, parent_name, recur):
    self.name = name
    self.parent_name = parent_name
    self.recur = recur
