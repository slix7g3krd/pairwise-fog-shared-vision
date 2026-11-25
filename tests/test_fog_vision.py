import pytest
import game.fog_vision as mod

CASES = [
    ("fog_dirty_cell_clear", (1,)),
    ("fog_team_ref_reclaim", (1,)),
    ("fog_chunk_version", (1,)),
    ("fog_edge_visibility", (1,)),
    ("fog_event_order_snapshot", (1,)),
    ("fog_tick_resync", (1,)),
    ("load_map_fog", (1,)),
    ("update_vision_grid", (1,)),
    ("merge_team_vision", (1,)),
    ("present_fog", (1,)),
    ("validate_fog", (1,)),
    ("metrics_fog", (1,)),
    ("audit_fog", (1,)),
    ("fallback_fog", (1,)),
    ("determinism_fog", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
