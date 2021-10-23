# 3.203 Generate a genome

import numpy as np

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
    return {}