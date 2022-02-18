// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.4;

import {
    ERC20Upgradeable
} from "@openzeppelin/contracts-upgradeable/token/ERC20/ERC20Upgradeable.sol";

contract MockERC20A is ERC20Upgradeable {
    constructor() {
        __ERC20_init("TokenA", "TOKENA");
        _mint(msg.sender, 100000e18);
    }
}

contract MockERC20B is ERC20Upgradeable {
    constructor() {
        __ERC20_init("TokenB", "TOKENB");
        _mint(msg.sender, 100000e18);
    }
}
