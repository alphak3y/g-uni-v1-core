/* eslint-disable @typescript-eslint/naming-convention */
interface Addresses {
  Gelato: string;
  WETH: string;
  DAI: string;
  USDC: string;
  UniswapV3Factory: string;
  Swapper: string;
  GelatoDevMultiSig: string;
  GUniFactory: string;
  GUniImplementation: string;
}

export const getAddresses = (network: string): Addresses => {
  switch (network) {
    case "goerli":
      return {
        Gelato: "0x683913B3A32ada4F8100458A3E1675425BdAa7DF",
        Swapper: "",
        GelatoDevMultiSig: "0xF15C3a5C951722D1eD4176a2e153f0c3ba325474",
        WETH: "",
        DAI: "",
        USDC: "",
        UniswapV3Factory: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        GUniFactory: "",
        GUniImplementation: "",
      };
    default:
      throw new Error(`No addresses for Network: ${network}`);
  }
};
