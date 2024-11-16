import os
import pytest
from collections import namedtuple
from spliceai.utils import Annotator, get_delta_scores

Record = namedtuple('Record', ['chrom', 'pos', 'ref', 'alts'])

@pytest.fixture(scope='module')
def ann():
    fasta_path = os.path.join(os.path.dirname(__file__), 'data', 'test.fa')
    return Annotator(fasta_path, 'grch37')

@pytest.fixture(scope='module')
def ann_without_prefix():
    fasta_without_prefix_path = os.path.join(os.path.dirname(__file__), 'data', 'test_without_prefix.fa')
    return Annotator(fasta_without_prefix_path, 'grch37')

def test_get_delta_score_acceptor(ann, ann_without_prefix):
    record = Record('10', 94077, 'A', ['C'])
    expected_scores = ['C|TUBB8|0.15|0.27|0.00|0.05|89|-23|-267|193|0.52|0.67|0.98|0.71|0.00|0.00|0.13|0.08']
    scores = get_delta_scores(record, ann, 500, 0)
    assert scores == expected_scores
    scores = get_delta_scores(record, ann_without_prefix, 500, 0)
    assert scores == expected_scores

    record = Record('chr10', 94077, 'A', ['C'])
    scores = get_delta_scores(record, ann, 500, 0)
    assert scores == expected_scores
    scores = get_delta_scores(record, ann_without_prefix, 500, 0)
    assert scores == expected_scores

def test_get_delta_score_donor(ann, ann_without_prefix):
    record = Record('10', 94555, 'C', ['T'])
    expected_scores = ['T|TUBB8|0.01|0.18|0.15|0.62|-2|110|-190|0|0.00|0.01|0.97|0.79|0.56|0.71|0.99|0.36']
    scores = get_delta_scores(record, ann, 500, 0)
    assert scores == expected_scores
    scores = get_delta_scores(record, ann_without_prefix, 500, 0)
    assert scores == expected_scores

    record = Record('chr10', 94555, 'C', ['T'])
    scores = get_delta_scores(record, ann, 500, 0)
    assert scores == expected_scores
    scores = get_delta_scores(record, ann_without_prefix, 500, 0)
    assert scores == expected_scores
