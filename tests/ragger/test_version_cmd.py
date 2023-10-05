from starknet_client.boilerplate_cmd_builder import BoilerplateCommandBuilder

def test_version(backend, firmware):
    rapdu: RAPDU = backend.exchange(<whatever>)
    assert cmd.get_version() == (0, 1, 1)
