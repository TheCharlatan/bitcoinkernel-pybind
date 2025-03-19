import bitcoinkernel

main_params = bitcoinkernel.MainNetParams()

chain_type = main_params.GetChainTypeString()

print(f"Chain Type: {chain_type}")
