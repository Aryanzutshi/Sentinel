
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import {
    ERC2771Context
} from "@gelatonetwork/relay-context/contracts/vendor/ERC2771Context.sol";

contract PaymentsInterface is ERC2771Context {
    mapping(address => uint256) private balances;
    mapping(address => Transaction[]) private transactions;

    struct Transaction {
        address to;
        uint256 amount;
        uint256 timestamp;
    }

    constructor(address trustedForwarder) ERC2771Context(trustedForwarder) payable {
        (bool success,) = _msgSender().call{value: msg.value}("");
        if (!success)
            revert("Transfer failed.");
            
    }

    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        
       // balances[_msgSender()] += msg.value;
    }

    function withdraw(uint256 amount) public {
        address caller = _msgSender();
        require(balances[caller] >= amount, "Insufficient balance");
        balances[caller] -= amount;
        payable(caller).transfer(amount);
    }

    function getBalance(address user) public view returns (uint256) {
        return balances[user];
    }

    function transfer(address to, uint256 amount) public {
        address caller = _msgSender();
        require(balances[caller] >= amount, "Insufficient balance");
        balances[caller] -= amount;
        balances[to] += amount;

        // Record transaction
        transactions[caller].push(Transaction(to, amount, block.timestamp));
        transactions[to].push(Transaction(caller, amount, block.timestamp));
    }

    function getTransactionHistory(address user) public view returns (Transaction[] memory) {
        return transactions[user];
    }
}
