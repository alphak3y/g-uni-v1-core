import { ethers, network } from "hardhat";
import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/dist/src/signer-with-address";
import { getAddresses } from "../src/addresses";

const addresses = getAddresses(network.name);

const op = async (signer: SignerWithAddress) => {
  const gUniFactory = await ethers.getContractAt(
    "GUniFactory",
    addresses.GUniFactory,
    signer
  );

  await gUniFactory.initialize(
    addresses.GUniImplementation,
    addresses.GelatoAdmin,
    addresses.GelatoAdmin,
    {
      gasLimit: 200000,
    }
  );
};

(async () => {
  const [signer] = await ethers.getSigners();
  await op(signer);
})();