---
layout: post
title: "Build and deploy #Ethereum smart contracts using Visual Studio"
date: 2017-01-17
description: "The Story: Blockchain and Ethereum network"
image: https://cdn-images-1.medium.com/max/1200/1*GrpshFUAu8l6Sr5u6KGQ4w.png
tags: ["Blockchain", ".NET"]
---

### Build and deploy #Ethereum smart contracts using Visual Studio

![](https://cdn-images-1.medium.com/max/1200/1*GrpshFUAu8l6Sr5u6KGQ4w.png)*A visual of a distributed peer-to-peer application*

### The Story: **Blockchain and Ethereum network**

I’ve been sleepless since I got more familiar with [Blockchain](https://en.wikipedia.org/wiki/Blockchain_%28database%29) and the [Ethereum network](https://ethereum.org/) and [Smart Contracts](https://www.ethereum.org/greeter).

I have been reading and reading and reading and finally I was able to use some of the tools they recommend in the [Ethereum](https://ethereum.org/) website to build and deploy some smart contracts using the official [Ethereum client application](https://github.com/ethereum/mist/releases) (Ethereum Wallet).

I was also able to execute the Smart Contract using the Ethereum client. But then I was like, I need to use a better tool to build smart contracts and they are nothing but pieces of code, so I found out that I can do it within Visual Studio as well as the [Visual Studio Code](https://github.com/juanfranblanco/vscode-solidity).

### What did I do? **Built smart contracts with Visual Studio**

To build Ethereum Smart Contracts with Visual Studio you need the [Solidity Extension](https://marketplace.visualstudio.com/items?itemName=ConsenSys.Solidity) found in the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ConsenSys.Solidity).

![](https://cdn-images-1.medium.com/max/800/1*QgTlsrqY_Of8aOBCS5TWhA.png)*Solidity Extension in Visual Studio Marketplace*

#### First Smart Contract Project

After downloading that, you will have the Solidity Project Template right in the Visual Studio, File => New Project: Then select the “**Smart Contract Project**” template and click OK.

![](https://cdn-images-1.medium.com/max/1200/1*FcDmp4hhUbd4malF8-u9rQ.png)*Solidity Smart Contract Project Template in Visual Studio*

As you can see in the Solution Explorer, the template comes with 3 sample Smart Contracts (.sol files) which are our Solidity files.

![](https://cdn-images-1.medium.com/max/800/1*uGIX1KYv_Acp9oD95or3IA.png)*Solidity Project Template — Smart Contract Samples*

Here is how the Payout.sol sample looks like:

Boom, you got your first Ethereum smart contract in Visual Studio.

#### Compile and Deploy

Next thing you want to do, after you built [your brilliant idea](http://dapps.ethercasts.com/) with smart contracts, you need to Compile it.

So just right click on the .sol file and select Compile.

![](https://cdn-images-1.medium.com/max/800/1*-gZN-m9c4wCSs_gjCbqf5Q.png)*Compile a Solidity File from Visual Studio*

Now it’s time to deploy your smart contract to the Ethereum network.

To do that we need to setup the project with the Blockchain information, so right click on the project and select Properties:

![](https://cdn-images-1.medium.com/max/800/1*WuJMhzGA7mNpn9ff3EUo1A.png)*Smart Contract Project Properties*

After entering the Blockchain password, the BlockChain Service URL (Or otherwise known as The RPC Url), you can Deploy your Smart Contract to the network.

Just right click on the Smart Contract (.sol file) and select “Deploy Smart Contract”.

**Note: For the Smart Contract deployment to work, you need Geth console to be running on your computer. So if you are deploying to testnet network, open a command prompt and type in below command before clicking on Deploy:**

```
geth --testnet
```

![](https://cdn-images-1.medium.com/max/800/1*Xphr6cCbD8ZM5lc4SBdbgQ.png)*Deploying a Solidity Smart Contract from Visual Studio*

And there you have it. Your distributed application’s back-end services is up and running in the network, and people can execute it as they wish.

### Any thing else?

Interested in exploring the smart contract you just deployed, the transations on it an all the details?

You can use the etherscan.io website for the testnet Ethereum network using the address of the contract you just deployed.

The following url is the one i just deployed:

**Note:** The [0x061e4d089f5341786fade6277d2a0e9526551500](https://testnet.etherscan.io/address/0x061e4d089f5341786fade6277d2a0e9526551500) is the public key of the smart contract.

[**Ethereum Account 0x061e4d089f5341786fade6277d2a0e9526551500 Info**  
*The Ethereum BlockChain Explorer, API and Analytics Platform*testnet.etherscan.io](https://testnet.etherscan.io/address/0x061e4d089f5341786fade6277d2a0e9526551500 "https://testnet.etherscan.io/address/0x061e4d089f5341786fade6277d2a0e9526551500")

And this is what you will see:

![](https://cdn-images-1.medium.com/max/1200/1*F9EAq-zKpQnGPt8BHBrW1Q.png)*Overview of a Smart Contract on Etherscan website on testnet Ethereum network*

As you can see everything in the contract is visible to everyone with 100% transparency!

### Book Recommendation

Here are some book recommendation if you are interested:

[**Ethereum: Blockchains, Digital Assets, Smart Contracts, Decentralized Autonomous Organizations**  
*Blockchain For the Non-Technical \*\*\* THIS IS A PREVIEW PRINT \*\*\* As IBM´s official liaison to the Ethereum core…*www.amazon.com](https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3 "https://www.amazon.com/gp/product/1523930470/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1523930470&linkId=c82362da36588ebb20b557d2fbf25df3")

<https://www.amazon.com/gp/product/1491971940/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1491971940&linkId=3c156e0927d49236b14f139d0450c554>

[**Introducing Ethereum and Solidity: Foundations of Cryptocurrency and Blockchain Programming for…**  
*Learn how to use Solidity and the Ethereum project - second only to Bitcoin in market capitalization. Blockchain…*www.amazon.com](https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f "https://www.amazon.com/gp/product/1484225341/ref=as_li_tl?ie=UTF8&tag=aramkoukia-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1484225341&linkId=290599f896e774b8890420998653660f")
