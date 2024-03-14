# Russian-Roulette

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Welcome to The Fray. This is a warm-up to test if you have what it takes to tackle the challenges of the realm. Are you brave enough?

## NOTES

1. Extract contents
   1. > unzip blockchain_russian_roulette.zip
      1. Setup.sol, RussianRoulette.sol
2. Spawn Docker
   1. IP: 83.136.252.194
   2. PORT: 39045 -> RPC connection
   3. PORT: 48986 -> TCP connection
3. Interact with docker
   1. > nc 83.136.252.194 39045
      1. 1 - Connection Infromation
      2. 2 - Restart Instance
      3. 3 - Get Flag
   2. Lets select option 1

        ```text
            Private key     :  0xab4a76acd6a8605ef6653aa685bfcd2cb3e1611620348124b2c203ea9671f233
            Address         :  0x00e6c206EFD2c42DC2d8DF7965812805a52eE617
            Target contract :  0x3deB684224733844A567cA8dc514AFef426D14ec
            Setup contract  :  0x46b54Bb492A6AAC9A5A6cBceDb618Dc2058aD2be
        ```

        1. So this looks like the address data we need
4. CONTRACTS
   1. Setup.sol

        ```s
            pragma solidity 0.8.23;

            import {RussianRoulette} from "./RussianRoulette.sol";

            contract Setup {
                RussianRoulette public immutable TARGET;

                constructor() payable {
                    TARGET = new RussianRoulette{value: 10 ether}();
                }

                function isSolved() public view returns (bool) {
                    return address(TARGET).balance == 0;
                }
            }
        ```

    2. RussianRoulette.sol

        ```s
            pragma solidity 0.8.23;

            contract RussianRoulette {

                constructor() payable {
                    // i need more bullets
                }

                function pullTrigger() public returns (string memory) {
                    if (uint256(blockhash(block.number - 1)) % 10 == 7) {
                        selfdestruct(payable(msg.sender)); // 💀
                    } else {
                    return "im SAFU ... for now";
                    }
                }
            }
        ```

5. PYTHON
   1. Lets create a python script to interact with the contracts (Example from my 2023 Cyber-Apoc Challenge)
   2. We will need w3 python library to work with contracts
