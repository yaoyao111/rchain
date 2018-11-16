"""Tests for the testing code itself."""


from rnode_testing.rnode import extract_block_hash_from_propose_output


def test_extract_block_hash_from_propose_output():
    response = "Response: Success! Block a91208047c... created and added.\n"
    assert extract_block_hash_from_propose_output(response) == "a91208047c"
