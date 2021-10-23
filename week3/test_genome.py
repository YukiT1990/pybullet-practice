# 3.203 Generate a genome

import unittest
import genome
import numpy as np

class GenomeTest (unittest.TestCase):

  def testClassExists(self):
    self.assertIsNotNone(genome.Genome)

  def testRandomGene(self):
    self.assertIsNotNone(genome.Genome.get_random_gene)

  def testRandomGeneNotNone(self):
    self.assertIsNotNone(genome.Genome.get_random_gene(5))

  def testRandomGeneHasValues(self):
    gene = genome.Genome.get_random_gene(5)
    print(gene)
    self.assertIsNotNone(gene[0])

  def testRandomGeneLength(self):
    gene = genome.Genome.get_random_gene(20)
    self.assertEqual(len(gene), 20)

  def testRandomGeneIsNumpyArrays(self):
    gene = genome.Genome.get_random_gene(20)
    self.assertEqual(type(gene), np.ndarray)

  def testRandomGeneExists(self):
    data = genome.Genome.get_random_genome(20, 5)
    print(data)
    self.assertIsNotNone(data)

  def testGeneSpecExists(self):
    spec = genome.Genome.get_gene_spec()
    self.assertIsNotNone(spec)

unittest.main()