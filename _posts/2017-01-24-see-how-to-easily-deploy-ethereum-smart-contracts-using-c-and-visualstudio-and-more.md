---
layout: post
title: "See how to easily deploy Ethereum smart contracts using C# and VisualStudio and more"
date: 2017-01-24
description: "The Story"
image: https://cdn-images-1.medium.com/max/800/1*BrxSmz09re9UUV-zVuUADg.png
---

### See how to easily deploy Ethereum smart contracts using C# and VisualStudio and more

![](https://cdn-images-1.medium.com/max/800/1*BrxSmz09re9UUV-zVuUADg.png)*Nethereum is the .Net integration library for Ethereum, it allows you to interact with Ethereum clients like geth, eth or parity using RPC*

### The Story

[In a previous article](https://koukia.ca/build-and-deploy-an-ethereum-smart-contracts-using-visual-studio-10218d3b8091#.e5olix70d) I demonstrated how to use [Solidity Visual Studio Extension](https://marketplace.visualstudio.com/items?itemName=ConsenSys.Solidity) to be able to implement [Ethereum](https://ethereum.org/) Smart Contracts using Visual Studio or Visual Studio Code.

Now I want to show, when your Solidity [Smart Contract](https://www.ethereum.org/greeter) code is ready, how you can actually deploy that smart contract code to the Ethereum network using C# code.

### What do we do?

So first of all, we need an empty C# Console application (Obviously you can do the same thing in a web app or any other app with C# language).

Then we need to install a nuget package called [Nethereum](https://github.com/Nethereum/Nethereum).

![](https://cdn-images-1.medium.com/max/1200/1*GIn7_wEZbwMuCCmParwGTA.png)*Nethereum Nuget packages*

I install all of them, except for the Nethereum.Portable one (I think that one has all the others in it as dependency, so if you want you can just download that single one)

Now, is the time to do some coding.

First thing we need to do in the code is to UnLock the account that will be used to create the contract in the Ethereum network. Any gas price or Ethers transferred to the smart contract will come out of this account’s wallet.

Values that are needed are, the Account’s Public Key, Account’s password, and the time we want the account to stay unlocked.

Before we write the code to deploy the contract we need the smart contract’s abi (contract’s interface) and the smart contract’s byecode which you can get after compiling your contract in Visual Stutio Code or Visual Studio.

You can find the abi and the contract’s byte code, in the bin folder of your Solidity Smart Contract folder in Visual Studio or Visual Studio code. The “*contractname.abi*” file contains the abi json and the “*contractname.bin*” contains the bytecode of your contract.

![](https://cdn-images-1.medium.com/max/1200/1*mkDDIHOOd95Wgbmn8SKrTw.png)

Now that you have the abi and the byte code, let’s get back to the code.

After unlocking the account, it is time to deploy the contract. To deploy the contract you need the contract’s abi (json file), contract’s byte code, Ethers you want to transfer to the contract, gas amount, the public key of the user deploying the contract(the account we unlocked earlier) and any argument if your contract has any constructor with parameters.

That’s it. this last line will return a *transactioHash* which can later on be used to get the actual deployed contract’s public key. If you use the “*testnet*” network it will take some seconds for the transaction to be approved by the network minders.

Once the contract transaction was confirmed you can use the following code using the “*transactionHash*” to get the contract information:

There, we deployed our contract to the Ethereum network with C# and we can give this contract address (The contract’s public key) to anyone who is interested to call it’s functions.

I have a test repository in github that puts this all together in an Asp.net mvc application:

[**aramkoukia/Bethereum**  
*Contribute to Bethereum development by creating an account on GitHub.*github.com](https://github.com/aramkoukia/Bethereum "https://github.com/aramkoukia/Bethereum")

### Book Recommendation

Here are some book recommendation if you are interested:

[**Ethereum: Blockchains, Digital Assets, Smart Contracts, Decentralized Autonomous Organizations**  
*Blockchain For the Non-Technical \*\*\* THIS IS A PREVIEW PRINT \*\*\* As IBM´s official liaison to the Ethereum core…*www.amazon.com](https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3 "https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3")

<https://www.amazon.com/gp/product/1491971940/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491971940&linkId=3c156e0927d49236b14f139d0450c554>

[**Introducing Ethereum and Solidity: Foundations of Cryptocurrency and Blockchain Programming for…**  
*Learn how to use Solidity and the Ethereum project — second only to Bitcoin in market capitalization. Blockchain…*www.amazon.com](https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f "https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f")
