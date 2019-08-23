from check_difference import check_difference


def test_empty_protrusion():
	assert check_difference([],'test.txt') == False

def test_empty_filename():
    assert check_difference([10,10], '') == False

def test_inexistent_filename():
    assert check_difference([10,10], 'nonexistentfile.txt') == False

def test_toosmall_prot():
    assert check_difference([10,10],'new_max_greenchannel_smooth_diffs.ome.tif') == False

def test_positive():
    assert check_difference([326,520,0,1],'new_max_greenchannel_smooth_diffs.ome.tif') == True

def test_ignore_first():
    assert check_difference([356,477,0,0],'new_max_greenchannel_smooth_diffs.ome.tif') == False

def test_noninteger_coords():
    assert check_difference([325.9,520.1,0,1],'new_max_greenchannel_smooth_diffs.ome.tif') == True