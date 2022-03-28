"""
Testing
=======

General guidelines for writing good tests:

- doctests always assume ``import networkx as nx`` so don't add that
- prefer pytest fixtures over classes with setup methods.
- use the ``@pytest.mark.parametrize``  decorator
- use ``pytest.importorskip`` for numpy, scipy, pandas, and matplotlib b/c of PyPy.
  and add the module to the relevant entries below.

"""
import pytest
import networkx
import sys
import warnings


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


# TODO: The warnings below need to be dealt with, but for now we silence them.
@pytest.fixture(autouse=True)
def set_warnings():
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="k_nearest_neighbors"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="numeric_mixing_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message=r"Ordered.* is deprecated"
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="literal_stringizer is deprecated",
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="literal_destringizer is deprecated",
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="is_string_like is deprecated"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="\nauthority_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="\nhub_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="default_opener is deprecated"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="empty_generator is deprecated"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="make_str is deprecated"
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="generate_unique_node is deprecated",
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="context manager reversed is deprecated",
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="This will return a generator in 3.0*",
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="betweenness_centrality_source"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="edge_betweeness"
    )
    warnings.filterwarnings(
        "ignore", category=PendingDeprecationWarning, message="the matrix subclass"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="to_numpy_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="from_numpy_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="networkx.pagerank_numpy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="networkx.pagerank_scipy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="write_gpickle"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="read_gpickle"
    )
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="write_shp")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="read_shp")
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="edges_from_line"
    )
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="write_yaml")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="read_yaml")
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="FilterAtlas.copy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="FilterAdjacency.copy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="FilterMultiAdjacency.copy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="FilterMultiInner.copy"
    )
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="jit_data")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="jit_graph")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="consume")
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="iterable is deprecated"
    )
    warnings.filterwarnings(
        "ignore",
        category=FutureWarning,
        message="\nThe function signature for cytoscape",
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="\nThe `attrs` keyword"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="preserve_random_state"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="`almost_equal`"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="`assert_nodes_equal`"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="`assert_edges_equal`"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="`assert_graphs_equal`"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="networkx.hits_scipy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="networkx.hits_numpy"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="preserve_random_state"
    )
    warnings.filterwarnings(
        "ignore",
        category=FutureWarning,
        message="google_matrix will return an np.ndarray instead of a np.matrix",
    )
    ### Future warnings from scipy.sparse array transition
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="biadjacency_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="bethe_hessian_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="incidence_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="laplacian_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="normalized_laplacian_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="directed_laplacian_matrix"
    )
    warnings.filterwarnings(
        "ignore",
        category=FutureWarning,
        message="directed_combinatorial_laplacian_matrix",
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="modularity_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="directed_modularity_matrix"
    )
    warnings.filterwarnings(
        "ignore", category=FutureWarning, message="adjacency_matrix"
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message="\n\nThe scipy.sparse array containers",
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="networkx.project"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="\nfind_cores"
    )
    warnings.filterwarnings("ignore", category=FutureWarning, message="attr_matrix")
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message=r"\n\nmake_small_.*"
    )
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, message="to_numpy_recarray"
    )
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="info")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message="to_tuple")


@pytest.fixture(autouse=True)
def add_nx(doctest_namespace):
    doctest_namespace["nx"] = networkx
