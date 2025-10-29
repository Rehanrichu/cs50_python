from project import update_state

def test_collect_token():
    state = {'location':'north', 'inventory':[], 'game_over':False}
    update_state("collect", state)
    assert "token1" in state['inventory']

def test_move_north():
    state = {'location':'south', 'inventory':[], 'game_over':False}
    update_state("move north", state)
    assert state['location'] == "north"

def test_invalid_action():
    state = {'location':'north', 'inventory':[], 'game_over':False}
    update_state("fly", state)
    assert state['inventory'] == []
