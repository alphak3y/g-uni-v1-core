/* eslint-disable @typescript-eslint/naming-convention */
interface Addresses {
  UniswapV3Factory: string;
  Gelato: string;
  WETH: string;
  DAI: string;
  MetaPoolFactory: string;
  gUNIV3: string;
  Swapper: string;
  GelatoAdmin: string;
}

export const getAddresses = (network: string): Addresses => {
  if (network == "rinkeby") {
    return {
      UniswapV3Factory: "0xFeabCc62240297F1e4b238937D68e7516f0918D7",
      Gelato: "0xD90fC89e89E3E5b75256b5aA617f887C583b29a2",
      WETH: "0xc778417E063141139Fce010982780140Aa0cD5Ab",
      DAI: "0x5592EC0cfb4dbc12D3aB100b257153436a1f0FEa",
      MetaPoolFactory: "0xb4Cecd92ADc5CDb0Dd877d6D8203Ac4Eb9db242D",
      gUNIV3: "0xb6b312AE470126D09e2E47a395c2b783dd82366d",
      Swapper: "0x52327D6d94B77AEc83664A4e4758aEA5E34b8574",
      GelatoAdmin: "0x88215a2794ddC031439C72922EC8983bDE831c78",
    };
  } else if (network == "ropsten") {
    return {
      UniswapV3Factory: "0x273Edaa13C845F605b5886Dd66C89AB497A6B17b",
      Gelato: "0xCc4CcD69D31F9FfDBD3BFfDe49c6aA886DaB98d9",
      WETH: "0xc778417E063141139Fce010982780140Aa0cD5Ab",
      DAI: "0xaD6D458402F60fD3Bd25163575031ACDce07538D",
      MetaPoolFactory: "0x7DE83D96a084643568A8740634Ca7F3f3B28acDE",
      gUNIV3: "0x788377ae260B1D7B45Ce1528e14557953E742680",
      Swapper: "0x2E185412E2aF7DC9Ed28359Ea3193EBAd7E929C6",
      GelatoAdmin: "0xD90fC89e89E3E5b75256b5aA617f887C583b29a2",
    };
  } else if (network == "mainnet") {
    return {
      UniswapV3Factory: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
      Gelato: "0x3CACa7b48D0573D793d3b0279b5F0029180E83b6",
      WETH: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
      DAI: "0x6B175474E89094C44Da98b954EedeAC495271d0F",
      MetaPoolFactory: "0x8582Bf142BE76fEF830D23f590a2587f2aD7C216",
      gUNIV3: "0x29DFc3E6eDB63965Cf35e343Fa583a926F22410C",
      Swapper: "",
      GelatoAdmin: "0x163407FDA1a93941358c1bfda39a868599553b6D",
    };
  } else {
    throw new Error(`No addresses for Network: ${network}`);
  }
};
