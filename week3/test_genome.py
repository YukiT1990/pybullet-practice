# 3.203 Generate a genome
# 3.204 Genome spec
# 3.208 Gene to graph - implementation

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
    # print(gene)
    self.assertIsNotNone(gene[0])

  def testRandomGeneLength(self):
    gene = genome.Genome.get_random_gene(20)
    self.assertEqual(len(gene), 20)

  def testRandomGeneIsNumpyArrays(self):
    gene = genome.Genome.get_random_gene(20)
    self.assertEqual(type(gene), np.ndarray)

  def testRandomGeneExists(self):
    data = genome.Genome.get_random_genome(20, 5)
    # print(data)
    self.assertIsNotNone(data)

  def testGeneSpecExists(self):
    spec = genome.Genome.get_gene_spec()
    self.assertIsNotNone(spec)

  def testGeneSpecHasLinkLength(self):
    spec = genome.Genome.get_gene_spec()
    self.assertIsNotNone(spec['link-length'])

  def testGeneSpecHasLinkLength(self):
    spec = genome.Genome.get_gene_spec()
    # print(spec)
    self.assertIsNotNone(spec['link-length']["ind"])

  def testGeneSpecScale(self):
    spec = genome.Genome.get_gene_spec()
    gene = genome.Genome.get_random_gene(20)
    self.assertGreater(gene[spec["link-length"]["ind"]], 0)

  def testFlatLinks(self):
    links = [
      genome.URDFLink(name="A", parent_name=None, recur=1),
      genome.URDFLink(name="B", parent_name="A", recur=1),
      genome.URDFLink(name="C", parent_name="B", recur=1),
      genome.URDFLink(name="D", parent_name="C", recur=1)
    ]
    self.assertIsNotNone(links)

  def testExpandLinks(self):
    links = [
      genome.URDFLink(name="A", parent_name="None", recur=1),
      genome.URDFLink(name="B", parent_name="A", recur=1),
      genome.URDFLink(name="C", parent_name="B", recur=2),
      genome.URDFLink(name="D", parent_name="C", recur=1)
    ]
    exp_links = [links[0]]
    genome.Genome.expandLinks(links[0], links[0].name, links, exp_links)
    names = [l.name+"-parent-is-"+l.parent_name for l in exp_links]
    print(names)
    self.assertEqual(len(exp_links), 6)

unittest.main()