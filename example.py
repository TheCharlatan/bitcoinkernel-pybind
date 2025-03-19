import bitcoinkernel as bk

main_params = bk.MainNetParams()
chain_type = main_params.GetChainTypeString()
print(f"Chain Type: {chain_type}")
test_params = bk.TestNetParams()
test_chain_type = test_params.GetChainTypeString()
print(f"Chain Type: {test_chain_type}")
